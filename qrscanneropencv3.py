from cv2 import cv2
import pyzbar.pyzbar as pyzbar
import datetime , keyboard , time

cap = cv2.VideoCapture(0)
cap.set(3,1000) # Camera Width
cap.set(4,600)  # Camera Height
detector = cv2.QRCodeDetector()

filename = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
filename = filename.replace(':','-')
filename = 'QRScanData_'+filename.replace(' ','_')+'.txt'

#file = open(filename, "wb")

while cap.isOpened():

	success,image = cap.read()

	if not success :
		print('Skipping Empty Frame ! ')
		continue

	decodedObjects = pyzbar.decode(image)

	#if decodedObjects == [] :
	#	cv2.putText(image,'QR Code Not Detected !',(50, 50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2) 

	cv2.rectangle(image,(0,0),(1000,80),(245,176,66),-1)

	for obj in decodedObjects:

		data = obj.data.decode('utf-8')
		cv2.putText(image,data,(20, 50),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,250),2)	
		x,y,w,h = obj.rect
		cv2.rectangle(image,(x,y),(x+w,y+h),(0,250,0),2)
		
		with open(filename, 'a') as the_file:
			the_file.write(data+'\n')
		the_file.close()

	cv2.imshow("QR SCANNER",image)
    
	#print('[Press \'q\' to print results !]')
	if cv2.waitKey(5) & 0xFF == 27 :
		break
	if keyboard.is_pressed('q') :
		break


#print(set(the_file.readlines()))

cap.release()
cv2.destroyAllWindows()