python = ['KAWINWAT', 'KIDSAKORN', 'PHON', 'SUPANAT', 'SURACHAD', 'TEERAPON']
java = ['PAWARIS', 'PHON', 'PONGSAKORN', 'RATTANACHAT', 'SUPANAT', 'SURACHAD']
cpp = ['KAWINWAT', 'MATCHAKAN', 'RATTANACHAT', 'SUPANAT', 'SURACHAD', 'TEERAPON']

# set เพราะต้องการหาค่าที่ไม่ซ้ำกัน ในแต่ละภาษา
set_python = set(python)
set_java = set(java)
set_cpp = set(cpp)

print('='*50)
print('Analysis of Elective Programing course Registration')
print('='*50)

print('Registration Data for Each Course :')
print(f'Python   ({len(python)}  students) : ', python)
print(f'Java     ({len(java)}  students) : ', java)
print(f'C++      ({len(cpp)}  students) : ', cpp )

print('\n')
print('='*50)
print('Analysis Result :')
print('='*50)

# 1. นักเรียนที่ลงทะเบียนเรียนทุกหลักสูตร
all_courses = set_python & set_java & set_cpp
print(f"1. Enrolled in all 3 courses ({len(all_courses)}  student)")
print('Names :', list(all_courses))

#2. เฉพาะวิชา Python เพียงวิชาเดียว
only_python = list(set_python - (set_java | set_cpp))
print(f"\n2. Enrolled in only Python ({len(only_python)} student)")
print(f"Name: {only_python}")

#3. เฉพาะวิชา Java เพียงวิชาเดียว
only_java = list(set_java - (set_python | set_cpp))
print(f"\n3. Enrolled in only Java ({len(only_java)} student)")
print(f"Name: {only_java}")

#4. เฉพาะวิชา C++ เพียงวิชาเดียว
only_cpp = list(set_cpp - (set_python | set_java))
print(f"\n4. Enrolled in only C++ ({len(only_cpp)} student)")
print(f"Name: {only_cpp}")

#5. วิชา Python และ Java เท่านั้น (แต่ไม่ได้เรียน C++)
python_java = list((set_python & set_java) - set_cpp)
print(f"\n5. Enrolled in Python and Java only ({len(python_java)} student)")
print(f"Name: {python_java}")

#6. วิชา Python และ C++ เท่านั้น (แต่ไม่ได้เรียน Java)
python_cpp = list((set_python & set_cpp) - set_java)    
print(f"\n6. Enrolled in Python and C++ only ({len(python_cpp)} student)")
print(f"Name: {python_cpp}")

#7. วิชา Java และ C++ เท่านั้น (แต่ไม่ได้เรียน Python)
java_cpp = list((set_java & set_cpp) - set_python)
print(f"\n7. Enrolled in Java and C++ only ({len(java_cpp)} student)")
print(f"Name: {java_cpp}")

#8. อย่างน้อย 2 วิชาขึ้นไป
at_least_two = list((set_python & set_java) | (set_python & set_cpp) | (set_java & set_cpp))
print(f"\n8. Enrolled in at least 2 courses ({len(at_least_two)} student)")
print(f"Name: {at_least_two}")
