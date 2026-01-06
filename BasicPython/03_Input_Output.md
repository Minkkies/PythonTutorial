# 3. การรับและแสดงผลข้อมูล (Input & Output) 
## การรับค่าจากผู้ใช้ (Input)
input() คือฟังก์ชันรับข้อมูลจากผู้ใช้ (stdin) และคืนค่าเป็น str เสมอ
  ```python
  name = input("ชื่อ: ")   # prompt แสดงก่อนรับค่า
  ```
แปลงชนิดหลังรับค่าเมื่อต้องการคำนวณ
  ```python
  age = int(input("อายุ: "))
  price = float(input("ราคา: "))
  ```
รับหลายค่าในบรรทัดเดียวด้วย split() และ map()
- .split(",") ถ้าไม่ใส่ parameter มันจะ split จากช่องว่าง คืนค่าเป็นรายการ (list)
  ```python
  a, b = input("สองค่า: ").split()        # คืนรายการของ str
  x, y = map(int, input().split())        # แปลงเป็น int โดยตรง
  nums = list(map(int, input().split()))  # รายการของ int
  ```
การจัดการช่องว่างและ newline
  - ใช้ strip()/rstrip()/lstrip() เพื่อลบช่องว่าง
  ```python
  s = input().strip()
  ```
รับค่าจากหลายบรรทัด (เช่น ข้อมูล competitive programming)
  - วนรอบอ่าน input() หลายครั้ง หรือใช้ sys.stdin.readline() ที่เร็วกว่า
  ```python
  import sys
  line = sys.stdin.readline().strip()
  ```
ตรวจจับข้อผิดพลาดการแปลงชนิด
  ```python
  try:
      n = int(input("เลข: "))
  except ValueError:
      print("กรุณากรอกตัวเลข")
  ```
การใช้ unpacking กับ split() เมื่อจำนวนค่าคงที่:
  ```python
  a, b, c = input().split()
  ```
เคล็ดลับ
  - input() คืน str เสมอ ต้องแปลงก่อนนำไปคำนวณ
  - สำหรับข้อมูลจำนวนมากหรือการรับเร็ว ใช้ sys.stdin.readline()
  - ใช้ map() กับ int/float เพื่อโค้ดกระชับและเร็วขึ้น
    - ```.strip()```: ใช้ลบ Whitespace (ช่องว่าง, tab,newline) ที่ส่วนหัวและท้ายของสตริง
    - ```.replace(old, new)``` แทนที่ old substring ด้วย new substring
    - ```.find(text)``` คืน index ของคำที่พบ

### split() - การแยกสตริง
**split():** แยกสตริงให้เป็นรายการโดยใช้ตัวคั่นที่กำหนด (default คือช่องว่างต่อเนื่อง)
- ช่องว่างรอบๆ: .split(',') ไม่ตัดช่องว่างรอบ token; ใช้ .strip() เพื่อทำความสะอาด
```py
'a b   c'.split()            # ['a', 'b', 'c']
'a, b , c'.split(',')        # ['a', ' b ', ' c']
[t.strip() for t in 'a, b , c'.split(',')]  # ['a', 'b', 'c']
```
### map() - การแปลงค่าทุกสมาชิก
**map():** นำฟังก์ชันไปใช้กับทุกสมาชิกของ iterable แล้วคืน iterator (ขี้เกียจ/lazy)

รูปแบบ: map(func, iterable) คืน iterator; หากต้องใช้หลายครั้งให้ทำ list(map(...))
- ใช้งานทั่วไป: แปลงชนิด str → int/float
```py
list(map(int, ['1', '2', '3']))    # [1, 2, 3]
list(map(str.upper, ['a', 'b']))   # ['A', 'B']
```

**ข้อควรระวัง:** 
- ความเป็น iterator: map(...) ใช้ได้ครั้งเดียว; หากต้องวนหลายรอบให้แปลงเป็น list(...)
- เครื่องหมาย , กับวงเล็บ () ความหมายต่างกัน
    - , = แยก argument
    - () = เรียกฟังก์ชัน
- ระวังเขียน map(int(x))
    - ❌ เรียก int ก่อน เพราะ input('...').split(',') จะได้เป็น list
        - int(list) ❌ ทำไม่ได้ → int แปลงได้ทีละค่า (str/number) เท่านั้น จึงเกิด TypeError
    - ✅ map(int, x) เมื่อ x เป็น list ของ string
        - map(int, x) จะนำ int ไป แปลงทีละสมาชิก ใน list ผลลัพธ์คือ iterable ของ int จากนั้นสามารถ unpack ใส่ตัวแปรได้

