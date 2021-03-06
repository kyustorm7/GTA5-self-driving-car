import numpy as np
from PIL import ImageGrab
import cv2
import time

def process_img(original_image):
    #images need to be simplified for processsing
    #in this case, we want to get the lanes
    #however, since we need to get the lane lines back on the original image
    #it is important to keep the original image
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    #convert original image to grayscale image
    #[256, 256, 256] to [256]; decrease file size
    processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=300)
    #use feature detection (edge detection)
    return processed_img



last_time = time.time()
while(True):
    #game is running at resolution 800X600
    screen = np.array(ImageGrab.grab(bbox=(0,40,800, 640)))

    #make new processed image (edge detection)
    new_screen = process_img(screen)
    
    #print program time
    print('Loop took {} seconds' .format(time.time() - last_time))
    last_time = time.time()
    cv2.imshow('window', new_screen)
    
    ###cv2.imshow('window2', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
    ###do not delete b/c need later

    if cv2.waitKey(25)&0xFF==ord('q'):
        cv2.destroyAllWindows()
        break
    
