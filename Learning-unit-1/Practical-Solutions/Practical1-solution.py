student_name = input("Enter the student name: ")
student_number = input("Enter the student number: ")
test_mark = float(input("Enter the test mark: "))
assignment_mark = float(input("Enter the assignment mark: "))

average = (test_mark + assignment_mark) / 2
passed = average >= 50

print("\nStudent Registration Summary")
print("Name:", student_name)
print("Student number:", student_number)
print("Average:", average)
print("Passed:", passed)