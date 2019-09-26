import asvmq
import asvprotobuf.sensor_pb2
import cv2
import time
import base64
import numpy as np

t = time.time()

asvmq.init()

def cb(data, args=[]):
    global t
    frame = cv2.imdecode(np.frombuffer(base64.b64decode(data.image), np.uint8), cv2.IMREAD_COLOR)

    print(1/(time.time()-t))
    t = time.time()

pub = asvmq.Subscriber("camera", asvprotobuf.sensor_pb2.Image, cb)

asvmq.spin()
