import os
import math
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# หาคำตอบของสมการกำลังสอง (ใช้เครื่องหมาย -)
def quad1(a, b, c):
    return (-b + math.sqrt(b*b - 4*a*c)) / (2*a)

# หาคำตอบของสมการกำลังสอง (ใช้เครื่องหมาย +)
def quad2(a, b, c):
    return (-b - math.sqrt(b*b - 4*a*c)) / (2*a)


filename = input("Choose your problem file: ")

with open(filename, "r") as file:
    for line in file:
        a, b, c = map(float, line.split())

        # ตรวจสอบว่าเป็นปัญหาที่แก้ได้หรือไม่
        if a == 0 or b*b - 4*a*c < 0:
            print("Invalid problem")
        else:
            x1 = quad1(a, b, c)
            x2 = quad2(a, b, c)
            print(f"a, b, c = {line.strip()}")
            print(f"Roots: {x1}, {x2}")
            print('---')
