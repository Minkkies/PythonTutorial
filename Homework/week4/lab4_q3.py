def add_student(students):
    std_id = input('Enter Student ID: ')

    if std_id not in students:
        name = input('Enter Full Name: ')
        students[std_id] = name   # ⭐ ตรงนี้สำคัญ
        print('Student added successfully.')
    else:
        print('Student ID already exists!')

def view_student(students):
    std_id = input('Enter Student ID to view: ')

    if std_id in students:
        print(f'Student ID: {std_id}, Name: {students[std_id]}') #ดึง value (ชื่อ) จาก key
    else:
        print('Student not found!')
  
def update_student(students):
    std_id = input('Enter Student ID to update: ')

    if std_id in students:
        new_name = input('Enter New Full Name: ')
        students[std_id] = new_name  # อัปเดตชื่อใหม่
        print('Student data updated successfully.')
    else:
        print('Student not found!')

def delete_student(students):
    std_id = input('Enter Student ID to delete: ')

    if std_id in students:
        del students[std_id]  # ลบข้อมูลนักเรียนตาม Student ID
        print('Student deleted successfully.')
    else:
        print('Student not found!')

def view_all_students(students):
    if students:
        print('All Students:')
        for std_id, name in students.items():
            print(f'Student ID: {std_id}, Name: {name}')
    else:
        print('No students found!')

students = {} # สร้าง dictionary ว่างเพื่อเก็บข้อมูลนักเรียน เป็นตัวแปรgolobal
while True:
    print('\n----- Student Profile Managment -----')
    print('1. Add Student')
    print('2. View Student')
    print('3. Update Student')
    print('4. Delete  Student')
    print('5. View All  Student')
    print('6. Exit')
    print('-'*45)

    op = input('Please choose an option: ')

    if op == '1':
        add_student(students)
    elif op == '2':
        view_student(students)
    elif op == '3':
        update_student(students)
    elif op == '4':
        delete_student(students)
    elif op == '5':
        view_all_students(students)
    elif op == '6':
        print('Exiting program goodbye!')
        break
    else:
        print('Invalid option, please try again.')

# ตัวอย่างการทำงาน
# ----- Student Profile Managment -----
# 1. Add Student
# 2. View Student
# 3. Update Student
# 4. Delete  Student
# 5. View All  Student
# 6. Exit
# ---------------------------------------------
# Please choose an option: 1
# Enter Student ID: 6605001699
# Enter Full Name: Somchai
# Student added successfully.
# ----- Student Profile Managment -----
# 1. Add Student
# 2. View Student
# 3. Update Student
# 4. Delete  Student
# 5. View All  Student
# 6. Exit
# ---------------------------------------------
# Please choose an option: 1
# Enter Student ID: 6605001699
# Student ID already exists!