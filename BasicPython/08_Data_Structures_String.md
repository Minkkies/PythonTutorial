# 8. String (สตริง)

> **String** คือชนิดข้อมูลสายอักขระ (Sequence of Characters) ใน Python ใช้ชื่อย่อว่า `str` เป็นชนิดข้อมูลที่ใช้สำหรับจัดเก็บและจัดการข้อความ

## คุณสมบัติหลักของ String

1. **มีลำดับ (Ordered)**: อักขระแต่ละตัวมีตำแหน่ง (index) ที่แน่นอน
   - Index บวก: นับจากซ้ายไปขวา เริ่มที่ 0
   - Index ลบ: นับจากขวามาซ้าย เริ่มที่ -1
2. **ไม่สามารถแก้ไขได้ (Immutable)**: ไม่สามารถเปลี่ยนแปลงอักขระในตำแหน่งเดิมได้
3. **เป็นลำดับ (Sequence)**: สามารถวนซ้ำ (iterate) และใช้ slicing ได้

## การสร้าง String

```python
# ใช้ single quote ('') หรือ double quotes ("")
text1 = 'Hello'
text2 = "World"

# สตริงหลายบรรทัด - ใช้ triple quotes (''' หรือ """)
multiline = """This is
a multiline
string"""

# สตริงว่าง
empty = ""
empty2 = str()

# Escape characters
escaped = "Line1\nLine2\tTabbed"  # \n = newline, \t = tab
quote = 'It\'s a nice day'        # \' = single quote
path = "C:\\Users\\Name"          # \\ = backslash
# Raw strings (r prefix) - ไม่แปลง escape sequences
regex = r"C:\Users\Name"          # ✅ ใช้ได้กับ regex และ file paths
normal = "C:\\Users\\Name"        # ❌ ต้อง escape แต่ละ \
```

### Escape Sequences ที่สำคัญ
```python
print("Line1\nLine2")             # \n = newline (ขึ้นบรรทัดใหม่)
print("Col1\tCol2")               # \t = tab (ช่องว่างแนวนอน)
print("He said \"Hello\"")        # \" = double quote
print("It\'s okay")               # \' = single quote
print("Path: C:\\Users")          # \\ = backslash
print("\r")                        # \r = carriage return
print("Bell: \a")                 # \a = bell (เสียง beep)```
```

## การเข้าถึงอักขระ (Indexing & Slicing)
```python
s = "Python" # 0-5

# Indexing (เข้าถึงตัวอักษรตัวเดียว)
print(s[0])      # 'P' (ตัวแรก)
print(s[-1])     # 'n' (ตัวสุดท้าย)
print(s[2])      # 't'

# Slicing [start:stop:step]
print(s[0:3])    # 'Pyt' (index 0,1,2)
print(s[:3])     # 'Pyt' (ตั้งแต่ต้นถึง index 2)
print(s[3:])     # 'hon' (จาก index 3 ถึงท้าย)
print(s[::2])    # 'Pto' (ทุก ๆ 2 ตัว)
print(s[::-1])   # 'nohtyP' (กลับด้าน)

# Slicing edge cases
print(s[1:-1])   # 'ytho' (ยกเว้นตัวแรกและตัวสุดท้าย)
print(s[:-2])    # 'Pyth' (ทั้งหมดยกเว้น 2 ตัวสุดท้าย)
print(s[10:20])  # '' (empty, ไม่มี error ถึงแม้เกิน range)
print(s[2:20])   # 'thon' (ตัดไปถึงจุดสิ้นสุด)

# ไม่สามารถแก้ไขได้
# s[0] = 'J'     # ❌ TypeError: 'str' object does not support item assignment
```
**ข้อควรระวัง:**
- ถ้าเรียก Index เกินจำนวนที่มีจะเกิด Error (IndexError)
- ไม่สามารถใช้Index เพื่อแก้ไขค่าได้เช่น word[0] = 'J' จะ error
- Slicing ไม่มี error ถึงแม้เกิน range (จะคืน substring ที่เป็นไปได้)

---

## String Methods (เมธอดสำคัญ)

### การแปลงตัวพิมพ์
```python
s = "Hello World"

s.upper()        # 'HELLO WORLD' ตัวใหญ่ทั้งหมด
s.lower()        # 'hello world' ตัวเล็กทั้งหมด
s.capitalize()   # 'Hello world' (ตัวแรกพิมพ์ใหญ่)
s.title()        # 'Hello World' (แต่ละคำขึ้นต้นพิมพ์ใหญ่)
s.swapcase()     # 'hELLO wORLD' (สลับพิมพ์เล็ก-ใหญ่)
```

---

### การค้นหาและตรวจสอบ
```python
s = "Python Programming"

