import asvmq
import asvprotobuf.sensor_pb2
import imutils.video
import cv2
import time
import base64
import sys

id = int(sys.argv[1])
cam = imutils.video.VideoStream(src=id)
cam.start()

pub = asvmq.Publisher("camera".format(id), asvprotobuf.sensor_pb2.Image)

while True:
    t = time.time()
    im_obj = asvprotobuf.sensor_pb2.Image()
    im_obj.header.frame_id = "camera{}".format(id+1)
    im_obj.header.stamp = time.time()
    im_obj.format = 1
    im_obj.image = base64.b64encode(cv2.imencode(".png", cam.read())[1].tostring())
    pub.publish(im_obj)
    print(1/(time.time()-t))
