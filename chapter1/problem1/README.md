# Python Programming Problem Set #1

## **Premise**

 - Given a 32-bit signed integer, reverse digits of an integer.
 - Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

## **Example**
```
Example 1:
Input: 123
Output:  321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21
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