# 9. List (ลิสต์)

> **List** คือโครงสร้างข้อมูลที่ใช้เก็บข้อมูลหลายรายการในตัวแปรเดียว เป็น **mutable** (แก้ไขได้) และเป็น sequence ที่เรียงลำดับ

## คุณสมบัติหลักของ List

1. **มีลำดับ (Ordered)**: สมาชิกมีตำแหน่ง index ที่แน่นอน
2. **แก้ไขได้ (Mutable)**: สามารถเพิ่ม ลบ แก้ไขสมาชิกได้หลังสร้าง
3. **ยอมรับค่าซ้ำ (Allows Duplicates)**: สามารถมีค่าซ้ำกันได้
4. **เก็บข้อมูลหลากหลายชนิด (Heterogeneous)**: เก็บข้อมูลต่างชนิดกันได้

## การสร้าง List

```python
# ใช้ square brackets []
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.14, True, [1, 2]]  # ข้อมูลหลายชนิด

# List ว่าง
empty = []
empty2 = list()

# ใช้ list() constructor
from_string = list("Python")        # ['P', 'y', 't', 'h', 'o', 'n'] => string
from_tuple = list((1, 2, 3))        # [1, 2, 3] => tuple
from_range = list(range(5))         # [0, 1, 2, 3, 4] => range

# List comprehension
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]
```

---

## การเข้าถึงและ Slicing

```python
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Indexing
print(fruits[0])      # 'apple'
print(fruits[-1])     # 'elderberry'
print(fruits[2])      # 'cherry'

# Slicing
print(fruits[1:3])    # ['banana', 'cherry']
print(fruits[:2])     # ['apple', 'banana']
print(fruits[2:])     # ['cherry', 'date', 'elderberry']
print(fruits[::2])    # ['apple', 'cherry', 'elderberry'] (ทุก 2 ตัว)
print(fruits[::-1])   # ลิสต์กลับด้าน

# การแก้ไขได้
fruits[1] = "blueberry"  # ✅ ['apple', 'blueberry', 'cherry', ...]
fruits[1:3] = ["kiwi"]   # ✅ แทนที่ 2 ตัวด้วย 1 ตัว
```

---

## List Methods (เมธอดสำคัญ)

### การเพิ่มข้อมูล
1. **append(value)** เพิ่มสมาชิก หม่ (หนึ่งตัว) เข้าไปที่ ท้ายสุดของ List เสมอ
2. **insert(index, value)** แทรกสมาชิกใหม่เข้าไปที่ตำแหน่งดัชนี (Index)ที่ระบุ
3. **extend(iterable)** ใช้สำหรับเพิ่มสมาชิกทั้งหมดจาก List อื่น เข้าไปต่อท้าย List ปัจจุบัน (เสมือนการเทรวมกัน)
```python
fruits = ["apple", "banana"]

# เพิ่มท้ายลิสต์
fruits.append("cherry")              # ['apple', 'banana', 'cherry']

# แทรกที่ตำแหน่งที่กำหนด
fruits.insert(1, "blueberry")        # ['apple', 'blueberry', 'banana', 'cherry']

# เพิ่มหลายรายการ (extend)
fruits.extend(["date", "elderberry"])  # ['apple', 'blueberry', 'banana', 'cherry', 'date', 'elderberry']
fruits += ["fig"]                    # เหมือน extend
```

### การลบข้อมูล
```python
fruits = ["apple", "banana", "cherry", "banana"]

# ลบตามค่า (ครั้งแรกที่เจอ)
fruits.remove("banana")              # ['apple', 'cherry', 'banana']

# ลบตาม index และคืนค่า
item = fruits.pop()                  # ลบตัวสุดท้าย, คืน 'banana'
item = fruits.pop(0)                 # ลบ index 0, คืน 'apple'

# ลบตาม index (ไม่คืนค่า)
del fruits[1]                        # ลบ index 1
del fruits[0:2]                      # ลบช่วง
del fruits                           # ลบ List                   

# ลบทั้งหมด
fruits.clear()                       # []
```

### การค้นหาและนับ
```python
numbers = [1, 2, 3, 2, 4, 2, 5]

# ค้นหา index
numbers.index(3)                     # 2 (index ที่พบครั้งแรก)
numbers.index(2, 2)                  # 3 (หา 2 จาก index 2 เป็นต้นไป)

# นับจำนวนครั้ง
numbers.count(2)                     # 3

# ตรวจสอบการมีอยู่
2 in numbers                         # True
10 not in numbers                    # True
```

### การจัดเรียงและกลับลำดับ

รูปแบบ: `var.sort(reverse=True/False)`
```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# เรียงลำดับ (แก้ไข list เดิม)
numbers.sort()                       # [1, 1, 2, 3, 4, 5, 6, 9]
numbers.sort(reverse=True)           # [9, 6, 5, 4, 3, 2, 1, 1]

# เรียงลำดับ (สร้าง list ใหม่)
sorted_nums = sorted(numbers)        # ไม่แก้ไข list เดิม

# กลับลำดับ
numbers.reverse()                    # กลับลำดับที่เดิม
reversed_list = numbers[::-1]        # สร้าง list ใหม่ (slice)

# เรียงตาม key
words = ["banana", "pie", "Washington", "book"]
words.sort(key=len)                  # เรียงตามความยาว
words.sort(key=str.lower)            # เรียงโดยไม่สนพิมพ์

# เรียงตัวเลขทศนิยม
floats = [3.14, 2.71, 1.41, 2.23]
floats.sort()                        # [1.41, 2.23, 2.71, 3.14]
```

