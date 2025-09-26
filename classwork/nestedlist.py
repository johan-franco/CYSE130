classes = {
"Class 1": ["Student A", "Student B", "Student C"],
"Class 2": ["Student D", "Student E", "Student F"],
"Class 3": ["Student G", "Student H", "Student I"]
}
for class_name, students in classes.items():
    print(f"Checking homework for {class_name}:")
    for student in students:
        print(f"Grading homework for {student}...")
    print("") # Adds a newline for better readability between class