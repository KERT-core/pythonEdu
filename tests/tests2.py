
#cretes list filled with incrementations from 0 to 10
b = [x for x in range(0,10)]
print(b)

#creating a list of n elements
print()
n = 7
c = []*n  #it is malloc in C
d = [0]*n #it creates a list of specified size filled with zeroes
print("empty list with allocated specified size "+str(c))
print(" "+str(d))

# overriden function
print()
def addition(a, b, c=0, d=0):
    return a+b+c+d

#getting 2 inputs at the same time from user
#if you know how many inputs you gonna get, you can do it easily
e, f = 3, 4
e, f = map(int, input().split()) #many inputs at the same time
#todo: how to make it work in pycharm (with the way pycharm input works)
print(str(e)+" "+str(f))

#adding lists, matrices
a = [1,2,3]
b = [4,5,6]
#next, commented line doesnt work
#d = map(add, a,b)
d = [sum(x) for x in zip(a,b)]
print(d)

#how to use lambda in python??
#next line doesnt work
#print(map(lambda x, x:x+y, a, b))

