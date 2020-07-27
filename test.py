from generate_random_image import Generate
image = Generate.image()
import cv2
cv2.imshow("img", image)
cv2.waitKey(0)
