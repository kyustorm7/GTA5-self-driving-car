import numpy as np
from PIL import ImageGrab
import cv2
import time

last_time = time.time()
while(True):
    # game is running at resolution 800X600
    screen = np.array(ImageGrab.grab(bbox=(0,40,800, 640)))
    
    ## print program time
    print('Loop took {} seconds' .format(time.time() - last_time))
    last_time = time.time()
    
    cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
    #opencv runs at BGR instead of RGB
    if cv2.waitKey(25)&0xFF==ord('q'):
        cv2.destroyAllWindows()
        break
    
