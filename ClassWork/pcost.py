import sys

def portfolio_cost(file):
    total = 0
    with open(file, 'r') as f:
        for line in f:
            data = line.split()
            try:
                total += int(data[1]) * float(data[2])
            except ValueError:
                print("Couldn't parse", line)
            # print(int(data[1]))
    f.close()
    return total

if __name__ == '__main__':
    print(portfolio_cost('../Data/portfolio.dat'))


