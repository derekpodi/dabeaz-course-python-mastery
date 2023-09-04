#pcost.py  

def portfolio_cost(filename: str):
    total = 0.0

    with open('./'+ filename, 'r') as f:
        for line in f:
            fields = line.split()
            try:
                nshares = int(fields[1])
                price = float(fields[2])
                total = total + nshares * price
            except ValueError as e:
                print('Couldn''t Parse:', repr(line))
                print('Reason:', e)

    return total


print(portfolio_cost('Data/portfolio3.dat'))
