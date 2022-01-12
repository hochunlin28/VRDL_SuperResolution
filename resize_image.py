import cv2
from os import listdir

test_dir = './test/'
test_list = listdir(test_dir)

for img_name in test_list:
    img = cv2.imread(test_dir + img_name)
    h,w,a = img.shape
    img = cv2.resize(img, (w*3,h*3), interpolation=cv2.INTER_CUBIC)
    cv2.imwrite(test_dir + img_name, img)
