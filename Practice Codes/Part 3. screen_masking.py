import numpy as np
from PIL import ImageGrab
import cv2
import time

def roi(image, vertices):
    #define Region-Of-Interest by masking
    #do not need sky view or pedestrian street view
    #only focus on the road
    mask = np.zeros_like(image)
    #make black image with same size 
    cv2.fillPoly(mask, vertices, 255)
    #fill the given vertices of the mask white
    masked = cv2.bitwise_and(image, mask)
    #black(00000000) + image = black, white(11111111) + image = image
    return masked



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

    vertices = np.array([[10, 500], [10,300], [300, 200], [500,200], [800, 300], [800, 500]])
    processed_img = roi(processed_img, [vertices])
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
    
