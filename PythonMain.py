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
import PythonThresholding

#Imported to display image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


imgName = input('Enter the name of a color PNG image file ')

#Exception handling
try:
    img = mpimg.imread(imgName)   
    # If the file name is incorrect/not found, outputs an appropriate file handling error message
except FileNotFoundError:
    raise Exception("File name not found in directory, enter a proper file name")

#The following four lines of code go through each process by calling the specific method it invokes
gray = PythonGray.rgbG(img) 
smoothedArray = PythonSmoothing.smoothing(gray) 
edgeHigh = PythonEdgeEnhancement.getHighPassImage(smoothedArray)
finalImage = PythonThresholding.getTImage(edgeHigh)

plt.imshow(finalImage, cmap=plt.get_cmap('gray'), vmin=0, vmax=1)

#Output final image result to folder
plt.savefig('output.png')
'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''