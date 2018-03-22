

# Python Programming Problem Set #5

## **Premise**
Since we are part of information security club. We will be touching bit of security perspective.

According to the techtarget, the MD5 hashing algorithm is one-way cryptographic function that accepts a message of any length as input and returns as output a fixed-length digest value to be used for authenticating the original message.

Even though this algorithm is designed for cryptographic message authentication code but, it is widely used on the internet.

So, I'm asking you to build MD5 encrypter using python. [Visit this site](https://docs.python.org/3/library/hashlib.html) to learn about module that you have to use

However, in this question please use
sha224 algorithm when you are solving. Search for Hashlib


## **Example**
```
Input: therearenoone
Output: 506ed6d3b8430711e84d1089ff8afb8a14df9e99d66f880311edf46b

Input: baegopa
Output: f5d84bf91d724b39e3af68a2715b7c162684aada3728aa404220c911
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
LrestGetLib.py
```

 - test.py will be given to you for each problem set, so just copy and  
   paste the file in to your directory.  
 - solutions.py is the one that you need to create
 - restGetLib.py will be given to you for some problems like this which requires online authentication

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
