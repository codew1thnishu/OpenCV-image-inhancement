import cv2
import numpy as np

# Load reference image
img1 = cv2.imread(r"c:\Users\nisarg prajapati\OneDrive\Documents\Downloads\360p-resolution.jpg", 0)

# Start webcam
cap = cv2.VideoCapture(0)

# Create SIFT detector
sift = cv2.SIFT_create()

# Detect keypoints in reference image
kp1, des1 = sift.detectAndCompute(img1, None)

# FLANN Matcher
FLANN_INDEX_KDTREE = 1

index_params = dict(
    algorithm=FLANN_INDEX_KDTREE,
    trees=5
)

search_params = dict(checks=50)

flann = cv2.FlannBasedMatcher(index_params, search_params)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    kp2, des2 = sift.detectAndCompute(gray, None)

    if des2 is not None:

        matches = flann.knnMatch(des1, des2, k=2)

        good = []

        for m, n in matches:
            if m.distance < 0.7 * n.distance:
                good.append(m)

        if len(good) > 15:

            src_pts = np.float32(
                [kp1[m.queryIdx].pt for m in good]
            ).reshape(-1,1,2)

            dst_pts = np.float32(
                [kp2[m.trainIdx].pt for m in good]
            ).reshape(-1,1,2)

            M, mask = cv2.findHomography(
                src_pts,
                dst_pts,
                cv2.RANSAC,
                5.0
            )

            if M is not None:

                h, w = img1.shape

                pts = np.float32([
                    [0,0],
                    [0,h],
                    [w,h],
                    [w,0]
                ]).reshape(-1,1,2)

                dst = cv2.perspectiveTransform(pts, M)

                frame = cv2.polylines(
                    frame,
                    [np.int32(dst)],
                    True,
                    (0,255,0),
                    3
                )

                cv2.putText(
                    frame,
                    "Object Detected",
                    (20,40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0,255,0),
                    2
                )

        cv2.putText(
            frame,
            f"Matches: {len(good)}",
            (20,80),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255,0,0),
            2
        )

    cv2.imshow("SIFT Object Detection", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()