## Intro
[Python คืออะไร / ภาษา Python ใช้ทำอะไรได้บ้าง / วิธีลงไพทอน](https://docs.mikelopster.dev/c/python-series/101/intro)

สามารถรัน Python ได้ 2 วิธี :
1. พิมใน Terminal => python (..ชื่อไฟล์..)
2. กด Run code ใน VSC Ctrl+Alt+N ก่อนกดโหลด Python ใน VSC ก่อน

# ตัวแปร (Variables) 
ตัวแปรคือชื่อที่ใช้เก็บข้อมูล (ค่าหรืออ้างอิงไปยังวัตถุ) ใน Python ตัวแปรผูกกับวัตถุและ Python เป็นภาษาแบบ dynamic typing — ไม่ต้องประกาศชนิดก่อน

## การกำหนดค่า (Assignment)
Syntax:
```python
ชื่อตัวแปร = ค่า
```
ตัวอย่าง:
```python
x = 10
name = "Alice"
pi = 3.14159
```

## การตั้งชื่อ (Naming rules & conventions)
- ชื่อเป็นตัวอักษร (a-z, A-Z), ตัวเลข (0-9) และ underscore (_)
- ห้ามขึ้นต้นด้วยตัวเลข (เช่น 1var ไม่ได้)
- หลีกเลี่ยงใช้คำสงวนของ Python (เช่น if, for, while)
- ตาม convention ใช้ lowercase_with_underscores สำหรับตัวแปร และ UPPER_SNAKE_CASE สำหรับค่าคงที่ (constant)

## การกำหนดหลายตัวพร้อมกัน / การสลับค่า
```python
a, b, c = 1, 2, 3
x = y = 0        # กำหนดค่าเดียวให้หลายตัว
a, b = b, a      # สลับค่าโดยไม่ต้องตัวแปรชั่วคราว
```

## ชนิดข้อมูลและการเปลี่ยนชนิด (Casting)
- พื้นฐาน: int, float, str, bool, None, list, tuple, dict, set
- แปลงชนิด:
```python
n = int("10")
f = float("3.14")
s = str(123)
b = bool(0)  # False
```

## ตรวจชนิด / ตรวจวัตถุ
```python
type(x)         # คืนชนิดของวัตถุ
isinstance(x, int)  # ตรวจว่า x เป็น int หรือไม่
id(x)           # คืนที่อยู่/เอกลักษณ์วัตถุ (ใช้ในการอธิบายการอ้างอิง)
```

## การอัปเดตค่า / นิพจน์แบบย่อ (Augmented assignment)
```python
x = 5
x += 3   # เทียบกับ x = x + 3
x *= 2
```

## ตัวแปรแบบคงที่ (Constants)
Python ไม่มีตัวแปรคงที่จริง ๆ แต่ใช้ convention:
```python
PI = 3.14159
MAX_RETRIES = 5
```

## การลบตัวแปร
```python
del x    # ลบการอ้างอิงตัวแปร x
```

## Scope: ขอบเขตของตัวแปร
- Local: ตัวแปรภายในฟังก์ชัน
- Global: ตัวแปรระดับโมดูล
- ใช้ `global` เพื่ออ้างอิงตัวแปร global ภายในฟังก์ชัน (ควรใช้อย่างระมัดระวัง)
```python
count = 0
def inc():
    global count
    count += 1
```

## Mutability (เปลี่ยนค่าได้) vs Immutability (เปลี่ยนค่าไม่ได้)
- Immutable: int, float, str, tuple
- Mutable: list, dict, set
ความแตกต่างสำคัญเมื่อส่งผ่านตัวแปรเป็นอาร์กิวเมนต์ให้ฟังก์ชัน (การแก้ไขวัตถุ mutable จะเห็นผลจากภายนอก)

## Type hints (คำแนะนำชนิดแบบไม่บังคับ)
```python
def greet(name: str) -> str:
    return "Hello " + name
```

## ตัวอย่างรวมสั้น ๆ
```python
# กำหนดและใช้งานตัวแปร
name = input("ชื่อ: ")
age = int(input("อายุ: "))
greeting = f"สวัสดี {name}, อายุ {age}"
print(greeting)

# List เป็น mutable
nums = [1,2,3]
nums.append(4)   # nums => [1,2,3,4]
```

## เคล็ดลับสั้น ๆ
- ใช้ `type()` และ `isinstance()` ตรวจชนิดขณะดีบัก
- แปลงชนิดของ input ก่อนนำไปคำนวณ (input คืน str)
- ตั้งชื่อตัวแปรให้สื่อความหมายเพื่อความชัดเจนของโค้ด

## ควบคุมการไหลของโปรแกรม (Control structures) — สรุปจาก: https://docs.mikelopster.dev/c/python-series/101/control-structure

ส่วนนี้ครอบคลุมวิธีควบคุมลำดับการทำงานของโปรแกรม เช่น เงื่อนไขและลูป พร้อม syntax และตัวอย่างสั้น ๆ

### เงื่อนไข (if / elif / else)
Syntax:
```python
if condition:
    # บล็อกเมื่อเงื่อนไขเป็นจริง
elif other_condition:
    # บล็อกเมื่อเงื่อนไขก่อนหน้าไม่เป็นจริงแต่เงื่อนไขนี้เป็นจริง
else:
    # บล็อกเมื่อไม่มีเงื่อนไขข้างต้นเป็นจริง
```
ตัวอย่าง:
```python
x = 10
if x > 0:
    print("บวก")
elif x == 0:
    print("ศูนย์")
else:
    print("ลบ")
```
Expression แบบย่อ (ternary):
```python
result = "บวก" if x > 0 else "ไม่บวก"
```

### ลูป for
- ใช้ iterate กับ iterable ใด ๆ (list, tuple, dict, string, range ฯลฯ)
- `range()` มักใช้สร้างลำดับตัวเลข

ตัวอย่าง:
```python
for i in range(5):      # 0..4
    print(i)

words = ["a", "b", "c"]
for w in words:
    print(w)
```
ประโยชน์ของ enumerate/zip:
```python
for idx, val in enumerate(words):    # ได้ดัชนีและค่า
    print(idx, val)

a = [1,2]; b = ['x','y']
for i, j in zip(a, b):
    print(i, j)
```
การวนกับ dictionary:
```python
d = {"a":1, "b":2}
for k in d:              # key
    print(k, d[k])
for k, v in d.items():    # key และ value
    print(k, v)
```

### ลูป while
Syntax:
```python
while condition:
    # ทำซ้ำจน condition เป็น False
    ...
```
ตัวอย่าง:
```python
i = 0
while i < 3:
    print(i)
    i += 1
```
ระวัง infinite loop หากเงื่อนไขไม่มีการเปลี่ยนแปลง

### break, continue, pass
- break: ออกจากลูปทันที
- continue: ข้ามรอบปัจจุบัน ไปทำรอบถัดไป
- pass: ไม่ทำอะไร (placeholder)

ตัวอย่าง:
```python
for i in range(10):
    if i == 5:
        break    # ออกลูป
    if i % 2 == 0:
        continue # ข้ามตัวเลขคู่
    pass         # ที่นี่ยังคงไม่ทำอะไร
```

### else กับลูป
ลูป (for/while) สามารถมี else ซึ่งจะรันเมื่อไม่มีการจบลูปด้วย break:
```python
for i in range(3):
    print(i)
else:
    print("จบโดยไม่มี break")
```

### Comprehensions (การย่อการสร้างลิสต์/เซ็ต/ดิกชันนารี)
- List comprehension:
```python
squares = [x*x for x in range(5)]
evens = [x for x in range(10) if x % 2 == 0]
```
- Dict/set comprehension:
```python
d = {x: x*x for x in range(5)}
s = {x for x in range(5)}
```
- Generator expression (ไม่สร้างรายการในหน่วยความจำทันที):
```python
g = (x*x for x in range(5))
```

### แนวทางปฏิบัติ
- เลือกใช้ for เมื่อรู้จำนวนรอบหรือ iterate บน iterable, ใช้ while เมื่อเงื่อนไขขึ้นกับสถานะที่เปลี่ยนแปลง
- ใช้ enumerate/zip แทนการจัดการดัชนีด้วยตัวเอง
- ใช้ comprehensions เพื่อโค้ดที่กระชับและอ่านง่าย แต่หลีกเลี่ยง comprehension ที่ซับซ้อนเกินไป

## การรับค่า (Input) 

- input() คือฟังก์ชันรับข้อมูลจากผู้ใช้ (stdin) และคืนค่าเป็น str เสมอ
  ```python
  name = input("ชื่อ: ")   # prompt แสดงก่อนรับค่า
  ```
- แปลงชนิดหลังรับค่าเมื่อต้องการคำนวณ
  ```python
  age = int(input("อายุ: "))
  price = float(input("ราคา: "))
  ```
- รับหลายค่าในบรรทัดเดียวด้วย split() และ map()
  ```python
  a, b = input("สองค่า: ").split()        # คืนรายการของ str
  x, y = map(int, input().split())        # แปลงเป็น int โดยตรง
  nums = list(map(int, input().split()))  # รายการของ int
  ```
- การจัดการช่องว่างและ newline
  - ใช้ strip()/rstrip()/lstrip() เพื่อลบช่องว่าง
  ```python
  s = input().strip()
  ```
- รับค่าจากหลายบรรทัด (เช่น ข้อมูล competitive programming)
  - วนรอบอ่าน input() หลายครั้ง หรือใช้ sys.stdin.readline() ที่เร็วกว่า
  ```python
  import sys
  line = sys.stdin.readline().strip()
  ```
- ตรวจจับข้อผิดพลาดการแปลงชนิด
  ```python
  try:
      n = int(input("เลข: "))
  except ValueError:
      print("กรุณากรอกตัวเลข")
  ```
- การใช้ unpacking กับ split() เมื่อจำนวนค่าคงที่:
  ```python
  a, b, c = input().split()
  ```
- เคล็ดลับ
  - input() คืน str เสมอ ต้องแปลงก่อนนำไปคำนวณ
  - สำหรับข้อมูลจำนวนมากหรือการรับเร็ว ใช้ sys.stdin.readline()
  - ใช้ map() กับ int/float เพื่อโค้ดกระชับและเร็วขึ้น
