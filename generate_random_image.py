from imutils import paths
import numpy as np
import cv2

class Generate:
    @staticmethod
    def image():
        MODEL_FILENAME = "captcha_breaker_basic1/captcha_model.hdf5"
        CAPTCHA_IMAGE_FOLDER = "captcha_breaker_basic1/generated_captcha_images"
        captcha_image_files = list(paths.list_images(CAPTCHA_IMAGE_FOLDER))
        image_file = np.random.choice(captcha_image_files, size=1, replace=False)
        image_file = image_file[0]
        print(image_file)
        image = cv2.imread(image_file)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Add some extra padding around the image
        image = cv2.copyMakeBorder(image, 20, 20, 20, 20, cv2.BORDER_REPLICATE)

# threshold the image (convert it to pure black and white)
        thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

        output = cv2.merge([thresh] * 3)
        img_file = cv2.imwrite("img.png", output)
        return img_file

