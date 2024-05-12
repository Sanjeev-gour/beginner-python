print("Hello world")

items = ["bread","veggies", "pasta","fruits"]
print(items)

print(items[0])

#updated the list 
items[0]="Chips"

print(items)
print(items[0])

print(items[0:2])
#remember here the second index i.e 2 will be excluded only 0th and 1st index wil be printed 

print([items[-1]])
#here index will start from end

items = ["bread","veggies", "pasta","fruits"]

items.append("Butter")#this append wil add the butter to the initial list
print(items)

items = ["bread","veggies", "pasta","fruits"]
items.insert(1,"butter")#this function will add butter to the 1st index
print(items)


#joining two list
food =["butter","pasta","bread"]
bath=["soap","detergent"]
items=food+bath
print(items)

print(len(items))

#to check true or false

print("bread" in items)
print("chips" in items)
