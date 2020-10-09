'''
===============================================================================
ENGR 133 Fa 2020

Assignment Information
	Assignment:     e.g. Py1 Task 1
	Author:         Jonathan Budiman, jbudiman@purdue.edu
	Team ID:        LC1-15
	
Contributors:   Yolanda Chen, chen2633@purdue 
                Collin Gernhardt, cgernhar@purdue 
                Rachel Evrard, revrard@purdue 
	My contributor(s) helped me:	
	[X] understand the assignment expectations without
		telling me how they will approach it.
	[X] understand different ways to think about a solution
		without helping me plan my solution.
	[X] think through the meaning of a specific error or
		bug present in my code without looking at my code.
	Note that if you helped somebody else with their code, you
	have to list that person as a contributor here as well.
===============================================================================
'''
import numpy as np
import matplotlib.pyplot as plt
image = plt.imread('Purdue_Arch.png')
import matplotlib.image as mpimg
#Read and Process image file
plt.imshow(image)


#Start Python smoothing
def smoothing(gray):
    tempSum = 0
    smoothA = np.zeros((len(gray), len(gray[0])))
    #smoothingArray = np.array([1,1,1],[1,1,1],[1,1,1])
    dividingFactor = 9
    
    for i in range(len(gray)):
        for j in range(len(gray[0])):
            if j < len(gray[0]) - 1:
                tempSum += gray[i][j+1]
                if i < len(gray) - 1:
                    tempSum += gray[i+1][j+1]
            if j > 0:
                tempSum += gray[i][j-1]
                if i > 0:
                    tempSum += gray[i-1][j-1]
            if i < len(gray) - 1:
                tempSum += gray[i+1][j]
                if j > 0:
                    tempSum += gray[i+1][j-1]
            if i > 0:
                tempSum += gray[i-1][j]
                if j < len(gray[0]) - 1:
                    tempSum += gray[i-1][j+1]
                    
            tempSum += gray[i][j]

            smoothA[i][j] = tempSum/dividingFactor
            
            tempSum = 0
    
    return smoothA
            
#End Python smoothing
def rgbG(RGB):
    return np.dot(RGB[...,:3], [0.2126, 0.7152, 0.0722])

img = mpimg.imread('Purdue_Arch.png')     
gray = rgbG(img)    
plt.imshow(gray, cmap=plt.get_cmap('gray'), vmin=0, vmax=1)
plt.show()
#plt.imshow(gray)

smoothedArray = smoothing(gray)

plt.imshow(smoothedArray, cmap=plt.get_cmap('gray'), vmin=0, vmax=1)


'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''