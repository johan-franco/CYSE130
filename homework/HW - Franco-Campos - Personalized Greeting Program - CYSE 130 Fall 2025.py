# personalized greeting function that takes in 3 parameters
def personalized_greeting(name=0, age=0, num=0): # assumes that all are 0 if no input is entered by user
    try
    newage = str(int(age) + int(num))
    print(f"\nHello, {name}!")
    print(f"You are {age} years old.")
    print(f"You will be {newage} years old in {num} years.")


print("Welcome user! Please fill in the information below.")

name = input("\nEnter your name: ")
age = input("Enter your age: ")
num = input("Enter any number: ")

personalized_greeting(name, age, num)