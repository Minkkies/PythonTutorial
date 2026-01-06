# Week 4 — สรุปและตัวอย่างโค้ด

โฟลเดอร์นี้เก็บแบบฝึกหัด (Python scripts) ของสัปดาห์ที่ 4:
- lab4_q1.py
- lab4_q2.py
- lab4_q3.py
- lab4_q4.py
- lab4-2.py

ไฟล์งาน (Assignment):
- Assignment Week 04-1.pdf
- Assignment Week 04-2.pdf

---

## หัวข้อรวม (ภาพรวม)
- ประยุกต์ใช้ฟังก์ชัน (functions) ที่กำหนดเองและฟังก์ชันในตัว (built-in)
- จัดการรูปแบบข้อมูลที่ซับซ้อน (nested data structures)
- การจัดการไฟล์ (file I/O) อ่านและเขียนข้อมูล
- การใช้ modules และ libraries ต่างๆ
- การแก้ปัญหาที่ต้องหลายขั้นตอน

---

## เทคนิคหลัก
```python
# ประกาศฟังก์ชัน
def my_function(param1, param2):
    result = param1 + param2
    return result

# อ่านไฟล์
with open('file.txt', 'r') as f:
    data = f.read()

# เขียนไฟล์
with open('output.txt', 'w') as f:
    f.write("Hello, World!")

# ใช้ modules
import math
print(math.sqrt(16))
```

## วิธีรันไฟล์ (Windows PowerShell / CMD)
- เปิดโฟลเดอร์ week4:
  ```
  cd d:\git\PythonTutorial\Homework\week4
  ```
- รันสคริปต์ .py:
  ```
  python lab4_q1.py
  ```

---

## เทคนิคและเคล็ดลับที่ใช้บ่อย
- **สร้างและเรียกใช้ฟังก์ชัน:** def, return, function parameters
- **การจัดการไฟล์:** open(), read(), write(), with statement
- **การใช้ built-in functions:** len(), range(), enumerate(), zip()
- **การแก้จุดบกพร่อง:** print debugging, try/except
