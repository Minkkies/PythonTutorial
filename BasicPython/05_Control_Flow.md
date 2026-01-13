# 5. โครงสร้างควบคุม (Control Flow)

## เงื่อนไข (if / elif / else)
Syntax:
```python
if condition:
    # บล็อกเมื่อเงื่อนไขเป็นจริง
elif other_condition:
    # บล็อกเมื่อเงื่อนไขก่อนหน้าไม่เป็นจริงแต่เงื่อนไขนี้เป็นจริง
else:
    # บล็อกเมื่อไม่มีเงื่อนไขข้างต้นเป็นจริง
```

### ตัวอย่างพื้นฐาน
```python
x = 10
if x > 0:
    print("บวก")
elif x == 0:
    print("ศูนย์")
else:
    print("ลบ")

# ตัวอย่างจริง
age = int(input("อายุ: "))
if age < 13:
    print("เด็ก")
elif age < 18:
    print("วัยรุ่น")
elif age < 65:
    print("ผู้ใหญ่")
else:
    print("ผู้สูงอายุ")
```

### If ย่อ (One-liner)
```python
number = 5
if number > 0: print(number, '> 0')

# สำหรับเรียงนอก if/else ใช้ Conditional Expression ดีกว่า
```

### Conditional Expression (Ternary Operator)
Syntax: `true_value if condition else false_value`

```python
# แบบปกติ
grade = 40
if grade >= 50:
    result = 'pass'
else:
    result = 'fail'
print(result)

# แบบ Conditional Expression (ดีกว่า)
grade = 40
result = 'pass' if grade >= 50 else 'fail'
print(result)

# แบบซ้อนสำหรับหลายเงื่อนไข
score = 75
status = 'excellent' if score >= 90 else 'good' if score >= 80 else 'pass' if score >= 50 else 'fail'
print(status)
```

## ลูป for
ใช้วนซ้ำ (iterate) กับ iterable ใด ๆ (list, tuple, dict, string, range, set)

### range() - สร้างลำดับตัวเลข
Syntax: `range(start, stop, step)` (default: start=0, step=1)
- **stop**: บังคับต้องระบุ (เป็นขีดจำกัด ไม่รวมค่านี้)
- **start**: เริ่มต้น (ค่าเริ่มต้น 0)
- **step**: ขั้นบันได (ค่าเริ่มต้น 1)

```python
# 0 ถึง 4
for i in range(5):
    print(i)

# 2 ถึง 5
for i in range(2, 6):
    print(i)

# นับเพิ่ม 2 ทีละครั้ง
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8

# นับถอยหลัง
for i in range(5, 0, -1):
    print(i)  # 5, 4, 3, 2, 1
```

### วนซ้ำกับ list
```python
words = ["apple", "banana", "cherry"]
for word in words:
    print(word)

# เข้าถึงค่าและดัชนีพร้อมกัน
for idx, word in enumerate(words):
    print(f"{idx}: {word}")
```

### Nested loops
```python
# ตารางสูตรคูณ
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}", end="  ")
    print()  # ขึ้นบรรทัดใหม่

# ผลลัพธ์:
# 1 x 1 = 1  1 x 2 = 2  1 x 3 = 3
# 2 x 1 = 2  2 x 2 = 4  2 x 3 = 6
# 3 x 1 = 3  3 x 2 = 6  3 x 3 = 9
```

### zip() - วนรวมหลายรายการ
```python
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']

for num, letter in zip(numbers, letters):
    print(f"{num}: {letter}")

# 1: a
# 2: b
# 3: c
```

## ลูป while
ใช้วนซ้ำตราบใดที่เงื่อนไขเป็นจริง

Syntax:
```python
while condition:
    # ทำซ้ำจน condition เป็น False
    ...
```

### ตัวอย่างพื้นฐาน
```python
i = 0
while i < 3:
    print(i)
    i += 1

# Output: 0, 1, 2
```

### ตัวอย่างจริง
```python
# รับข้อมูลจนกว่าผู้ใช้กรอก 'quit'
while True:
    command = input("คำสั่ง (quit เพื่อออก): ")
    if command == "quit":
        break
    print(f"คำสั่งคือ: {command}")

# นับถอยหลัง
count = 5
while count > 0:
    print(count)
    count -= 1
print("หมดเวลา!")
```

### ระวัง Infinite Loop
```python
# ❌ เป็น infinite loop - เงื่อนไขไม่เปลี่ยน
# while True:
#     print("ติดลูป")

# ✅ เพิ่มเงื่อนไขเพื่อออกจากลูป
count = 0
while count < 5:
    print(count)
    count += 1
```

><span style="color:red;"><b>ข้อควรระวัง: </b></span>
>ถ้าไม่ได้ใช้ range หรือ enumerate
>ตัวแปรใน for จะเป็น “ค่าจริง” ที่อยู่ใน iterable ไม่ใช่ index

## คำสั่งควบคุมลูป (break, continue, pass)

### break
- ออกจากลูปทันที แม้ว่าจะยังวนลูปไม่ครบ
- ใช้เมื่อพบเงื่อนไขที่ต้องการหยุดลูปก่อนเวลา

