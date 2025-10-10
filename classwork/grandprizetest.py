count = 0
value = 1
while (value < 100):
    if value % 7 == 0:
        value += 15
    elif value % 3 == 0:
        value *= 2
    else:
        value += 1
    count += 1

print(count)
