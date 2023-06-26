#!/usr/bin/env python3
import cv2
import sys

def cropfile(filename):
    print(f"cropppying again from {filename}")
    # Load the image
    img = cv2.imread(filename)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Threshold the image: below 240 is considered black (i.e., not background), else white
    _, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)

    # Find contours in the threshold image
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # For each contour, check the area. If it's above a threshold, consider it as an image and crop
    min_area = 200  # Minimum area to be considered as an image. Adjust as needed.

    for i, cnt in enumerate(contours):
        # Calculate contour area
        area = cv2.contourArea(cnt)
    
        if (area > min_area):
            x, y, w, h = cv2.boundingRect(cnt)
            crop = img[y:y+h, x:x+w]
            if (crop.shape != img.shape):
                cv2.imwrite(f'cropped_image{i}.jpg', crop)


if __name__ == "__main__":
    filelist = sys.argv[1::]
    for filename in filelist:
        print(f"cropping {filename}")
        cropfile(filename)

