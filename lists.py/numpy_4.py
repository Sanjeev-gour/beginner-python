#indexing and slicicng 

import numpy as np
'''
n = [6,7,8]
s=n[0:2]

print(s)

print(n[-1])

a= np.array([[3,4,5],[7,3,4],[5,3,6]])

print(a[1,2])#first row and second element

print(a[0:2])#first element and second element

print(a[0:2,2])#will print seocond elemet of each row 

print(a[-1])

#to print only first and secodn row and not print 0th row 
print(a[:,1:3])


a = np.arange(6).reshape(3,2)
b= np.arange(6,12).reshape(3,2)

print(a)

print(b)

c=np.vstack((a,b))
print(c) #it stacks both the matrix together vertically 

d=np.hstack((a,b))#it stacks both the matrix together horizontally
print(d)


e=np.arange(30).reshape(2,15)
print(e)

#now to split the array into three parts

f=np.hsplit(e,3)#this will split the above array into three parts horizontally
print(f) #this is not understandable 

#therefore 
print(f[0])#will print the zeroth split 
print(f[1])#will print the first split
print(f[2])#will print second split

#we can also do vertical split

g= np.split(e,2)#only be divided into two rows becuase e array has only two rows 

print(g[0])#will print the zeroth split 
print(g[1])#will print the first split

'''
p = np.arange(12).reshape(3,4)

print(p)

q= p>4

print(q) #this will give the answer in boolean form in array basically when elements of array p are greater than 3 it will give true otherwise false in array q

print(p[q])#will print the elements which give the value true

#we can also replace it by any number like 
p[q] = -1

print(p)