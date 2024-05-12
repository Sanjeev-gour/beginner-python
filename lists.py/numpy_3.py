import numpy as np

'''a = np.array([5,6,7])
print(a.ndim)#to print the dimension of array
#two dimensional array 

b= np.array([[1,2],[4,5],[3,8]])
print(b.ndim)

print(b.itemsize)

print(a.dtype)

#want to change the data type 
'''

#b= np.array([[1,2],[4,5],[3,8]] )
'''
print(b.dtype)
print(b.itemsize)

print(b.size)

print(b.shape)

b= np.array([[1,2],[4,5],[3,8]] , dtype =complex)

print(b)


c =np.zeros((3,4))
print(c) #to inltialize the elements with 0


c =np.ones((3,4))
print(c) #to inltialize the elements with 1


d=np.arange(1,5)
print(d)#will print the numbers from 1 to 4

e= np.arange(1,5,2)
print(e)#this will print the number with added 2 like 1+2=3 2+3=5

f=np.linspace(1,5,10)
print(f) #will produce 10 numbers netween 1 to 5

g= b.reshape(2,3)
print(g)#to reshape the array 

h = b.ravel()
print(h)#used to flaten the array

print(b.min())
print(b.max())
print(b.sum())


print(b.sum(axis=0))#will print the sum column wise 

print(b.sum(axis=1))#will print the sum row wise 


print(np.sqrt(b))

'''

a = np.array([[1,2],[3,4]])

b=np.array([[5,6],[7,8]])

#we can find dot cross product sum diffrence mul etc



