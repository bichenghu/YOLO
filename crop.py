#coding=utf-8
import cv2
import os
import pylab as plb
import PIL.Image as Image

import os
#读取path路径下的 jpg文件
def getAllFrames(dir):
    #f.endswith（）  限制文件类型
    #f.endswith('.jpg')|f.endswith('.png')  改成这句可以读取jpg/png格式的文件
    #注意 返回的是绝对路径
   return [os.path.join(dir,f) for f in os.listdir(dir) if f.endswith('.jpg')]

#循环读图
for dir in getAllFrames(r'/home/hbc/data/smartcity/dataset3/Cam5/frames/'):
    frame = Image.open(dir)
    label = os.path.splitext(dir.replace('frames','labels'))[0]+'.txt'
    print ('in '+label)
    file=open(label, 'r')
    i = 0
    for line in file.readlines():
        i += 1
        data = line.split( )
        x = data[0]
        y = data[1]
        w = data[2]
        h = data[3]        
        print ('box '+str(i)+': '+'x:'+x+' '+'y:'+y+' '+'w:'+w+' '+'h:'+h)
        #box中的数必须是 int 否则会报错
        bbox = [int(x),int(y),int(w),int(h)]
        result = frame.crop(bbox)
        gallery = os.path.splitext(dir.replace('frames/','gallery/dataset3_Cam5_'))[0]+'_'+str(i)+'.jpg'
        result.save(gallery)

