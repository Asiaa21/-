from PIL import ImageFilter
from PIL import Image 
import numpy as np
import sys 
import cv2

try: 
    img = Image.open(r"C:\Users\Asia\OneDrive\Desktop\1-project\img\1.jpg")
except IOError:
    print("Unable to load image")
    sys.exit(1)

bw_img = img.convert('L')
bw_img.save('чб1.jpg')
bw_img.show()

bw_array = np.array(bw_img)
threshold_value = 128
_, binary_mask = cv2.threshold(bw_array, threshold_value, 255, cv2.THRESH_BINARY)
binary_mask_img = Image.fromarray(binary_mask)
binary_mask_img.save('макска бін1.jpg')
binary_mask_img.show()

object_image = np.copy(np.array(img))
object_image[binary_mask == 0] = 0 
object_image_pil = Image.fromarray(object_image)
object_image_pil.save('вир1.jpg')
object_image_pil.show()


try: 
    img = Image.open(r"C:\Users\Asia\OneDrive\Desktop\1-project\img\2.jpg")
except IOError:
    print("Unable to load image")
    sys.exit(1)

bw_img = img.convert('L')
bw_img.save('чб2.jpg')
bw_img.show()

bw_array = np.array(bw_img)
threshold_value = 128
_, binary_mask = cv2.threshold(bw_array, threshold_value, 255, cv2.THRESH_BINARY)
binary_mask_img = Image.fromarray(binary_mask)
binary_mask_img.save('макска бін2.jpg')
binary_mask_img.show()

object_image = np.copy(np.array(img))
object_image[binary_mask == 0] = 0 
object_image_pil = Image.fromarray(object_image)
object_image_pil.save('вир2.jpg')
object_image_pil.show()


try: 
    img = Image.open(r"C:\Users\Asia\OneDrive\Desktop\1-project\img\3.jpg")
except IOError:
    print("Unable to load image")
    sys.exit(1)

bw_img = img.convert('L')
bw_img.save('чб3.jpg')
bw_img.show()

bw_array = np.array(bw_img)
threshold_value = 128
_, binary_mask = cv2.threshold(bw_array, threshold_value, 255, cv2.THRESH_BINARY)
binary_mask_img = Image.fromarray(binary_mask)
binary_mask_img.save('макска бін3.jpg')
binary_mask_img.show()

object_image = np.copy(np.array(img))
object_image[binary_mask == 0] = 0 
object_image_pil = Image.fromarray(object_image)
object_image_pil.save('вир3.jpg')
object_image_pil.show()



try: 
    img = Image.open(r"C:\Users\Asia\OneDrive\Desktop\1-project\img\4.jpg")
except IOError:
    print("Unable to load image")
    sys.exit(1)

bw_img = img.convert('L')
bw_img.save('чб4.jpg')
bw_img.show()

bw_array = np.array(bw_img)
threshold_value = 128
_, binary_mask = cv2.threshold(bw_array, threshold_value, 255, cv2.THRESH_BINARY)
binary_mask_img = Image.fromarray(binary_mask)
binary_mask_img.save('макска бін4.jpg')
binary_mask_img.show()

object_image = np.copy(np.array(img))
object_image[binary_mask == 0] = 0 
object_image_pil = Image.fromarray(object_image)
object_image_pil.save('вир4.jpg')
object_image_pil.show()