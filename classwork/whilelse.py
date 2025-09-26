count = 1
while count <= 3:
    print(count)
    if count == 2:
        print("Breaking out of the loop.")  
    break
    count += 1
else:
    print("Loop ended normally.")