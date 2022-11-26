import cv2
import matplotlib.pyplot as plt
import cvlib
from cvlib.object_detection import draw_bbox

im = cv2.imread("cars_1.jpeg")

bbox ,label,conf = cvimagedetect_cammon_objects(im)

output_image = draw_bbox(im, bbox, label, conf)
plt.imshow(output_image)
plt.show()