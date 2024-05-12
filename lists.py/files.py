#creating a file
#wriring and appending a file
#f = open("C:\\files\\funny.txt","a")
#f.write("\n Hi I am funny")
#f.close()

#reading a file
#f = open("C:\\files\\funny.txt","r")
#print(f.read())
#f.close()

#in loop
'''
f = open("C:\\files\\funny.txt","r")

for line in f:
    tokens = line.split(' ')
    #to get the word count
    print(len(tokens))

'''
f = open("C:\\files\\funny.txt","r")
f_out = open("C:\\files\\funny_wc.txt","w")

for line in f:
    tokens = line.split(' ')
    f_out.write("wordcount:" +str(len(tokens))   +line)


f.close()
f_out.close()