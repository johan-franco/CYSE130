#prints all numbers except 5 from 1 to 10
number = 1
while number <= 10:
    if number == 5:
        number += 1 # Increment before continue to avoid infinite loop
        continue # Skip the rest of the loop when number is 5
    print(number)
    number += 1