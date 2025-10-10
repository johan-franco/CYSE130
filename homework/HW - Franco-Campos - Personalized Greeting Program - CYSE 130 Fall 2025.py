# Previously i had it take in 3 parameters but if i want to force the user (through continuosly calling the function) to put in proper values before the program ends I don't need any
def personalized_greeting(): 
    print("Welcome user! Please fill in the information below.") # inital greeting (not personalized)

# ask for information and number to do age calculation
    name = input("\nEnter your name: ")
    age = input("Enter your age: ")
    num = input("Enter any number: ")

    
    #tries defining newage
    try:
        newage = str(int(age) + int(num)) # tries to add age and num to find age after num years
    except ValueError: #catches any value errors from trying to turn age and num into integers
        print("\nNumber was not entered for either age or number. Please try again user!\n\n") # tells user their error
        personalized_greeting() # call its own function again till user puts in ints for both age and num
    else:
        # if no value error finish the program through giving user personalized greeting
        print(f"\nHello {name}!")
        print(f"You are {age} years old.")
        print(f"You will be {newage} years old in {num} years.")

personalized_greeting()

# take in user's word
word = input("\nPlease enter any word: ")
# word[0] is first letter of user's word
print(f"\nFirst letter of your word: {word[0]}")
# word[-1] is last ketter of user's word. could have also put len(word) - 1
print(f"Last letter of your word: {word[-1]}")
#Finally we tell python to not exclude any parts of the word with :: but to skip every other letter
print(f"IEvery other letter: {word[::2]}")