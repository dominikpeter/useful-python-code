
def get_index(d, m):
    s = list(d.keys())
    s.sort(reverse=True)
    for i, j in enumerate(s):
        if j > m:
            s.pop(i)
    return s


def calc_price_rec(d, quantity, index):
    stack = index[0]
    if stack > quantity:
        index.pop(0)
        return calc_price_rec(d, quantity, index)
    if quantity % stack == 0:
        return quantity * d[stack]
    else:
        intDivision = int(quantity / stack)
        price = intDivision * d[stack] * stack
        remainder = quantity % stack
        index.pop(0)
        return price + calc_price_rec(d, remainder, index)


def calc_price(d, quantity):
    index = get_index(d, quantity)
    price = calc_price_rec(d, quantity, index)
    return price

def get_best(d, fromRange, toRange):
    bestPrice = np.inf
    bestQuantity = np.inf
    bestPricePerPiece = np.inf

    for i in range(fromRange,toRange):
        price = calc_price(d, i)
        if price/i < bestPricePerPiece:
            bestPrice = price
            bestQuantity = i
            bestPricePerPiece = price/i
    return bestPrice, bestQuantity


if __name__ == '__main__':

    m = 6

    d = {1:20,
         5:15,
         100:10,
         200:8,
         300:5}

    print("Total Price is {}".format(
        calc_price(d, m)))

    p, q = get_best(d, 950, 1300)

    print("Best price per piece = {} with {} quantity".format(p, q))
    
