import cv2

face_cascade = cv2.CascadeClassifier('Section 17 - Image and Video Processing/Face Detection/haarcascade_frontalface_default.xml')
video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(grey_frame, scaleFactor=1.2, minNeighbors=5)

    for x, y, w, h in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
    
    cv2.imshow('Webcam', frame)
    
    # Exit loop on 'q' keypress
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
