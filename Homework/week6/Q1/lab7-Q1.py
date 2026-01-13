import os

# คำสั่งนี้ เปลี่ยน working directory ไปที่โฟลเดอร์เดียวกับไฟล์โค้ด.py
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# รับชื่อไฟล์คำสั่ง
filename = input("Choose your movefile: ")

# รับตำแหน่งเริ่มต้น
x, y = map(int, input("Initial position : ").split(","))

valid = True   # ยังไม่เจอ error

# เปิดไฟล์และอ่านคำสั่ง
with open(filename, 'r') as file:
    for line in file:
        move = line.strip() #มันจะมีตัวขึ้นบรรทัดใหม่ (\n) ติดมาด้วยเลยต้องตัด

        if move == 'L':
            x -= 1
        elif move == 'R':
            x += 1
        elif move == 'U':
            y += 1
        elif move == 'D':
            y -= 1
        else:
            print("Invalid command")
            valid = False
            break

if valid:
    print(f"Robot stops at {x},{y}")

"""
ถ้ารันแล้วมันหาชื่อไฟล์ไม่เจอ ขึ้น FileNotFoundError

สาเหตุ: Python มองหาไฟล์ใน working directory ปัจจุบัน 
       ซึ่งอาจไม่ใช่โฟลเดอร์เดียวกับไฟล์ .py

วิธีแก้:
1. รัน Python ในโฟลเดอร์เดียวกับไฟล์
   Terminal: cd d:\git\PythonTutorial\Homework\week6\Q1
            python 6605001699lab7-Q1.py

2. เพิ่มโค้ดเปลี่ยน working directory (แนะนำ)
   import os
   os.chdir(os.path.dirname(os.path.abspath(__file__)))

3. ใส่ path เต็มของไฟล์
   script_dir = os.path.dirname(os.path.abspath(__file__))
   filepath = os.path.join(script_dir, filename)
   with open(filepath, 'r') as file:
"""