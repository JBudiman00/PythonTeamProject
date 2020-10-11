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
import math

#Start Python high filter
def highFilterX(smooth, Kernal):
    tempSum = 0
    edgeA = np.zeros((len(smooth), len(smooth[0])))
    
    #Iterate through each pixel
    for i in range(len(smooth)):
        for j in range(len(smooth[0])):
            #If statements check for edge cases along border of matrix
            if j < len(smooth[0]) - 1:
                tempSum += smooth[i][j+1]*Kernal[1][2]
                if i < len(smooth) - 1:
                    tempSum += smooth[i+1][j+1]*Kernal[2][2]
            if j > 0:
                tempSum += smooth[i][j-1]*Kernal[1][0]
                if i > 0:
                    tempSum += smooth[i-1][j-1]*Kernal[0][0]
            if i < len(smooth) - 1:
                if j > 0:
                    tempSum += smooth[i+1][j-1]*Kernal[2][0]
            if i > 0:
                if j < len(smooth[0]) - 1:
                    tempSum += smooth[i-1][j+1]*Kernal[0][2]
            
            edgeA[i][j] = tempSum

            tempSum = 0
    
    return edgeA

def highFilterY(smooth, Kernal):
    tempSum = 0
    edgeA = np.zeros((len(smooth), len(smooth[0])))
    
    #Iterate through each pixel
    for i in range(len(smooth)):
        for j in range(len(smooth[0])):
            #If statements check for edge cases along border of matrix
            if j < len(smooth[0]) - 1:
                if i < len(smooth) - 1:
                    tempSum += smooth[i+1][j+1]*Kernal[2][2]
            if j > 0:
                if i > 0:
                    tempSum += smooth[i-1][j-1]*Kernal[0][0]
            if i < len(smooth) - 1:
                tempSum += smooth[i+1][j]*Kernal[2][1]
                if j > 0:
                    tempSum += smooth[i+1][j-1]*Kernal[2][0]
            if i > 0:
                tempSum += smooth[i-1][j]*Kernal[0][1]
                if j < len(smooth[0]) - 1:
                    tempSum += smooth[i-1][j+1]*Kernal[0][2]
            
            edgeA[i][j] = tempSum

            tempSum = 0
    
    return edgeA

#Function that returns the combined filter in partial x and partial y direction
def gradientFilter(x, y):
    gradientArray = np.zeros((len(x), len(x[0])))
    for i in range(len(x)):
        for j in range(len(x[0])):
            gradientArray[i][j] = math.sqrt((x[i][j]**2) + (y[i][j]**2))
    return gradientArray
    
#End Python high filter

#This method will be what's called on by main and head all other functions called
def getHighPassImage(smoothedArray):
    #Define x direction kernal for the partial derivative of x
    xKernal = np.array([[-1,0,1],
                        [-2,0,2],
                        [-1,0,1]])
    
    #Define y direction kernal for the partial derivative of y
    yKernal = np.array([[-1,-2,-1],
                        [0,0,0],
                        [1,2,1]])
    
    #Find partial x and partial y images
    edgeY = highFilterY(smoothedArray, yKernal)
    edgeX = highFilterX(smoothedArray, xKernal)
    
    #Gradient will be ultimate result of high pass edge enhancement. 
    gradient = gradientFilter(edgeX, edgeY)

    return gradient
'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''