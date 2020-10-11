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
#Import other files containing functions that will be used in the main program
import PythonGray
import PythonSmoothing
import PythonEdgeEnhancement

#Imported to display image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('Purdue_Arch.png')    

#The following four lines of code go through each process by calling the specific method it invokes
gray = PythonGray.rgbG(img) 
smoothedArray = PythonSmoothing.smoothing(gray) 
edgeHigh = PythonEdgeEnhancement.getHighPassImage(smoothedArray)

plt.imshow(edgeHigh, cmap=plt.get_cmap('gray'), vmin=0, vmax=1)
'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''