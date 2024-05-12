f = open("c://files//stock2.csv","r")
f_out = open("c://files//output.csv","w")

f_out.write("Company name,PE ration,PB ration \n")
next(f)

for line in f:
        tokens = line.split(",")
        stock = tokens[0]
        price = float(tokens[1])
        eps = float(tokens[2])
        book = float(tokens[3])
        pe = round(price / eps, 2)
        pb = round(price / book, 2)
        f_out.write(f"{stock},{pe},{pb}\n")