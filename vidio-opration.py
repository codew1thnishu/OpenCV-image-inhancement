import cv2
video =  cv2.VideoCapture(r"C:\Users\nisarg prajapati\Downloads\video.mp4")
while(video.isOpened()):
    ret, frame = video.read()
    if ret == True:
        cv2.imshow('Video Playback',frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
    else:
        break
video.release()
cv2.destroyAllWindows()