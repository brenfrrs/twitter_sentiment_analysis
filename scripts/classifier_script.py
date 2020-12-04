import opencv@2
import numpy as np
import pandas as pd


while True:
    k = cv2.waitKey(1) & 0xFF
    # press 'q' to exit
    if k == ord('q'):
        break
    elif k == ord('b'):
        print('hi')
        # change a variable / do something ...
    elif k == ord('k'):
        print('bye')
        # change a variable / do something ...
