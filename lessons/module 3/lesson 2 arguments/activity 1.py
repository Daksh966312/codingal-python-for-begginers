def total_bill(order_amounts, tip_perc):
    total = order_amounts + tip_perc/100*order_amounts
    return total

print( total_bill(225, 10))

    