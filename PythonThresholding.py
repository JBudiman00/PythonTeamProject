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
#Input edge enhanced image, output thresholded image. This will be the final output.
import numpy as np

def getTImage(EImage):
    #Set finalArray to EImage size. The values in finalArray will be altered and finalArray will be what's outputted
    finalArray = np.zeros((len(EImage), len(EImage[0])))
    
    #Iterate through each pixel in image
    for i in range(len(EImage)):
        for j in range(len(EImage[0])):
            #Use threshold value to determine whether pixel is going to be white or black
            if EImage[i][j] < 0.5:
                finalArray[i][j] = 0
            else:
                finalArray[i][j] = 1
    
    return finalArray

'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''