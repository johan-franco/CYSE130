fruits = ["apple", "banana", "cherry", "other", "new"]
print(fruits[0])  #first item
print(fruits[::2])  #step  
fruits[1] = "blueberry"  #modify second item
fruits.append("orange")  #add item to end
fruits.append("kiwi")
print(fruits)
print(fruits[1:3]) #slice list will stop at orange if we want to include orange we need to do 1:4, 

