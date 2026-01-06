# 4. ตัวดำเนินการและคุณสมบัติข้อมูล (Operators & Data Properties)

## ตัวดำเนินการเลขคณิต (Arithmetic Operators)
```python
a = 10
b = 3

# บวก ลบ คูณ หาร
print(a + b)      # 13 (บวก)
print(a - b)      # 7 (ลบ)
print(a * b)      # 30 (คูณ)
print(a / b)      # 3.333... (หารปกติ - คืน float เสมอ)
print(a // b)     # 3 (หารแบบปัดลง - floor division)
print(a % b)      # 1 (เศษจากการหาร - modulo)
print(a ** b)     # 1000 (ยกกำลัง)

# การหารแบบต่าง ๆ
print(10 / 3)     # 3.3333... (float division)
print(10 // 3)    # 3 (floor division - ปัดลง)
print(-10 // 3)   # -4 (ปัดลงเพื่อให้ห่างจากศูนย์มากขึ้น)

# Modulo ใช้บ่อย
print(17 % 5)     # 2 (17 = 5*3 + 2)
print(20 % 3)     # 2 (20 = 3*6 + 2)
```

### ตัวดำเนินการกำหนดค่า (Assignment Operators)
```python
x = 10
x += 5    # x = x + 5 => 15
x -= 3    # x = x - 3 => 12
x *= 2    # x = x * 2 => 24
x /= 4    # x = x / 4 => 6.0
x //= 2   # x = x // 2 => 3.0
x %= 2    # x = x % 2 => 1.0
x **= 3   # x = x ** 3 => 1.0

# ตัวอย่างการใช้
count = 0
count += 1    # count = 1
count += 5    # count = 6
```

## ตัวดำเนินการเปรียบเทียบ (Comparison Operators)
คืนค่า `True` หรือ `False`
```python
x = 5
y = 10

print(x == y)     # False (เท่ากับ)
print(x != y)     # True (ไม่เท่ากับ)
print(x < y)      # True (น้อยกว่า)
print(x > y)      # False (มากกว่า)
print(x <= y)     # True (น้อยกว่าหรือเท่ากับ)
print(x >= y)     # False (มากกว่าหรือเท่ากับ)

# ใช้กับ string
print("apple" == "apple")     # True
print("apple" != "banana")    # True
print("apple" < "banana")     # True (เปรียบเทียบตัวอักษรแบบ lexicographic)

# ใช้กับ list
print([1,2] == [1,2])         # True (มีค่าเดียวกัน)
print([1,2] != [1,2,3])       # True (ไม่เท่ากัน)
```

### Chaining Comparisons (เปรียบเทียบแบบลูกโซ่)
```python
x = 5
print(0 < x < 10)      # True (เทียบเท่ากับ 0 < x and x < 10)
print(1 < x < 3)       # False

# ตัวอย่างจริง
age = 25
if 18 <= age < 65:
    print("เป็นวัยแรงงาน")
```

## ตัวดำเนินการตรรมชาติ (Logical Operators)
```python
a = True
b = False

print(a and b)    # False (ทั้งสองต้องเป็น True)
print(a or b)     # True (อย่างน้อยตัวเดียวต้องเป็น True)
print(not a)      # False (กลับค่า)

# ตัวอย่างการใช้งาน
age = 25
income = 50000
if age >= 18 and income >= 30000:
    print("ได้เงินกู้")
```

## ตัวดำเนินการสมาชิก (Membership Operators)
```python
fruits = ["apple", "banana", "cherry"]
x = "apple"

print(x in fruits)         # True
print("grape" not in fruits)  # True

# ใช้กับ string
text = "Hello"
print("H" in text)         # True
print("x" not in text)     # True
```

## ตัวดำเนินการเอกลักษณ์ (Identity Operators)
```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)     # True (อ้างอิงวัตถุเดียวกัน)
print(a is c)     # False (วัตถุคนละตัว)
print(a == c)     # True (มีค่าเท่ากัน)
print(a is not c) # True

# None ตรวจด้วย is
x = None
print(x is None)  # True ✅ ถูก
print(x == None)  # True แต่ไม่นิยม
```

## ลำดับความสำคัญของตัวดำเนินการ (Operator Precedence)
ตัวดำเนินการที่มีลำดับความสำคัญสูงจะถูกประเมินก่อน

| ลำดับ | ตัวดำเนินการ |
|------|------------|
| 1 | `**` (ยกกำลัง) |
| 2 | `+x, -x, ~x` (Unary operators) |
| 3 | `*, /, //, %` (คูณ หาร) |
| 4 | `+, -` (บวก ลบ) |
| 5 | `<, <=, >, >=, !=, ==` (เปรียบเทียบ) |
| 6 | `is, is not, in, not in` (สมาชิก/เอกลักษณ์) |
| 7 | `not` (NOT ตรรมชาติ) |
| 8 | `and` (AND ตรรมชาติ) |
| 9 | `or` (OR ตรรมชาติ) |

```python
# ตัวอย่าง
result = 2 + 3 * 4      # 14 (คูณก่อน: 3*4=12, แล้ว 2+12=14)
result = (2 + 3) * 4    # 20 (วงเล็บมีความสำคัญสูงสุด)
result = 2 ** 3 ** 2    # 512 (ยกกำลังมีลำดับจากขวามา: 3**2=9, 2**9=512)
```

