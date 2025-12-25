# 1. บทนำ (Introduction)
[Python คืออะไร / ภาษา Python ใช้ทำอะไรได้บ้าง / วิธีลงไพทอน](https://docs.mikelopster.dev/c/python-series/101/intro)

watch: [Basic Python](https://www.youtube.com/watch?v=ESNFhgRqeow&list=PLwZ0y9k-cYXALFTl5X2A3IPNTyK-9vm-v&index=6)

สามารถรัน Python ได้ 2 วิธี :
1. พิมใน Terminal => python (..ชื่อไฟล์..)
2. กด Run code ใน VSC Ctrl+Alt+N ก่อนกดโหลด Python ใน VSC ก่อน

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
- พื้นฐาน: int, float, str, bool, None, list, tuple, dict, set
- แปลงชนิด:
```python
n = int("10")
f = float("3.14")
s = str(123)
b = bool(0)  # False
```

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

```py
syntax => print(*objects, sep=" ", end="\n", file=sys.stdout, flush=False)
```
พารามิเตอร์หลัก:

- *objects ค่าหรือ expression ที่ต้องการพิมพ์ ใส่ได้หลายตัว แยกด้วยเครื่องหมายจุลภาค
- sep ตัวคั่นระหว่างแต่ละ object ค่าเริ่มต้นคือช่องว่างหนึ่งตัว
- end สิ่งที่ต่อท้ายบรรทัด ค่าเริ่มต้นคือขึ้นบรรทัดใหม่ "\n"
    ```py
    print("hello", "world!", sep=" + ", end='') # hello + world!
    ```
    - sep=" + " -> ขั้นกลางด้วยอะไร
    - end='' -> ต่อท้ายอยากให้ทำไร กรณี end='' -> ไม่ขึ้นบรรทัดใหม่
- file สตรีมปลายทาง ค่าเริ่มต้นคือ sys.stdout
- flush ถ้าเป็น True จะบังคับ flush buffer ทันที


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

# 4. ตัวดำเนินการและคุณสมบัติข้อมูล (Operators & Data Properties)

## ตรวจสอบชนิดและวัตถุ
```python
type(x)         # คืนชนิดของวัตถุ
isinstance(x, int)  # ตรวจว่า x เป็น int หรือไม่
id(x)           # คืนที่อยู่/เอกลักษณ์วัตถุ (ใช้ในการอธิบายการอ้างอิง)
```

## การลบตัวแปร
```python
del x    # ลบการอ้างอิงตัวแปร x
```

## ขอบเขตของตัวแปร (Variable Scope)
- Local: ตัวแปรภายในฟังก์ชัน
- Global: ตัวแปรระดับโมดูล
- ใช้ `global` เพื่ออ้างอิงตัวแปร global ภายในฟังก์ชัน (ควรใช้อย่างระมัดระวัง)
```python
count = 0
def inc():
    global count
    count += 1
```

## ความสามารถในการเปลี่ยนแปลงค่า (Mutability vs Immutability)
- Immutable: int, float, str, tuple
- Mutable: list, dict, set
ความแตกต่างสำคัญเมื่อส่งผ่านตัวแปรเป็นอาร์กิวเมนต์ให้ฟังก์ชัน (การแก้ไขวัตถุ mutable จะเห็นผลจากภายนอก)

## ตัวอย่างรวมสั้น ๆ
```python
# กำหนดและใช้งานตัวแปร
name = input("ชื่อ: ")
age = int(input("อายุ: "))
greeting = f"สวัสดี {name}, อายุ {age}"
print(greeting)

# List เป็น mutable
nums = [1,2,3]
nums.append(4)   # nums => [1,2,3,4] เป็นการเพิ่ม 4 เข้าไปที่ตัวสุดท้ายของ list
```

## เคล็ดลับสั้น ๆ
- ใช้ `type()` และ `isinstance()` ตรวจชนิดขณะดีบัก
- แปลงชนิดของ input ก่อนนำไปคำนวณ (input คืน str)
- ตั้งชื่อตัวแปรให้สื่อความหมายเพื่อความชัดเจนของโค้ด

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

---

### If ย่อ
```py
number = 5
if number > 0: print(number, '> 0')
```

### Conditional Expression
Syntax: ` (true_value if ..condition.. else false_value) `

normal
```py
grade = 40
if grade >= 50:
    result = 'pass'
else:
    result = 'fail'
print(result)
```
Expression
```py
grade = 40
result = 'pass' if grade >= 50 else 'fail'
print(result)
```

## ลูป for
- ใช้ วนซ้ำ(iterate) กับ iterable ใด ๆ (list, tuple, dict, string, range ,sets)
- `range(start,step,stop)` มักใช้สร้างลำดับตัวเลข
- default start = 0 & step = 1 ต้องกำหนด stop ถ้ามีการกำหนดค่ามาจะเป็น Stop โดยทันที

ตัวอย่าง:
```python
for i in range(5):      # 0..4
    print(i)

words = ["a", "b", "c"]
for w in words: # word = list ; w = index
    print(w)
```

## ลูป while
- ใช้วนซ้ำตราบใดที่เงื่อนไขเป็นจริง

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
ระวัง infinite loop หากเงื่อนไขไม่มีการเปลี่ยนแปลง หรือมันมีค่าเป็นจริงเสมอ

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

## else กับลูป
ลูป (for/while) สามารถมี else ซึ่งจะรันเมื่อไม่มีการจบลูปด้วย break:
```python
for i in range(3):
    print(i)
else:
    print("จบโดยไม่มี break")
```


## enumerate/zip:
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


# 6.ฟังก์ชันพื้นฐาน (Functions)

## ทำไมต้องใช้ฟังก์ชัน
- แยกส่วนการทำงานให้ชัดเจน นำกลับมาใช้ซ้ำได้
- ลดการซ้ำซ้อนของโค้ด ช่วยให้อ่านง่ายและทดสอบง่าย
- ควบคุมขอบเขตตัวแปร (scope) ให้เป็นสัดส่วน

## โครงสร้างพื้นฐาน
```python
def ชื่อฟังก์ชัน(พารามิเตอร์...):
    """docstring อธิบายการทำงาน"""
    # บล็อกคำสั่ง
    return ค่าที่จะส่งกลับ  # ถ้าไม่ใส่ return จะคืน None
```

ตัวอย่าง:
```python
def add(a, b):
    """คืนผลบวกของ a และ b"""
    return a + b

result = add(3, 4)  # 7
```

## พารามิเตอร์และอาร์กิวเมนต์
>**Parameters (พารามิเตอร์)** คือตัวแปรที่ถูกระบุไว้ภายในวงเล็บ ()ตอนที่ทำการนิยาม (Def) ฟังก์ชัน ทำหน้าที่เป็นตัวรับค่า <br>
>**Arguments (อาร์กิวเมนต์)** คือค่าจริง (Inputs) ที่ถูกส่งเข้าไปยังฟังก์ชันเมื่อทำการเรียกใช้งาน (Call) เพื่อให้ฟังก์ชันนำไปประมวลผล

ประเภทของ Arguments:
1. Positional: อาร์กิวเมนต์ตามตำแหน่ง
    - การส่งค่าจะยึด "ลำดับ" (Order)เป็นหลักค่าแรกจะถูกส่งไปที่พารามิเตอร์ตัวแรก ค่าที่สองไปตัวที่สองตามลำดับ
    ```py
    def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)

    # กรณีที่ 1: ส่งอําร์กิวเมนต์ถูกต้องตามตำแหน่ง
    print("Case-1:")
    nameAge("Sarawut", 32)
    # Case-1:
    # Hi, I am Sarawut
    # My age is  32

    # กรณีที่ 2: ส่งอําร์กิวเมนต์สลับตำแหน่งกัน
    print("\nCase-2:")
    nameAge(32,"Sarwut")
    # Case-2:
    # Hi, I am 32
    # My age is  Sarwut
    ```
    **ข้อควรระวัง**: หากจำลำดับผิดหรือใส่สลับกันโปรแกรมอาจทำงานผิดพลาดได้
2. Keyword: ระบุชื่อพารามิเตอร์ชัดเจน เป็นอาร์กิวเมนต์แบบคีย์เวิร์ด
    - การส่งค่าเข้าสู่ฟังก์ชันโดยการระบุชื่อของอาร์กิวเมนต์ ควบคู่ไปกับค่าที่ต้องการกำหนด
    - วิธีนี้ทำให้สามารถส่งค่าให้กับอาร์กิวเมนต์โดยไม่จำเป็นต้องเรียงตามลำดับตำแหน่งที่ประกาศไว้ในฟังก์ชัน
    ```py
    def display_info(first_name, last_name):
    print('first_name:', first_name)
    print('last_name:', last_name)

    # การเรียกใช้ฟังก์ชันแบบ Keyword Argument
    # สังเกตว่ําสลับตำแหน่งได้ เพราะระบุชื่อชัดเจน
    display_info(last_name = 'Meesri', first_name = 'Sarawut')

    #first_name: Sarawut
    #last_name: Meesri
    ```
3. Default: มีค่าเริ่มต้น หากไม่ส่งเข้ามาจะใช้ค่านั้น 
    - สามารถกำหนดค่าเริ่มต้นให้พาราได้ หากผู้ใช้ไม่ส่งค่ามา โปรแกรมจะใช้ค่าDefault นี้แทนโดยอัตโนมัติ
    ```py
    def greet(name, message="Hello"):
    print(message, name)
    
    # กํารเรียกใช้ฟังก์ชันโดยส่งผ่ํานอําร์กิวเมนต์ทั้งสอง
    greet("Alice","Good Morning")

    # กํารเรียกใช้ฟังก์ชันโดยส่งผ่ํานอําร์กิวเมนต์เพียงหนึ่งเดียว
    greet("Bob")

    #Good Morning Alice
    #Hello Bob
    ```
    **กฎสำคัญ: พารามิเตอร์ที่มีค่า Defaultต้องอยู่หลัง พารามิเตอร์ปกติเสมอ**
4. Arbitrary: ไม่จำกัดจำนวน (*args, **kwargs)

    - `Arbitrary Arguments (*args)` รับหลายค่าเป็น tupleใช้ในกรณีที่ไม่ทราบล่วงหน้าว่าจะมีอาร์กิวเมนต์ส่งเข้ามากี่ตัว
        - ใช้เครื่องหมาย * หน้าชื่อพารามิเตอร์
        - จะรวบรวมค่าทั้งหมดที่ส่งเข้ามา (แบบ Positional) เก็บไว้ในตัวแปรเดียวในรูปแบบของ Tuple ซึ่งสามารถวนลูปใช้งานได้
        ```py
        def sum_all(*numbers):
        total = 0
        for num in numbers:
            total += num
        return total

        # เรียกใช้ฟังก์ชันด้วยจ ํานวนอําร์กิวเมนต์ที่แตกต่ํางกัน
        print(sum_all(1, 2, 3))
        print(sum_all(10, 20, 30, 40, 50))
        # 6
        # 150
        ```
    - `Arbitrary Keyword Args (**kwargs)` ใช้รับค่าแบบ Keyword (Key = Value )ได้ไม่จำกัดจำนวน
        - ใช้เครื่องหมาย ** หน้าชื่อพารามิเตอร์
        - ข้อมูลจะถูกเก็บในรูปแบบ Dictionary
        - Key = ชื่อตัวแปร
        - Value = ค่าที่ส่งมา
        ```py
        def show_info(**kwargs):
            print("ข้อมูลที่ได้รับคือ:")
            # kwargs คือ dictionary เราจึงใช้ .items() เพื่อวนลูป
            for key, value in kwargs.items():
                print(f"-{key}: {value}")

        # เรียกใช้งําน
        show_info(name="สมศรี", age=35, city="กรุงเทพ")
        show_info(item="หนังสือ", price=250, author="นักเขียนนิรนําม", in_stock=True)
        # ข้อมูลที่ได้รับคือ:
        # -name: สมศรี
        # -age: 35
        # -city: กรุงเทพ

        # ข้อมูลที่ได้รับคือ:
        # -item: หนังสือ
        # -price: 250
        # -author: นักเขียนนิรนําม
        # -in_stock: True
        ```

## Scope และตัวแปรภายใน/ภายนอก
- ตัวแปรภายในฟังก์ชันเป็น **local** มองไม่เห็นจากภายนอก
- ใช้ `global` เพื่อแก้ตัวแปรระดับโมดูล (ใช้เท่าที่จำเป็น)
- ใช้ `nonlocal` เพื่อแก้ตัวแปรใน enclosing scope (ฟังก์ชันซ้อน)

```python
count = 0

def inc():
    global count
    count += 1
```

## Return หลายค่า (tuple packing/unpacking)
```python
def min_max(nums):
    return min(nums), max(nums)

lo, hi = min_max([3, 1, 4])  # lo=1, hi=4
```


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