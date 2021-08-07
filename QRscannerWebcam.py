from cv2 import cv2
import pyzbar.pyzbar as pyzbar
import datetime , keyboard

cap = cv2.VideoCapture(0)
cap.set(3,1000)  # Webcam Width & Height
cap.set(4,600)

detector = cv2.QRCodeDetector()

while cap.isOpened() :

    success,image = cap.read()  # READ frames of video

    if not success :
        print('Skiping empty frame.')
    
    decodedObjects = pyzbar.decode(image) # Decoding qr code data

    cv2.rectangle(image,(0,0),(1000,80),(245,176,66),-1) # Background rectangle to display text

    for obj in decodedObjects : 

        data = obj.data.decode('utf-8')

        cv2.putText(image,data,(20,50),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,250),2) # Display data in qr code

        x,y,w,h = obj.rect # get qr code coordinates to draw rectangle
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,250,0),2) # Rectangle around qr code

    cv2.imshow('QR CODE SCANNER',image)  # Show webcam feed

    if cv2.waitKey(5) & 0xFF == 27 :
        break

cap.release()
cv2.destroyAllWindows()