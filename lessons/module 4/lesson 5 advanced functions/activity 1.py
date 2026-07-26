items = ["pencil", "eraser", "pen", "notebook", "sharpener", "glue"]
stock_counts = [12, 0, 8, 3, 5, 9]

inventory = {item: count for item, count in zip(items, stock_counts)}
print("Full inventory: ",inventory)

in_stock_items = [m for m in items if inventory[m] > 0]
print(in_stock_items)

chosen_items = input("which item fo you want to buy? ")

if chosen_items not in inventory or inventory[chosen_items] == 0:
    print(chosen_items, "is out of stock! Stopping the checker.")
    exit()

prices = [10, 5, 40, 15, 20, 500]
markup = int(input("enter the markup amount to add to every price: "))

marked_up_prices = list(map(lambda p: p + markup, prices))
print(("marked up prices: ", marked_up_prices))

item_index = items.index(chosen_items)
chosen_price = marked_up_prices[item_index]
print("price of", chosen_items, "after markup: ", chosen_price)