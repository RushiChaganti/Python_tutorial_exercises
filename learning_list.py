# List is a collection of items and in a particular order.

# Declare a list 
cars_make = ["Suzuki", "Toyota", "Ferrari", "Honda", "Tesla"]

# Accessing list elements. List eleemnts start with index as 0
print(cars_make[0])

# Print third elemnt, index is 2
print(cars_make[2])

# Modify the elements in a list.
cars_make[1] = "Audi"
print(cars_make)
# Appending to the end of a list. 
cars_make.append("Ford")
print(cars_make)

# Insert elements at a posistion. 
cars_make.insert(1, "Lamborgiini")
print(cars_make)

# Remove elements from the list. using del, pop, remove
del cars_make[3]
print(cars_make)

# pop will also remove but can capture the removed value. 
removed_car = cars_make.pop(4)
print("Remvoed car is " + removed_car)
print(cars_make)

cars_make.remove("Honda")
print(cars_make)



