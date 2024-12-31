import cv2

cap = cv2.VideoCapture(0)

fileName = "D:\\Videolar\\kayit.mp4"
codec = cv2.VideoWriter_fourcc(*"mp4v")

frameRate = 30
resolution = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

videoFileOutput = cv2.VideoWriter(fileName, codec, frameRate, resolution)

sayac = 0
baslat = False

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    frame = cv2.flip(frame, 1)
    cv2.imshow("Webcam Live", frame)
    
    if baslat:
        videoFileOutput.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        baslat = True
    
    if cv2.waitKey(1) & 0xFF == ord('q') or sayac == 1000:
        break

    if baslat == False:
        sayac += 1



videoFileOutput.release()
cap.release()
cv2.destroyAllWindows()