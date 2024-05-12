import numpy as np

'''
a = np.arange(12).reshape(3,4)

print(a)

for cell in a.flatten():
    print(cell) #will flatten all the cell 


#we can achive this faltten by nditer function 
for x in np.nditer(a,order='C'):  #this will print in c order which is same as above 
    print(x) 


for y in np.nditer(a,order='F'):  #this will print in forten order which is same as above 
    print(y) 


#instead of going element by element if you want to print the enite column use need to use flag as external_loop function

for z in np.nditer(a,order="F",flags=['external_loop']):
    print(z)



#if want to print the square of every element 

for t in np.nditer(a,op_flags=['readwrite']):
    t[...] = t*t
    print(a)
'''

#when we have to iterate through 2 arrays at the same time 

a= np.arange(12).reshape(3,4)
b= np.arange(3,15,4).reshape(3,1)

for x,y in np.nditer([a,b]):
    print(x,y)

    #but here they should be equal or one of them should be one 
