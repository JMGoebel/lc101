def get_students():
    return input("Enter Student name (type 000 to exit): ")

def get_grade(stu):
    return input("Grade for " + stu + ": ")

def print_book():
    total = 0
    print("Class roster:")
    for (key, value) in students.items():
        total += int(value)
        print(key, "({})".format(float(value)))
    print()
    print("Average grade: {}".format(total/len(students)))

print("\n" * 2)

students = {}

# Get students
done = False
while not done:
    student = get_students()    
    if student == "000":
        done = True
    else:
        students[student] = 0
print()
# Get grades
for student in students:
    students[student] = get_grade(student)

print_book()
