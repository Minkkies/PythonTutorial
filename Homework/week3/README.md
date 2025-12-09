# Week 3 — สรุปและตัวอย่างโค้ด

โฟลเดอร์นี้เก็บแบบฝึกหัด (Jupyter Notebooks) ของสัปดาห์ที่ 3:
- Lab3_Q1.ipynb
- Lab3_Q2.ipynb
- Lab3_Q3.ipynb
- Lab3_Q4.ipynb

ไฟล์ตัวอย่างที่สร้าง: Lab3_Q1_example.py ... Lab3_Q4_example.py (โฟลเดอร์เดียวกัน)

---

## หัวข้อรวม (ภาพรวม)
- ประยุกต์ใช้ string manipulation (slicing, upper/lower, zip)
- ลูปและเงื่อนไขซ้อน (nested loop, while with flag)
- การจัดการรูปแบบข้อมูลและการตรวจสอบ
- คณิตศาสตร์เบื้องต้น (modulo, arithmetic operations)
- การใช้ comprehension กับ generator expression

---

- **เทคนิคหลัก:**
  ```python
  # ตรวจจับ exit
  if ans.lower() == "exit":
      break
  
  # เปรียบเทียบแบบไม่สนตัวพิมพ์
  if ans[i].upper() == std[i].upper():
      count += 1
  
  # ใช้ comprehension + zip
  count = sum(1 for a, s in zip(ans.upper(), std.upper()) if a == s)
  ```

## วิธีรันไฟล์ (Windows PowerShell / CMD)
- เปิดโฟลเดอร์ week3:
  ```
  cd d:\git\PythonTutorial\Homework\week3
  ```
- รัน notebook: เปิดใน VS Code หรือ Jupyter แล้วรันแต่ละ cell (Shift+Enter)
- รันสคริปต์ .py:
  ```
  python Lab3_Q1_example.py
  ```

---

## เทคนิคและเคล็ดลับที่ใช้บ่อย
- **String methods:** .upper(), .lower(), .strip()
- **Slicing:** id[:-1] (ตัด ตัวสุดท้าย)
- **zip():** เดินบนสองลิสต์พร้อมกัน
  ```python
  for a, s in zip(answers, student_answers):
      ...
  ```
- **Comprehension + generator:**
  ```python
  count = sum(1 for a, s in zip(ans.upper(), std.upper()) if a == s)
  ```
- **Loop control:** while True + break เมื่อเจอเงื่อนไข
- **Modulo & arithmetic:** % (mod), - (ลบ)

---

## ข้อแนะนำการทำแบบฝึกหัด
- อ่านโจทย์ให้ชัดเจน และเขียนขั้นตอนลงมาก่อน
- ทดสอบจากตัวอย่าง input/output ที่ให้มา
- สำหรับ Q3: ทดสอบกรณี exit, ความยาวไม่เท่า, ตัวพิมพ์เล็ก-ใหญ่
- สำหรับ Q4: ทดสอบด้วยตัวอย่างและใช้ calculator ตรวจสอบขั้นตอน
- ใช้ enumerate เมื่อต้องการ index ในลูป
- ใช้ zip เมื่อต้องเดินบนสองลิสต์พร้อมกัน

---

## ไฟล์ที่เกี่ยวข้อง
- BasicPython.md — บันทึกพื้นฐาน (string methods, comprehension, zip, enumerate)
- week2/README.md — เทคนิกจาก Week 2 (input parsing, loops, functions)