## การแสดงผล (Output)

### ฟังก์ชัน print()
```py
syntax => print(*objects, sep=" ", end="\n", file=sys.stdout, flush=False)
```

พารามิเตอร์หลัก:
- **objects**: ค่าหรือ expression ที่ต้องการพิมพ์ ใส่ได้หลายตัว แยกด้วยเครื่องหมายจุลภาค
- **sep**: ตัวคั่นระหว่างแต่ละ object ค่าเริ่มต้นคือช่องว่างหนึ่งตัว
- **end**: สิ่งที่ต่อท้ายบรรทัด ค่าเริ่มต้นคือขึ้นบรรทัดใหม่ "\n"
- **file**: สตรีมปลายทาง ค่าเริ่มต้นคือ sys.stdout
- **flush**: ถ้าเป็น True จะบังคับ flush buffer ทันที

### ตัวอย่างการใช้งาน print()
```python
# แสดงผลพื้นฐาน
print("Hello")           # Hello
print("Hello", "World")  # Hello World

# เปลี่ยน sep
print("a", "b", "c", sep=" + ")     # a + b + c
print("apple", "banana", sep=", ")  # apple, banana

# เปลี่ยน end
print("Loading", end="")
print(".")
print(".")
print(".")
# ผลลัพธ์: Loading...

# ใช้ร่วมกัน
print("Hello", "World", sep="-", end="!\n")  # Hello-World!
```

### การจัดรูปแบบข้อความ (String Formatting)

#### 1. f-strings (วิธีที่ดีที่สุด - Python 3.6+)
```python
name = "Alice"
age = 25
score = 95.5

# ใส่ตัวแปรในเครื่องหมาย {}
print(f"Name: {name}, Age: {age}")  # Name: Alice, Age: 25

# ระบุจำนวนทศนิยม
print(f"Score: {score:.1f}")        # Score: 95.5
print(f"Score: {score:.2f}")        # Score: 95.50

# การจัดแนว (alignment)
print(f"{name:>10}")        # ชิดขวา (10 ตัวอักษร)
print(f"{name:<10}")        # ชิดซ้าย (10 ตัวอักษร)
print(f"{name:^10}")        # ชิดกลาง (10 ตัวอักษร)
```

#### 2. เมธอด format()
```python
name = "Bob"
age = 30

# ใช้ {} และ .format()
print("Name: {}, Age: {}".format(name, age))      # Name: Bob, Age: 30

# ระบุ index
print("{0} is {1}".format(name, age))             # Bob is 30

# ตั้งชื่อ
print("{n} is {a}".format(n=name, a=age))         # Bob is 30
```

#### 3. String concatenation
```python
name = "Charlie"
age = 35

# ใช้ + (เรียบง่ายแต่ทีละบิต)
print("Name: " + name + ", Age: " + str(age))    # Name: Charlie, Age: 35

# ใช้ , ใน print
print("Name:", name, ", Age:", age)              # Name: Charlie , Age: 35
```

### ตัวอย่างการรับและแสดงผลรวมกัน
```python
# รับข้อมูลและแสดงผล
name = input("ชื่อ: ") # มิ้ง
age = int(input("อายุ: ")) # 20
height = float(input("ส่วนสูง: ")) # 152

# ใช้ f-strings
print(f"ชื่อ: {name}, อายุ: {age}, ส่วนสูง: {height:.2f}") # ชื่อ: มิ้ง, อายุ: 20, ส่วนสูง: 152.00

# ใช้ format()
print("ชื่อ: {}, อายุ: {}, ส่วนสูง: {:.2f}".format(name, age, height)) 

# ใช้ print กับ sep
print("ชื่อ:", name, "อายุ:", age, "ส่วนสูง:", round(height, 2), sep=" | ") # ชื่อ: มิ้ง | อายุ: 20 | ส่วนสูง: 152.00
```


**ตัวอย่างการใช้ร่วมกัน**
```py
a, b, c = map(int, input('Enter coefficients a, b, c : ').split(","))  # ✅ รันได้
a, b, c = map(int(input('Enter coefficients a, b, c : ').split(",")))  # ❌ รันไม่ได้
print(f"a: {a}, b: {b}, c: {c}")

name = input('Enter your name: ')  # แบบ Basic
print(f"name is: {name}")
print("hello", "world!", sep=" + ", end='')
```

**output:**
```py
Enter coefficients a, b, c : 1,2,3
a: 1, b: 2, c: 3
name is: <your name>
hello + world!
```
