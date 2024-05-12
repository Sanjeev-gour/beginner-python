book = {}

book['tom'] = {

'name': 'tom',
'address': 'new york',
'phone': 437843888

}

book['bob'] = {

'name': 'bob',
'address': 'Chicago',
'phone': 437844568

}


import json
s=json.dumps(book)
with open("C://files//book.txt","w") as f:
    f.write(s)