s.find('Pro')         # 7 (index ที่พบ, คืน -1 ถ้าไม่เจอ)
s.index('Pro')        # 7 (index ที่พบ, raise ValueError ถ้าไม่เจอ)
s.count('o')          # 2 (นับจำนวนครั้งที่พบ)
s.startswith('Py')    # True
s.endswith('ing')     # True

'Pro' in s            # True (ตรวจสอบว่ามี substring หรือไม่)
'Java' not in s       # True
```

---

### การตรวจสอบชนิดอักขระ
```python
'123'.isdigit()       # True (เป็นตัวเลขทั้งหมด)
'abc'.isalpha()       # True (เป็นตัวอักษรทั้งหมด)
'abc123'.isalnum()    # True (เป็นตัวอักษรหรือตัวเลข)
'hello'.islower()     # True (เป็นตัวพิมพ์เล็กทั้งหมด)
'HELLO'.isupper()     # True (เป็นตัวพิมพ์ใหญ่ทั้งหมด)
'   '.isspace()       # True (เป็นช่องว่างทั้งหมด)
```

---

### การตัดแต่งและทำความสะอาด
```python
s = "  hello world  "

s.strip()        # 'hello world' (ลบช่องว่างหน้า-หลัง)
s.lstrip()       # 'hello world  ' (ลบช่องว่างด้านซ้าย)
s.rstrip()       # '  hello world' (ลบช่องว่างด้านขวา)
s.strip('h')     # 'ello world' (ลบอักขระที่ระบุ)

'aabbccaa'.strip('a')  # 'bbcc'
```

---

### การแทนที่และแยก
```python
s = "Hello World"

# replace
s.replace('World', 'Python')   # 'Hello Python'
s.replace('l', 'L', 2)         # 'HeLLo World' (แทนที่ 2 ครั้งแรก)

# split() - แยกเป็น list
'a,b,c'.split(',')             # ['a', 'b', 'c']
'hello world'.split()          # ['hello', 'world'] (แยกด้วยช่องว่าง)
'a-b-c'.split('-', maxsplit=1) # ['a', 'b-c'] (แยกครั้งแรกเท่านั้น)

# join() - รวม list เป็น string
'-'.join(['a', 'b', 'c'])      # 'a-b-c'
' '.join(['Hello', 'World'])   # 'Hello World'
```

---

### การจัดรูปแบบ (Formatting)
```python
# f-strings (Python 3.6+) ⭐ แนะนำ
name = "Alice"
age = 25
print(f"My name is {name} and I'm {age} years old")
print(f"{name:>10}")      # '     Alice' (จัดขวา, กว้าง 10)
print(f"{age:05d}")       # '00025' (เติม 0 นำหน้า)
print(f"{3.14159:.2f}")   # '3.14' (ทศนิยม 2 ตำแหน่ง)

# format() method
"Hello, {}!".format("World")           # 'Hello, World!'
"{0} {1}".format("Hello", "Python")    # 'Hello Python'
"{name} is {age}".format(name="Bob", age=30)

# %-formatting (เก่า)
"Hello, %s!" % "World"                 # 'Hello, World!'
"%d + %d = %d" % (1, 2, 3)            # '1 + 2 = 3'
```

### การจัดเรียงและกรอก
```python
s = "Python"

s.center(10)       # '  Python  ' (จัดกลาง)
s.ljust(10)        # 'Python    ' (จัดซ้าย)
s.rjust(10)        # '    Python' (จัดขวา)
s.zfill(10)        # '0000Python' (เติม 0 นำหน้า)

# การจัดรูปแบบตัวเลข
num = 42
f"{num:05d}"       # '00042'
f"{num:>10}"       # '        42'
```

- :>10 → ชิดขวา กว้าง 10 ช่อง
- :<10 → ชิดซ้าย กว้าง 10 ช่อง
- :^10 → จัดกึ่งกลาง กว้าง 10 ช่อง
- :05d → เลขจำนวนเต็ม กว้าง 5 หลัก เติม 0 ด้านหน้า (d = decimal integer)

---

## String Operations (การดำเนินการ)

```python
# การต่อสตริง (Concatenation)
'Hello' + ' ' + 'World'    # 'Hello World'
'Hi' * 3                   # 'HiHiHi'

# การเปรียบเทียบ
'apple' == 'Apple'         # False (case-sensitive)
'apple' < 'banana'         # True (เปรียบเทียบตาม alphabetical order)

# ความยาว
len('Hello')               # 5
len('')                    # 0

# การวนซ้ำ
for char in "Python":
    print(char)            # P, y, t, h, o, n

# List comprehension กับ string
[c.upper() for c in "hello"]  # ['H', 'E', 'L', 'L', 'O']
```
---