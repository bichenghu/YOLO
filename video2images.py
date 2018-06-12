import cv2
f=0
cap = cv2.VideoCapture('/home/hbc/data/smartcity/dataset3/Cam5.avi')
if cap.isOpened():
    rval,frame = cap.read()
else:
    rval = False
while rval:
    rows,cols,channel = frame.shape
    #if(f%5 == 0) #Set the frame rate
    _path = '/home/hbc/data/smartcity/images/dataset3/Cam5/'+str(f).zfill(6)+'.jpg'
    cv2.imencode('.jpg',frame)[1].tofile(_path)  
    print ('saving %s' % _path)
    f = f+1
    cv2.waitKey(1)
    rval,frame = cap.read()
cap.release()
print ('total saved %d jpgs' % f)

