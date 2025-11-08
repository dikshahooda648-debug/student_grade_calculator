# Student Grade Calculator 🎓

def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"

print("🎓 Student Grade Calculator 🎓")
name = input("Enter student's name: ")
num_subjects = int(input("Enter number of subjects: "))

total_marks = 0

for i in range(num_subjects):
    marks = float(input(f"Enter marks for subject {i+1}: "))
    total_marks += marks

percentage = total_marks / num_subjects
grade = calculate_grade(percentage)

print("\n📊 RESULT 📊")
print(f"Name: {name}")
print(f"Total Marks: {total_marks}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
