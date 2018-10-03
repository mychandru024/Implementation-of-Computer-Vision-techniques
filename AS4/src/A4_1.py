import numpy as np
import cv2

# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((5*5,3), np.float32)
objp[:,:2] = np.mgrid[0:5,0:5].T.reshape(-1,2)

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

fname = "CB.png"

img = cv2.imread(fname)
print(img.shape)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Find the chess board corners
ret, corners = cv2.findChessboardCorners(gray, (5,5),None)
print(ret)

# If found, add object points, image points (after refining them)
if ret == True:
	objpoints.append(objp)

	cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
	imgpoints.append(corners)

	# Draw and display the corners
	cv2.drawChessboardCorners(img, (7,6), corners,ret)
	cv2.imshow('img',img)
	cv2.waitKey(500)

cv2.destroyAllWindows()
print(imgpoints)
print(len(imgpoints))

#write image points to a file