### การคัดลอก
```python
original = [1, 2, 3]

# การอ้างอิงเดียวกัน (ไม่ใช่ copy)
ref = original
ref[0] = 99                          # original ก็เปลี่ยนด้วย!

# Shallow copy
copy1 = original.copy()              # ✅
copy2 = original[:]                  # ✅
copy3 = list(original)               # ✅

# Deep copy (สำหรับ nested list)
import copy
nested = [[1, 2], [3, 4]]
deep = copy.deepcopy(nested)         # คัดลอกทุกระดับ
```

---

## List Operations

```python
# การต่อลิสต์
[1, 2] + [3, 4]                      # [1, 2, 3, 4]
[1, 2] * 3                           # [1, 2, 1, 2, 1, 2]

# ความยาว
len([1, 2, 3])                       # 3

# Min/Max/Sum
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
min(numbers)                         # 1
max(numbers)                         # 9
sum(numbers)                         # 31

# การวนซ้ำ
for item in [1, 2, 3]:
    print(item)

# Enumerate (ได้ทั้ง index และ value)
for i, val in enumerate(['a', 'b', 'c']):
    print(f"{i}: {val}")

# List comprehension
[x**2 for x in range(5)]             # [0, 1, 4, 9, 16]
[x for x in range(10) if x % 2 == 0] # [0, 2, 4, 6, 8]
```

## ตัวอย่างการใช้งานจริง

```python
# หา unique values
numbers = [1, 2, 2, 3, 4, 4, 5]
unique = list(set(numbers))          # [1, 2, 3, 4, 5]

# Flatten nested list
nested = [[1, 2], [3, 4], [5, 6]]
flat = [item for sublist in nested for item in sublist]
# [1, 2, 3, 4, 5, 6]

# Filter ค่า
numbers = [1, 2, 3, 4, 5, 6]
evens = [x for x in numbers if x % 2 == 0]  # [2, 4, 6]
evens2 = list(filter(lambda x: x % 2 == 0, numbers))  # เหมือนกัน

# Map - แปลงค่าทุกตัว
squares = [x**2 for x in numbers]    # [1, 4, 9, 16, 25, 36]
squares2 = list(map(lambda x: x**2, numbers))  # เหมือนกัน

# Zip - รวม 2 list
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
combined = list(zip(names, ages))    # [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

# Unpacking
a, b, c = [1, 2, 3]                  # a=1, b=2, c=3
first, *rest = [1, 2, 3, 4]          # first=1, rest=[2,3,4]
```
---

## Common Mistakes (ข้อผิดพลาดทั่วไป)

### ❌ Mistake 1: append vs extend
```python
# ❌ ผิด - append เพิ่มทั้ง list เป็น element เดียว
my_list = [1, 2, 3]
my_list.append([4, 5])              # [1, 2, 3, [4, 5]]

# ✅ ถูก - extend รวมสมาชิกทั้งหมด
my_list = [1, 2, 3]
my_list.extend([4, 5])              # [1, 2, 3, 4, 5]
```

### ❌ Mistake 2: Reference vs Copy
```python
# ❌ ผิด - เปลี่ยน copy แล้ว original ก็เปลี่ยน
original = [1, 2, 3]
copy = original                      # อ้างอิงเดียวกัน!
copy[0] = 99                         # original[0] ก็เป็น 99

# ✅ ถูก - ใช้ copy()
copy = original.copy()
copy[0] = 99                         # original ไม่เปลี่ยน
```

### ❌ Mistake 3: Modifying list ขณะ loop
```python
# ❌ ผิด - อาจข้าม element
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num) # บางตัวข้ามไป

# ✅ ถูก - loop กับ copy หรือ list comprehension
numbers = [1, 2, 3, 4, 5]
for num in numbers[:]:  # loop กับ copy
    if num % 2 == 0:
        numbers.remove(num)

# หรือ
numbers = [x for x in numbers if x % 2 != 0]
```

### ❌ Mistake 4: append ใน nested loop
```python
# ❌ ช้า
result = []
for i in range(1000):
    result.append(i)                # ทำ 1000 ครั้ง

# ✅ เร็ว - list comprehension
result = [i for i in range(1000)]

# หรือ
result = list(range(1000))
```

---

## Best Practices (แนวทางปฏิบัติที่ดี)

✅ **ควรทำ:**
- ใช้ list comprehension แทน append loop เมื่อเป็นไปได้
- ใช้ `extend()` เมื่อต้องการเพิ่มหลาย element
- ใช้ `copy()` เมื่อต้องการสำเนา list
- ใช้ slicing `[::-1]` เพื่อกลับลำดับแบบสร้าง list ใหม่

```python
# ✅ ดี - comprehension
squares = [x**2 for x in range(1000)]

# ✅ ดี - extend แทน append
my_list.extend([4, 5, 6])

# ✅ ดี - explicit copy
copy = my_list.copy()
```

❌ **ไม่ควรทำ:**
- ไม่ใช้ `append()` กับ iterable (ใช้ `extend()` แทน)
- ไม่ลืม copy ก่อนแก้ไข (ถ้าต้องเก็บ original)
- ไม่ลบ element ขณะ loop

```python
# ❌ ไม่ดี - append list ส่วนหนึ่ง
my_list.append([4, 5])  # ส่วน [4,5] เป็น 1 element

# ❌ ไม่ดี - แก้ไข original โดยไม่ตั้งใจ
ref = original_list  # อ้างอิง ไม่ copy!
```