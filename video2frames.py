import cv2
f=0
c=0
cap = cv2.VideoCapture('/home/hbc/data/smartcity/dataset2/Cam3/Cam3.avi')
if cap.isOpened():
    rval,frame = cap.read()
else:
    rval = False
while rval:
    rows,cols,channel = frame.shape
    #Set the frame rate
    if(f%5 == 0):
        _path = '/home/hbc/data/smartcity/dataset2/Cam3/frames/'+str(c).zfill(6)+'.jpg'
        cv2.imencode('.jpg',frame)[1].tofile(_path)  
        print ('saving %s' % _path)
        c = c + 1
        cv2.waitKey(1)
    f = f + 1
    rval,frame = cap.read()
cap.release()
print ('total saved %d imagess' % c)

