# Function to find the tallest student
def find_tallest_student(students):
    # Find the student with the maximum height
    tallest_student = max(students, key=students.get)
    return tallest_student

# Dictionary to store student names and their heights
students = {
    "John": 170,
    "Alice": 172,
    "Bob": 150
}

# Get the tallest student
tallest_student = find_tallest_student(students)

# Print the heights of all students
for student, height in students.items():
    print(f"{student}: {height} cm")

# Print the tallest student
print(f"\n{tallest_student} is the tallest")
