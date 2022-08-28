# for image processing
import cv2

# mathematical library for image handling
import numpy as np

import time

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

time.sleep(2)
background = 0
for i in range(50):
    ret, background = cam.read()

background = np.flip(background, axis=1)

while cam.isOpened():
    ret, current_frame = cam.read()

    if ret:
        current_frame = np.flip(current_frame, axis=1)

        hsv = cv2.cvtColor(current_frame, cv2.COLOR_BGR2HSV)

        lower_red = np.array([0, 120, 50])
        upper_red = np.array([10, 255, 255])
        mask1 = cv2.inRange(hsv, lower_red, upper_red)

        lower_red = np.array([170, 120, 50])
        upper_red = np.array([180, 255, 255])
        mask2 = cv2.inRange(hsv, lower_red, upper_red)

        red_mask = mask1 + mask2

        close_mask = cv2.morphologyEx(red_mask, cv2.MORPH_CLOSE, np.ones((7, 7), np.uint8))
        open_mask = cv2.morphologyEx(close_mask, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
        dilation = cv2.dilate(open_mask, np.ones((10, 10), np.uint8), iterations=1)

        result1 = cv2.bitwise_and(background, background, mask=dilation)
        red_free = cv2.bitwise_not(dilation)
        result2 = cv2.bitwise_and(current_frame, current_frame, mask=red_free)

        final_result = cv2.addWeighted(result1, 1, result2, 1, 0)

        cv2.imshow("Cloak", final_result)

        k = cv2.waitKey(10)

        if k == 27:
            break

cam.release()
cv2.destroyAllWindows()
