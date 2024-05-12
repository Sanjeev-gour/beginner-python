def calculate_total(exp):
    total=0
    for items in exp:
        total  = total + items
    return total    

def sum(a,b):
    print("a: ",a)
    print("b: ",b)
    total = a+b
    return total


tom_list=[234,567,433]
joe_list=[466,222,789]


toms_total = calculate_total(tom_list)  
joes_total = calculate_total(joe_list)
n=sum(4,6)

print("The sum of two numbers is: ",n)
print("Toms total is : ",toms_total)
print("Joes total is : ",joes_total)
