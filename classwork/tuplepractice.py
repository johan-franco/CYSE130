coordinates = (10.0, 20.0)
#tuples are immutable
# coordinates[0] = 15.0 will raise an error
# Access tuple items
print(f"X coordinate: {coordinates[0]}")
print(f"Y coordinate: {coordinates[1]}")
print(f"Coordinates Tuple: {coordinates}")
# Unpacking the tuple
x, y = coordinates
print(f"Unpacked X: {x}, Y: {y}")
