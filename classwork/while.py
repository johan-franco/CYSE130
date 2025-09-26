correct_password = "secret123"
attempt_count = 0
while True:
    password = input("Enter your password: ")
    attempt_count += 1
    if password == correct_password:
        print("Password correct!")
        break 
    print("Password incorrect. Please try again.")
    if attempt_count >= 3:
        print("Too many failed attempts. Access denied.")
        break
print("Exiting password check.")