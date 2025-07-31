# Step 1: Create the student marks dictionary
student_marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Daisy": 88
}

# Step 2: Ask for student name
student_name = input("Enter the student's name: ")

# Step 3 & 4: Retrieve and display marks or show not found message
if student_name in student_marks:
    print(f"{student_name}'s marks are: {student_marks[student_name]}")
else:
    print(f"Sorry, no marks found for '{student_name}'.")
