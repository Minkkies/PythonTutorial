# 2. ตัวแปรและชนิดข้อมูล (Variables & Data Types)
ตัวแปรคือชื่อที่ใช้เก็บข้อมูล (ค่าหรืออ้างอิงไปยังวัตถุ) ใน Python ตัวแปรผูกกับวัตถุและ Python เป็นภาษาแบบ dynamic typing — ไม่ต้องประกาศชนิดก่อน

## พื้นฐานทั่วไป
- คอมเมนต์
  ```python
  # บรรทัดเดียว
  """
  บล็อกคอมเมนต์ / docstring
  """
  ```
- Indentation สำคัญ (ปกติ 4 ช่อง)

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

## การตั้งชื่อ (Naming Rules & Conventions)
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

## ชนิดข้อมูลและการแปลงชนิด (Data Types & Casting)
ชนิดข้อมูลพื้นฐาน:
- **int**: จำนวนเต็ม (เช่น -5, 0, 100)
- **float**: จำนวนทศนิยม (เช่น 3.14, -0.5)
- **str**: ข้อความ (เช่น "Hello", 'Python')
- **bool**: ค่าความจริง (True หรือ False)
- **None**: ค่าว่าง/ไม่มีค่า
- **list, tuple, dict, set**: โครงสร้างข้อมูล

### ตัวอย่างการสร้างตัวแปร:
```python
# Numeric types
age = 25              # int
height = 1.75         # float
price = 99.99         # float

# String type
name = "Bob"          # ใช้ double quotes
message = 'Hello'     # ใช้ single quotes ก็ได้

# Boolean type
is_student = True
is_active = False

# None type
result = None

# Collection types
fruits = ["apple", "banana", "cherry"]      # list
coordinates = (10, 20)                      # tuple
person = {"name": "Alice", "age": 30}       # dict
unique_numbers = {1, 2, 3}                  # set
```

### การแปลงชนิดข้อมูล (Casting):
```python
# แปลงเป็น int
n = int("10")        # "10" → 10
n = int(3.99)        # 3.99 → 3 (ตัดทศนิยม)
n = int(True)        # True → 1

# แปลงเป็น float
f = float("3.14")    # "3.14" → 3.14
f = float(5)         # 5 → 5.0
f = float(False)     # False → 0.0

# แปลงเป็น str
s = str(123)         # 123 → "123"
s = str(3.14)        # 3.14 → "3.14"
s = str(True)        # True → "True"

# แปลงเป็น bool
b = bool(1)          # 1 → True
b = bool(0)          # 0 → False
b = bool("")         # "" → False
b = bool("text")     # "text" → True
```

## การตรวจสอบชนิดข้อมูล (Type Checking)
ใช้ฟังก์ชัน `type()` เพื่อตรวจสอบชนิดข้อมูล:
```python
x = 10
print(type(x))       # <class 'int'>

name = "Alice"
print(type(name))    # <class 'str'>

pi = 3.14
print(type(pi))      # <class 'float'>

# การใช้ isinstance() เพื่อตรวจสอบชนิด
if isinstance(x, int):
    print("x เป็นตัวเลขจำนวนเต็ม")

if isinstance(name, str):
    print("name เป็นข้อความ")
```

## ข้อสังเกตและเคล็ดลับ
1. **Dynamic Typing**: ตัวแปรสามารถเปลี่ยนชนิดได้หลังจากสร้าง
   ```python
   x = 10        # int
   x = "hello"   # str (ตัวแปรเดียวกันแต่เปลี่ยนชนิด)
   ```

2. **String Concatenation**: ห้ามรวม str กับชนิดอื่นโดยตรง
   ```python
   age = 25
   # ❌ print("Age: " + age)  # Error!
   # ✓ print("Age: " + str(age))
   # ✓ print(f"Age: {age}")   # f-string (ดีที่สุด)
   ```

3. **Mutable vs Immutable**: 
   - **Immutable** (ไม่เปลี่ยน): int, float, str, tuple
   - **Mutable** (เปลี่ยนได้): list, dict, set

