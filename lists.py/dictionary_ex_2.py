import statistics
stock = {

  "info" : [600,630,620],
  "ril" : [1430,1490,1567],
  "mtl" : [234,180,160]
  }


def print_all():
    for stocks,s in stock.items():
        avg = statistics.mean(s)
        print(f"{stocks} ==> {s} ==> avg: ",round(avg,2))


def add_stock():
    s = input("Enter a stock ticker to add:")
    p = input("Enter price of this stock:")
    p=float(p)
    if s in stock:
        stock[s].append(p)
    else:
        stock[s] = [p]
    print_all()


def main():
    op=input("Enter operation (print, add or amend):")
    if op.lower() == 'print':
        print_all()
    elif op.lower() == 'add':
        add_stock()
    else:
        print("Unsupported operation:",op)


if __name__ == '__main__':
    main()
             