## ตรวจสอบชนิดและวัตถุ
```python
type(x)         # คืนชนิดของวัตถุ
isinstance(x, int)  # ตรวจว่า x เป็น int หรือไม่ (ดีกว่า type())
id(x)           # คืนที่อยู่/เอกลักษณ์วัตถุ (ใช้ในการอธิบายการอ้างอิง)

# ตัวอย่าง
x = 10
print(type(x))          # <class 'int'>
print(isinstance(x, int))  # True
print(id(x))            # ตัวเลขเลขที่หน่วยความจำ
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
- **Immutable** (ไม่เปลี่ยน): int, float, str, tuple, bool, None
- **Mutable** (เปลี่ยนได้): list, dict, set

ความแตกต่างสำคัญเมื่อส่งผ่านตัวแปรเป็นอาร์กิวเมนต์ให้ฟังก์ชัน (การแก้ไขวัตถุ mutable จะเห็นผลจากภายนอก)

### ตัวอย่างความแตกต่าง Mutable vs Immutable
```python
# Immutable - สตริง
text = "hello"
text = text + " world"    # สร้างวัตถุใหม่ไม่ได้แก้ไขเดิม
print(text)               # "hello world"

# Immutable - จำนวน
x = 10
x = x + 5                 # สร้างวัตถุใหม่ไม่ได้แก้ไขเดิม
print(x)                  # 15

# Mutable - list
nums = [1, 2, 3]
nums.append(4)            # แก้ไขรายการเดิม ไม่สร้างใหม่
print(nums)               # [1, 2, 3, 4]

# Mutable - dict
person = {"name": "Alice", "age": 25}
person["age"] = 26        # แก้ไขวัตถุเดิม
print(person)             # {"name": "Alice", "age": 26}
```

### ผลกระทบเมื่อส่งให้ฟังก์ชัน
```python
# Immutable - ไม่มีผลภายนอก
def change_number(n):
    n = n + 10
    return n

x = 5
result = change_number(x)
print(x)       # 5 (ไม่เปลี่ยน)
print(result)  # 15

# Mutable - มีผลภายนอก
def add_item(lst):
    lst.append(99)
    return lst

numbers = [1, 2, 3]
add_item(numbers)
print(numbers)  # [1, 2, 3, 99] (เปลี่ยนไป!)
```

### การคัดลอก (Copy) ความแตกต่าง
```python
# Mutable - assignment คัดลอกการอ้างอิง
list1 = [1, 2, 3]
list2 = list1           # ชี้ไปยังวัตถุเดียวกัน
list2.append(4)
print(list1)            # [1, 2, 3, 4] (เปลี่ยนไป!)

# ต้องใช้ copy() เพื่อคัดลอกแท้จริง
list3 = [1, 2, 3]
list4 = list3.copy()    # คัดลอกแท้จริง
list4.append(4)
print(list3)            # [1, 2, 3] (ไม่เปลี่ยน)
```

## ตัวอย่างรวมและสรุป
```python
# ตัวอย่างที่ 1: การตรวจสอบผลประเมิน
x = 15
if 10 < x < 20:
    print(f"{x} อยู่ระหว่าง 10-20")

# ตัวอย่างที่ 2: การใช้ assignment operators
score = 0
for i in range(5):
    score += 10
print(f"คะแนนรวม: {score}")  # 50

# ตัวอย่างที่ 3: การใช้ logical operators
username = input("ชื่อผู้ใช้: ")
age = int(input("อายุ: "))

if len(username) >= 3 and age >= 13:
    print("สมัครสมาชิกได้")
else:
    print("ไม่สามารถสมัครสมาชิก")

# ตัวอย่างที่ 4: membership operator กับ list
fruits = ["apple", "banana", "cherry"]
choice = input("เลือกผลไม้: ")

if choice in fruits:
    print(f"{choice} มีในรายการ")
else:
    print(f"{choice} ไม่มีในรายการ")

# ตัวอย่างที่ 5: mutable vs immutable
# ❌ เรียมไม่ได้กับ str (immutable)
text = "hello"
# text[0] = "H"    # Error!

# ✅ เรียมได้กับ list (mutable)
chars = ['h', 'e', 'l', 'l', 'o']
chars[0] = 'H'
print(''.join(chars))  # Hello
```

## เคล็ดลับและข้อเตือน
1. **ตรวจสอบชนิด**: ใช้ `isinstance()` แทน `type()` เพื่อความถูกต้องมากขึ้น
2. **Short-circuit**: ใช้ประโยชน์จาก and/or เพื่อหลีกเลี่ยง error
3. **Mutable traps**: ระวังการแก้ไข list/dict ที่ไม่ตั้งใจ
4. **None checks**: ตรวจสอบ `is None` ไม่ใช่ `== None`
5. **Operator precedence**: ใช้วงเล็บถ้าไม่แน่ใจลำดับการประเมิน
- ตั้งชื่อตัวแปรให้สื่อความหมายเพื่อความชัดเจนของโค้ด
