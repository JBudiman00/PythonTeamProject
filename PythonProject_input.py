"""
===============================================================================
ENGR 133 Fa 2020

Assignment Information
	Assignment:     Py Team Project
	Author:         Yolanda, chen3633@purdue.edu
	Team ID:        LC1-15 
	
Contributors:   Collin Gernhardt, cgernhar@purdue.edu
                Rachel Evrard, revrard@purdue.edu
                Jonathan Budiman, jbudiman@purdue.edu
               
	My contributor(s) helped me:	
	[ ] understand the assignment expectations without
		telling me how they will approach it.
	[ ] understand different ways to think about a solution
		without helping me plan my solution.
	[ ] think through the meaning of a specific error or
		bug present in my code without looking at my code.
	Note that if you helped somebody else with their code, you
	have to list that person as a contributor here as well.
===============================================================================

"""
import numpy as np
import matplotlib.pyplot as plt
image = plt.imread('Purdue_Arch.png')
import matplotlib.image as mpimg
#Read and Process image file
plt.imshow(image)




def rgbG(RGB):
    return np.dot(RGB[...,:3], [0.2126, 0.7152, 0.0722])

img = mpimg.imread('Purdue_Arch.png')     
gray = rgbG(img)    
plt.imshow(gray, cmap=plt.get_cmap('gray'), vmin=0, vmax=1)
plt.show()

    
    
    
'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''

