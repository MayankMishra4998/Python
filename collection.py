# collection = single "variable" that holds multiple values
# List = [] ordered and changeable , allows duplicates OK
# Set = {} unordered and unchangeable , no duplicates , but Add / Remove items OK
# Tuple = () ordered and unchangeable , allows duplicates OK , FASTER

# List
fruits = ["Apple" , "Orange" , "Grapes" , "Banana" , "Apple"] # List
print(fruits)

print(len(fruits)) # it will print the number of items in the list
print("Apple" in fruits) # it will check if the item is in the list and return True or False
fruits.append("Mango") # it will add the item to the end of the list
fruits.remove("Grapes") # it will remove the item from the list
fruits.insert(1 , "Strawberry") # it will insert the item at the specified index{1} in the list
fruits.sort() # it will sort the items in the list in alphabetical order
fruits.reverse() # it will reverse the order of the items in the list

fruits.clear() # it will remove all the items from the list
#print(fruits.index("Apple")) # it will return the index of the first occurrence of the item in the list
#print(fruits.count("Apple")) # it will return the number of occurrences of the item in the list


# Set
numbers = {1 , 2 , 3 , 4 , 5 , 5}
print(numbers) # only one 5 will be printed because sets do not allow duplicates
print(len(numbers)) # it will print the number of items in the set
numbers.add(6) # it will add the item to the set
numbers.remove(3) # it will remove the item from the set
numbers.clear() # it will remove all the items from the set
#numbers.pop() # it will remove a random item from the set and return it

