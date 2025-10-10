def personalized_greeting(name, age, num):
    newage = str(int(age) + int(num))
    print(f"\nHello, {name}!")
    print(f"You are {age} years old.")
    print(f"You will be {newage} years old in {num} years.")


print("Welcome user! Please fill in the information below.")

name = input("\nEnter your name: ")
age = input("Enter your age: ")
num = input("Enter any number: ")

personalized_greeting(name, age, num)