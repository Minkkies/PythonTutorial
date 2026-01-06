# 7. ฟังก์ชันและเทคนิคขั้นสูง (Advanced Functions & Techniques)

## Comprehensions 

> **Comprehension** คือวิธีเขียนลูปสร้าง collection แบบย่อ (กระชับ และมักอ่านง่าย)  
> - ใช้ได้กับ list, set, dict และ generator expression

> 1. พื้นฐาน: [ expression for item in iterable ] "ทำสิ่งนี้... กับทุกตัว... ในลิสต์นั้น"
> 2. มีเงื่อนไข: [ expression for item in iterable if condition ] "Expression จะทำงานก็ต่อเมื่อ Condition เป็น True เท่านั้น"
> 3. เงื่อนไขสองทาง:  [expression_if_true if condition else expression_if_false for item in iterable ]
> **Expression:** สิ่งที่ต้องการทำกับข้อมลู (เช่น คูณ 2)<br>
> **Item:** ชื่อตัวแปรที่จะรับค่าในแต่ละรอบ<br>
> **Iterable:** ข้อมูลต้นทาง (เช่น List, Range, Tuple )

  ตัวอย่าง:
  ```python
  # List comprehension
  # syntax
  [ expression for item in iterable if condition ]
  squares = [x*x for x in range(10)]            # [0,1,4,...,81]

  # มีเงื่อนไข
  evens = [x for x in range(20) if x % 2 == 0]  # [0,2,4,...,18]

  # Dict comprehension
  # syntax
  { key_expr: value_expr for item in iterable if condition }
  square_map = {x: x*x for x in range(5)}       # {0:0,1:1,2:4,3:9,4:16}

  # Set comprehension
  uniq = {len(s) for s in ["a","ab","abc","ab"]}# {1,2,3}

  # Generator expression (lazy evaluation)
  g = (x*x for x in range(10))
  for v in g:
      print(v)
  ```

  ข้อควรระวัง:
  - หลีกเลี่ยง comprehension ที่ซับซ้อนเกินไป (nested หลายชั้น) เพื่อความอ่านง่าย
  - หากต้องการ side-effects หรือขั้นตอนหลายบรรทัด ให้ใช้ฟังก์ชัน/ลูปปกติ

## Enumerate
> enumerate() คือฟังก์ชันที่คืนคู่ (index, value) เมื่อวนซ้ำบน iterable — สะดวกเมื่อต้องการทั้งดัชนีและค่า
  ตัวอย่าง:
  ```python
  fruits = ["apple", "banana", "cherry"]

  # แบบปกติ (index เริ่มที่ 0)
  enumerate(iterable, start=0)
  # คืน iterator ของ (index, value)
  
  for i, v in enumerate(fruits):
      print(i, v)
  # ผลลัพธ์:
  # 0 apple
  # 1 banana
  # 2 cherry

  # กำหนด start ให้ index เริ่มที่ 1
  for idx, val in enumerate(fruits, start=1):
      print(idx, val)
  # 1 apple, 2 banana, 3 cherry

  # รวมกับ zip
  a = [10,20,30]; b = ['x','y','z']
  for i, (n, ch) in enumerate(zip(a, b), start=1):
      print(i, n, ch)
  # → (1, (10,'x')), (2, (20,'y')), (3, (30,'z'))
  # 1 10 x , 2 20 y , 3 30 z
  # (n, ch) → unpack ค่าจาก tuple ที่ได้จาก zip
  ```

- ตัวอย่างรวม: สร้าง list ของ tuple (index, square) โดยใช้ enumerate + list comprehension
  ```python
  squares_with_index = [(i, x*x) for i, x in enumerate(range(5))]
  # [(0,0),(1,1),(2,4),(3,9),(4,16)]
  ```


# 8. Recursion (การเรียกซ้ำ)

## Recursion คืออะไร?
> **Recursion** คือเทคนิคที่ฟังก์ชันเรียกตัวเองเพื่อแก้ปัญหาที่สามารถแบ่งย่อยให้เหมือนกันได้  
> ทุกฟังก์ชัน recursive จะต้องมี **base case** (กรณีสิ้นสุด) เพื่อหยุดการเรียกซ้ำ มิฉะนั้นจะเกิด infinite recursion

## โครงสร้างพื้นฐาน
```python
def recursive_function(n):
    # Base case: เงื่อนไขสิ้นสุด (ต้องมีเสมอ)
    if n == 0:
        return 0
    
    # Recursive case: เรียกฟังก์ชันตัวเองกับพารามิเตอร์ที่เล็กลง
    else:
        return n + recursive_function(n - 1)
```

## ตัวอย่างพื้นฐาน

### ตัวอย่างที่ 1: แฟกทอเรียล (Factorial)
```python
# factorial(n) = n * (n-1) * (n-2) * ... * 1
# factorial(5) = 5 * 4 * 3 * 2 * 1 = 120

def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recursive case
    else:
        return n * factorial(n - 1)

print(factorial(5))  # 120
```

**วิธีทำงาน:**
```
factorial(5)
= 5 * factorial(4)
= 5 * (4 * factorial(3))
= 5 * (4 * (3 * factorial(2)))
= 5 * (4 * (3 * (2 * factorial(1))))
= 5 * (4 * (3 * (2 * 1)))
= 120
```

---