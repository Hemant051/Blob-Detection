#Blob Detection
import cv2
import numpy as np
 
# Load image
image = cv2.imread('emoji.jpg', 0)
 
# Set our filtering parameters
# Initialize parameter settiing using cv2.SimpleBlobDetector
params = cv2.SimpleBlobDetector_Params()
 
# Set Area filtering parameters
params.filterByArea = True
params.minArea = 100
 
# Set Circularity filtering parameters
params.filterByCircularity = True
params.minCircularity = 0.9
 
# Set Convexity filtering parameters
params.filterByConvexity = True
params.minConvexity = 0.2
     
# Set inertia filtering parameters
params.filterByInertia = True
params.minInertiaRatio = 0.01
 
# Create a detector with the parameters
detector = cv2.SimpleBlobDetector_create(params)
     
# Detect blobs
keypoints = detector.detect(image)
 
# Draw blobs on our image as red circles
blank = np.zeros((1, 1))
blobs = cv2.drawKeypoints(image, keypoints, blank, (255,0 ,0 ),
                          cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
 
number_of_blobs = len(keypoints)
text = "Number of Circular Blobs: " + str(len(keypoints))
cv2.putText(blobs, text, (20, 550),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 100, 255), 3)
 
# Show blobs
cv2.imshow("Filtering Circular Blobs Only", blobs)
#Putting wait key to hold the image for longer interval
cv2.waitKey(0)
cv2.destroyAllWindows()