```python
# หาตัวเลขแรกที่หารด้วย 7 ลงตัว
for i in range(1, 100):
    if i % 7 == 0:
        print(f"เจอแล้ว: {i}")
        break  # หยุดทันทีพอเจอ
```

### continue
- ข้ามรอบปัจจุบัน ไปทำรอบถัดไปทันที
- ใช้เมื่อต้องการข้ามบางเงื่อนไขโดยไม่ประมวลผลต่อ

```python
# พิมพ์เฉพาะเลขคี่
for i in range(10):
    if i % 2 == 0:
        continue  # ข้ามตัวเลขคู่
    print(i)  # จะพิมพ์เฉพาะเลขคี่
```

### pass (The pass Statement)
- คำสั่งที่ "ไม่ทำอะไรเลย" (null operation)
- ใช้เป็น placeholder เมื่อต้องการบล็อกโค้ดว่างๆ ที่ถูกต้องตาม syntax
- มีประโยชน์เมื่อเขียนโครงสร้างไว้ก่อน แล้วค่อยกลับมาเติมโค้ดทีหลัง

**กรณีการใช้งาน:**

1. **placeholder ในฟังก์ชันหรือคลาส**
```python
def future_function():
    pass  # เตรียมไว้ เดี๋ยวกลับมาเขียนทีหลัง

class EmptyClass:
    pass  # สร้างคลาสเปล่าไว้ก่อน
```

2. **ใช้ในเงื่อนไขที่ไม่ต้องการทำอะไร**
```python
x = 10
if x < 0:
    pass  # ถ้าติดลบไม่ต้องทำอะไร
elif x == 0:
    print("ศูนย์")
else:
    print("บวก")
```

3. **ใช้ในลูปเพื่อให้โครงสร้างสมบูรณ์**
```python
for i in range(10):
    if i == 5:
        break    # ออกลูป
    if i % 2 == 0:
        continue # ข้ามตัวเลขคู่
    pass         # ที่นี่ยังไม่ทำอะไร (จะเติมโค้ดทีหลัง)
```

4. **Exception handling แบบเงียบ**
```python
try:
    risky_operation()
except SomeError:
    pass  # เกิดข้อผิดพลาดก็ไม่ต้องทำอะไร ให้โปรแกรมทำงานต่อ
```

**ข้อแตกต่าง:**
- `pass` ≠ `None` → pass เป็นคำสั่ง (statement) ไม่คืนค่า, None เป็นค่า (value)
- `pass` ≠ `...` (Ellipsis) → แม้ใช้ได้คล้ายกัน แต่ `...` เป็นค่า literal ส่วน `pass` เป็นคำสั่ง

## else กับลูป (Loop else)
ลูป (for/while) สามารถมี `else` ซึ่งจะรันเมื่อลูปสิ้นสุดโดยปกติ **ไม่ใช่** เมื่อ break:

```python
# for loop กับ else
for i in range(3):
    print(i)
else:
    print("จบลูปโดยปกติ (ไม่มี break)")

# Output:
# 0
# 1
# 2
# จบลูปโดยปกติ (ไม่มี break)

# while loop กับ else
count = 0
while count < 3:
    print(count)
    count += 1
else:
    print("จบลูป while")

# Output:
# 0
# 1
# 2
# จบลูป while
```

### ตัวอย่าง: ค้นหาตัวเลขในรายการ
```python
# ค้นหา 10 ในรายการ
numbers = [1, 3, 5, 7, 9]
for num in numbers:
    if num == 10:
        print("เจอ 10")
        break
else:
    print("ไม่เจอ 10 ในรายการ")

# Output: ไม่เจอ 10 ในรายการ
```


## การวนรอบ Dictionary
```python
d = {"name": "Alice", "age": 25, "city": "Bangkok"}

# วนเฉพาะ key
for key in d:
    print(key)

# วนเฉพาะค่า
for value in d.values():
    print(value)

# วนทั้ง key และ value
for key, value in d.items():
    print(f"{key}: {value}")

# Output:
# name: Alice
# age: 25
# city: Bangkok
```

## List Comprehension (บัญชีพยานจัดอักษร)
วิธีกะทัดรัดในการสร้างรายการใหม่จากรายการเดิม

### ตัวอย่างพื้นฐาน
```python
# วิธีทั่วไป
squares = []
for i in range(5):
    squares.append(i ** 2)
print(squares)  # [0, 1, 4, 9, 16]

# List comprehension (ดีกว่า)
squares = [i ** 2 for i in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

# ด้วยเงื่อนไข
evens = [i for i in range(10) if i % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]

# ด้วยการแปลง
words = ["apple", "banana", "cherry"]
upper_words = [word.upper() for word in words]
print(upper_words)  # ['APPLE', 'BANANA', 'CHERRY']
```

### List comprehension ที่ซับซ้อนขึ้น
```python
# สร้างตาราง
matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print(matrix)
# [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

# กระจายรายการซ้อน
nested = [[1, 2], [3, 4], [5, 6]]
flat = [x for sublist in nested for x in sublist]
print(flat)  # [1, 2, 3, 4, 5, 6]
```
