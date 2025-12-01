# สรุปพื้นฐาน Python (Week 1)
## รันโค้ด
- รันไฟล์ Python ใน Windows terminal:
  - python filename.py
- ใน Jupyter: รันแต่ละ cell (`Shift + Enter`)
- VS Code: กดปุ่ม Run หรือใช้ Integrated Terminal

---

## พื้นฐานทั่วไป
- คอมเมนต์
  ```python
  # บรรทัดเดียว
  """
  บล็อกคอมเมนต์ / docstring
  """
  ```
- Indentation สำคัญ (ปกติ 4 ช่อง)

## แสดงผล / รับค่า
- print()
  ```python
  print("Hello, Python", 123)
  ```
- input() (คืนค่าเป็น str)
  ```python
  name = input("ชื่อ: ")
  age = int(input("อายุ: "))  # แปลงเป็น int
  ```

## ตัวแปรและชนิดข้อมูล
- ตัวอย่างชนิดพื้นฐาน: int, float, str, bool, None
  ```python
  x = 10          # int
  y = 3.14        # float
  s = "text"      # str
  b = True        # bool
  n = None        # ไม่มีค่า
  ```
- การแปลงชนิด
  ```python
  int("5"), float("3.2"), str(10), bool(0)
  ```

## ตัวดำเนินการ
- ทางคณิตศาสตร์: + - * / (ผลลัพธ์ float) // (หารปัดลง) % (เศษ) ** (ยกกำลัง)
  ```python
  7 // 2   # 3
  7 % 2    # 1
  2 ** 3   # 8
  ```
- เปรียบเทียบ: ==, !=, >, <, >=, <=
- ลอจิก: and, or, not

## เงื่อนไข
```python
if score >= 80:
    print("เกรด A")
elif score >= 70:
    print("เกรด B")
else:
    print("เกรด C")
```

## ลูป
- for ... in ... (บ่อยใช้กับ range / list)
  ```python
  for i in range(5):      # 0..4
      print(i)
  for item in ["a","b"]:
      print(item)
  ```
- while
  ```python
  i = 0
  while i < 5:
      print(i)
      i += 1
  ```

## โครงสร้างข้อมูลพื้นฐาน
- List
  ```python
  lst = [1,2,3]
  lst.append(4)
  lst.pop()
  lst[0], lst[1:3]   # ดัชนีและ slicing
  ```
- Tuple (ไม่เปลี่ยนค่า)
  ```python
  t = (1,2,3)
  ```
- Dictionary
  ```python
  d = {"name":"A", "age":20}
  d["age"] = 21
  d.get("addr", "ไม่ระบุ")
  ```
- Set
  ```python
  s = {1,2,3}
  s.add(4)
  ```

## ฟังก์ชัน
```python
def greet(name):
    return f"Hello, {name}"

print(greet("A"))
```

## การนำเข้าโมดูล
```python
import math
from random import randint
print(math.sqrt(9), randint(1,10))
```

## ข้อผิดพลาดและการจัดการ (เบื้องต้น)
```python
try:
    x = int(input("เลข: "))
except ValueError:
    print("กรอกตัวเลขเท่านั้น")
finally:
    print("จบการทำงาน")
```

## เคล็ดลับสั้น ๆ สิ่งที่มักใช้ใน Lab1
- ใช้ `type()` เพื่อตรวจชนิดตัวแปร
- แปลง `input()` ก่อนใช้ทางคณิตศาสตร์
- ระวังการจัด indentation ในบล็อก if/loop/def
---
