
# Python Programming Problem Set #2

## **Premise**

Given  _n_  non-negative integers  _a1_,  _a2_, ...,  _an_, where each represents a point at coordinate (_i_,  _ai_).  _n_  vertical lines are drawn such that the two endpoints of line  _i_  is at (_i_,  _ai_) and (_i_, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and  _n_  is at least 2.
## **Example**
```
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
```

## ***Warning***
I made a program that evaluates your code by linter and pytest. So you need to follow some structure in coding.

 - Your program should be saved as ***solutions***
 - Create function call ***solution*** which returns the solution
 - When you want to run your program, run my test.py to check wether your code is going through well with my test cases.

*For example;*
```
L solutions.py
L test.py
```

 - test.py will be given to you for each problem set, so just copy and  
   paste the file in to your directory.  
 - solutions.py is the one that you need to create

Inside the solutions.py
```
def solution(x, y): #depends on the input you may change it
	'''
	Your code goes in here
	'''

	return (answer)

if __name__ == "__main__":
	'''
	Your own test case if you want to test it yourself
	'''
```   
How to run?
```
On your terminal or command prompt
----------------------------------
~# python test.py
```
Than it will prompt you with
```
========================== 4 passed in 0.03 seconds ===========================
```
If something similar pops up you are correct, else there is a problem with the codes or contact me or post an issue
