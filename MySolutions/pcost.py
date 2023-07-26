# pcost.py

import sys

def portfolio_cost(path):
    with open(path, 'r') as f:
        data = f.readlines()
    total = 0
    for line in data:
        _, num, price = line.split()
        try:
            num = int(num)
        except ValueError as e:
            print('Failed: Reason', e)
            continue
        try:
            price = float(price)
        except ValueError as e:
            print('Failed: Reason', e)
            continue
        total += num * price
    return total

if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit("Usage: pcost.py 'Path to file'")
    print(portfolio_cost(sys.argv[1]))