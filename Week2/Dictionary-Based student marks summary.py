student_marks = {
    "Math": 85,
    "Statistics": 90,
    "Python": 88,
    "English": 76
}

def calculate_average(marks_dict):
    total = sum(marks_dict.values())
    average = total / len(marks_dict)
    return average
average_marks = calculate_average(student_marks)
print("Student marks:", student_marks)
print("Average marks:", average_marks)