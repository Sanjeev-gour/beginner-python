#all about dictionary
"""
d ={"tom": 45 , "rob": 56 , "joe": 74}
print(d)

print(d["tom"])

#to add some more strings in dictionary

d["sam"]=32

print(d)

#how to delet 

del d["sam"]

print(d)

#to print every value in dictionary we use for loop 

for key in d:
    print("key: ",key,"value: ",d[key])

#another method to print the dicationary

for k,v in d.items():
    print("key:",key,"value:",v)

#to check the availability 

print("tom" in d)

print("sam" in d)

#to clear the content of dictionary 

d.clear()
print(d)
"""

#all about Tuples

point=(5,6,7,8)

print(point[0])

#tupples are immutable means you can't add or delet the content of tupple