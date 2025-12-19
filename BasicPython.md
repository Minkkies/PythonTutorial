# Intro
[Python คืออะไร / ภาษา Python ใช้ทำอะไรได้บ้าง / วิธีลงไพทอน](https://docs.mikelopster.dev/c/python-series/101/intro)

watch: [Basic Python](https://www.youtube.com/watch?v=ESNFhgRqeow&list=PLwZ0y9k-cYXALFTl5X2A3IPNTyK-9vm-v&index=6)

สามารถรัน Python ได้ 2 วิธี :
1. พิมใน Terminal => python (..ชื่อไฟล์..)
2. กด Run code ใน VSC Ctrl+Alt+N ก่อนกดโหลด Python ใน VSC ก่อน

# ตัวแปร (Variables) 
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

### รวม function
- input
    - .split(",") ถ้าไม่ใส่ parameter มันจะ split จากช่องว่าง 

- output
    - print(f'{variable}, {variable}')
    - print("hello", "world!", sep=" + ", end='') 

        sep=" + " -> ขั้นกลางด้วยอะไร

        end='' -> ต่อท้ายอยากให้ทำไร กรณี end='' -> ไม่ขึ้นบรรทัดใหม่


**code:**
```py
a, b, c = int(input('Enter coefficients a, b, c : ').split(",")) #แบบใช้ .split(",")
print(a , b, c, sep=", ")

name = input('Enter your name: ') #แบบ Basic
print(f"name is: {name}")
print("hello", "world!", sep=" + ", end='')
```

**output:**
```py
Enter coefficients a, b, c : 1,2,3
a: 1, b: 2, c: 3
hello + world!
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

if ย่อ
```py
number = 5
if number > 0: print(number, '> 0')
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

## ลูป for
- ใช้ iterate กับ iterable ใด ๆ (list, tuple, dict, string, range ฯลฯ)
- `range(start,step,stop)` มักใช้สร้างลำดับตัวเลข
- default start = 0 & step = 1 ต้องกำหนด stop ถ้ามีการกำหนดค่ามาจะเป็น Stop โดยทันที

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

## ลูป while
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

## break, continue, pass
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

## else กับลูป
ลูป (for/while) สามารถมี else ซึ่งจะรันเมื่อไม่มีการจบลูปด้วย break:
```python
for i in range(3):
    print(i)
else:
    print("จบโดยไม่มี break")
```

## Comprehensions และ enumerate 

- Comprehension คือวิธีเขียนลูปสร้าง collection แบบย่อ (กระชับ และมักอ่านง่าย)  
  - ใช้ได้กับ list, set, dict และ generator expression

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

- enumerate() คือฟังก์ชันที่คืนคู่ (index, value) เมื่อวนซ้ำบน iterable — สะดวกเมื่อต้องการทั้งดัชนีและค่า
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
  ```

- ตัวอย่างรวม: สร้าง list ของ tuple (index, square) โดยใช้ enumerate + list comprehension
  ```python
  squares_with_index = [(i, x*x) for i, x in enumerate(range(5))]
  # [(0,0),(1,1),(2,4),(3,9),(4,16)]
  ```

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
   - ```.strip()```: ใช้ลบ Whitespace (ช่องว่าง, tab,newline) ที่ส่วนหัวและท้ายของสตริง
 - ```.replace(old, new)``` แทนที่ old substring ด้วย new substring
 - ```.find(text)``` คืน index ของคำที่พบ


## Tuple

> **Tuple** คือโครงสร้างข้อมูลประเภทหนึ่งในภาษา Python ที่ใช้เก็บข้อมูลหลายรายการไว้ในตัวแปรเดียว Tuple มีลักษณะคล้ายกับ List      
>แต่มีความแตกต่างที่สำคัญคือ
**Tuple ไม่สามารถแก้ไขได้** (**immutable**)
เมื่อสร้างขึ้นแล้ว

## คุณสมบัติหลักของ Tuple

1.  **มีลำดับ (Ordered)**: สมาชิกใน Tuple จะถูกจัดเก็บตามลำดับที่เรากำหนด และสามารถเข้าถึงได้ผ่านดัชนี (index)
2.   **ไม่สามารถเปลี่ยนแปลงได้ (Immutable)**: นี่คือความแตกต่างที่สำคัญที่สุด เมื่อ Tuple ถูกสร้างขึ้น เราไม่สามารถเพิ่ม ลบ หรือแก้ไขสมาชิกภายในได้
3. **ยอมรับค่าซ้ำ (Allows Duplicates)**: สามารถมีสมาชิกที่มีค่าซ้ำกันได้
4. **เก็บข้อมูลได้หลากหลายชนิด (Heterogeneous)**: สามารถเก็บข้อมูลต่างชนิดกันได้ เช่น ตัวเลข, ข้อความ, หรือ List

## การสร้าง Tuple

**การสร้าง Tuple โดยใช้วงเล็บ ()**
> สามารถสร้าง Tuple ได้โดยการนำสมาชิกมาใส่ไว้ในวงเล็บ () และคั่นด้วยเครื่องหมายจุลภาค , (comma)

\`\`\`python
### ตัวอย่างการสร้าง Tuple
my_tuple = ("apple", "banana", "cherry", 123)

### การสร้าง Tuple ที่มีสมาชิกเพียงตัวเดียว ต้องมีเครื่องหมายจุลภาคต่อท้าย
single_tuple = ("hello",)
print(type(single_tuple))
\`\`\`

**การสร้าง Tuple โดยใช้ \`tuple()\` constructor**

**\`tuple()\`** constructor เป็นฟังก์ชันที่ใช้สร้าง Tuple โดยรับ iterable (เช่น List, String, หรือ Tuple อื่นๆ) เป็นอาร์กิวเมนต์ ตัวอย่างเช่น

\`\`\`python
# ใช้ tuple() constructor เพื่อสร้าง Tuple จาก List หรือ iterable อื่นๆ
tuple_constructor = tuple(['Jack', 'Maria', 'David'])
print(tuple_constructor)

**ผลลัพธ์: ('Jack', 'Maria', 'David')**
\`\`\`

**Tuple ว่าง (Empty Tuple)**

> สามารถสร้าง Tuple ที่ไม่มีสมาชิกได้โดยใช้เพียงวงเล็บเปล่า **\`()\`** หรือใช้ **\`tuple()\`** constructor ที่ไม่มีอาร์กิวเมนต์

\`\`\`python
### สร้าง Tuple ว่าง
empty_tuple = ()
print(empty_tuple)
### ผลลัพธ์: ()
\`\`\`


## Lab4 - Examples

### Lab4_Q1: CUT and SHUFFLE Operations
See file: [lab4_q1](Homework/week4/lab4_q1.py)

### Lab4_Q2: List Comprehension with Tuples
See file: [lab4_q2](Homework/week4/lab4_q2.py)
