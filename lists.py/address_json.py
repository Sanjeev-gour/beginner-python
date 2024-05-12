book ={}

book["Tom"] ={

    "name": "Tom",
    "address": "1 red street NY",
    "phone": 9322344564
}

book["Joe"] ={

    "name": "Joe",
    "address": "1 green street NY",
    "phone": 7632344564
}

import json

s=json.dumps(book)

#writing in file
with open("c://files//data.txt","w") as f:
    f.write(s)

#reading a file

f = open("c://files//data.txt","r")
s=f.read()
print(s)

#this will convert string to dictionary
book = json.loads(s)
print(book)

print(type(book))



print(book["Tom"])

#how to access bob's phone number
print(book["Tom"] ["phone"])


#to print all of the content 

for person in book:
    print(book[person])
