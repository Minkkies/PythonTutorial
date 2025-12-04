## สรุปและจัดระเบียบข้อมูล (Week 2)


เป้าหมายของสัปดาห์ที่ 2
- ฝึกการรับค่า (input parsing) ทั้งแบบเดี่ยวและหลายค่า
- ควบคุมลำดับการทำงาน (if/elif/else, for, while)
- ใช้งานโครงสร้างข้อมูลพื้นฐาน (list, dict, set, tuple)
- เขียนฟังก์ชัน (def/return) และจัดการ scope
- ใช้ comprehensions, enumerate, zip เพื่อโค้ดที่กระชับ
- จัดการข้อผิดพลาดเบื้องต้น (try/except) และอ่านข้อมูลจำนวนมาก (sys.stdin)

สรุปสั้น ๆ ตามแต่ละ Lab
- Lab2_Q1 — รับชื่อจนกว่าจะเป็น "Lisa" (while + input)
- Lab2_Q2 — ตรวจและจัดการสตริง (string methods,เงื่อนไข)
- Lab2_Q3 — List operations (append, pop, slicing, loop)
- Lab2_Q4 — Dictionary operations (get, items, update, loop)
- Lab2_Q5 — ฟังก์ชันและการแยกหน้าที่ของโค้ด (def, return, scope)
- Lab2_Q6 — อ่านหลายบรรทัด / parse ด้วย map/split / ใช้ sys.stdin.readline() เมื่อข้อมูลเยอะ
- Lab2_Q7 — Comprehensions, enumerate, zip (เขียนโค้ดกระชับ)
- Lab2_Q8 — แบบฝึกผสม (รวมเทคนิคจากข้อก่อนหน้า)

วิธีรันไฟล์ (Windows PowerShell / CMD)
- เปิดโฟลเดอร์ week2:
  - cd d:\git\PythonTutorial\Homework\week2
- รัน notebook: เปิดใน VS Code หรือ Jupyter แล้วรันแต่ละ cell (Shift+Enter)
- รันสคริปต์ .py:
  - python Lab2_Q1_example.py

ตัวอย่างคำสั่งและเทคนิคที่ใช้บ่อย
- รับหลายค่าและแปลงชนิด:
  ```py
  a, b = map(int, input().split())
  ```
- รับค่าจากหลายบรรทัด (เร็วกว่า input):
  ```py
  import sys
  line = sys.stdin.readline().strip()
  ```
- ลูปจนกว่าจะตรงเงื่อนไข:
  ```py
  while True:
      s = input().strip()
      if s == "Lisa":
          break
  ```
- ใช้ enumerate/zip แทนการจัดการ index:
  ```py
  for i, v in enumerate(my_list):
      ...
  for x, y in zip(list1, list2):
      ...
  ```

