# YOLO: Real-Time Object Detection
You only look once (YOLO) is a state-of-the-art, real-time object detection system. On a Pascal Titan X it processes images at 30 FPS and has a mAP of 57.9% on COCO test-dev.

The original YOLO run with [darknet](http://pjreddie.com/darknet) which is an open source neural network framework written in C and CUDA. It is fast, easy to install, and supports CPU and GPU computation.

This project is a modified version for some requirements such as saving labes, saving video and creating dataset for training.

### Modified 1 检测多张图片并保存标签信息
对于单张图片检测：
```
#不指定输出路径
./darknet detect cfg/yolov3.cfg yolov3.weights /home/username/data/xxx.jpg
#指定输出路径
./darknet detect cfg/yolov3.cfg yolov3.weights /home/username/data/xxx.jpg -out result
```
其中不指定输出路径的命令在darknet/目录下生成predictions.jpg；指定输出路径的时候只需要输入图片名，图片格式规定为.jpg

事实上，单张图片的测试也可以用如下通用方式：
```
./darknet detctor test cfg/coco.data cfg/yolov3.cfg yolov3.weights /home/username/data/xxx.jpg
```
对于多张图片检测：
如果上述通用命令不指定输出路径，就能实现多张图片测试，作者写的多张图片测试是在加载一次模型后，再一次一次的输入图片路径测试，这样的方式似乎不太实用，一般情况下我们想在一个文件夹下对所有图片进行检测，保存其标签信息，这就需要到修改源码来实现。需要修改到的文件主要有：include/darknet.h src/image.c examples/detector.c examples/darknet.c

修改之后，对于单张图片，可以用如下命令：
```
./darknet detect cfg/yolov3.cfg yolov3.weights -input /home/username/data/xxx.jpg -out test
```
对于文件夹内多张图片，可以用如下命令：
```
./darknet detect cfg/yolov3.cfg yolov3.weights -idir /home/username/data/imagedir/ -odir /home/username/data/results/
```
当然，在results目录下要提前建好images和labels文件夹。
