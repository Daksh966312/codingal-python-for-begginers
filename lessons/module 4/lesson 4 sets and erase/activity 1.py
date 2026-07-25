fruit_basket1 = {"mango", "banana", "mango"}
fruit_basket2 = {"apple", "oranges", "grapes", "mango"}

print("fruits are:", fruit_basket2, fruit_basket1)

fruit = input("whats you favpurite fruit (other than mango): ")
if len(fruit) == 0:
    print("ENTER A VALID FRUIT")
    exit()
fruit_basket1.add(fruit)
print("added!", fruit_basket1)

common = fruit_basket1.intersection(fruit_basket2)
print(common)
import array as arr
fruit_counts = arr.array("i", [3,5,2,4])
print(fruit_counts)
fruit_counts.insert(0,9)
fruit_counts.append(9)
print(fruit_counts)

count_of_9 = fruit_counts.count(9)
print(count_of_9)

fruit_counts.reverse()
print(fruit_counts)