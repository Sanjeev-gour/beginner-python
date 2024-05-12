f = open("C://files//book.txt","r")
s=f.read()
print(s)

import json 
book=json.loads(s)
print(book)


print(book['bob'])

print(book['bob']['phone'])

for name in book:
    print(book[name]['phone'])