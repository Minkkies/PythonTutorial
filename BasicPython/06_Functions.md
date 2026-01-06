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

### ตัวอย่างพื้นฐาน
```python
# ฟังก์ชันง่ายที่สุด
def greet():
    print("สวัสดี")

greet()

# ฟังก์ชันที่รับพารามิเตอร์
def add(a, b):
    """คืนผลบวกของ a และ b"""
    return a + b

result = add(3, 4)  # 7
print(result)
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
    ```py
    # ✅ ถูก - พารามิเตอร์ปกติ (a, b) มาก่อน ค่อย default parameters (c, d) มาหลัง
    def func(a, b, c=10, d=20):
        pass

    # ❌ ผิด - พารามิเตอร์มี default (c=10) อยู่ก่อน พารามิเตอร์ปกติ (b)
    def func(a, c=10, b, d=20):
        pass
    ```
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
#### ตารางชนิดของอาร์กิวเมนต์
  | ชนิด (Type)              | รูปแบบ (Syntax) | โครงสร้างข้อมูล | จุดเด่น                                     |
| ------------------------ | --------------- | --------------- | ------------------------------------------- |
| **Positional**           | func(a, b)    | ตัวแปรเดี่ยว    | รับค่าตามลำดับก่อน–หลัง ต้องส่งค่าให้ครบ    |
| **Keyword**              | func(k=v)     | ตัวแปรเดี่ยว    | ระบุชื่อชัดเจน สลับลำดับได้                 |
| **Default**              | func(a=1)     | ตัวแปรเดี่ยว    | มีค่าเริ่มต้นให้ ถ้าไม่ส่งค่ามาจะใช้ค่านั้น |
| **Arbitrary Positional** | *args         | tuple         | รับค่าได้ไม่จำกัดจำนวน (ตามลำดับ)           |
| **Arbitrary Keyword**    | **kwargs      | dictionary    | รับค่าแบบ key=value ได้ไม่จำกัด      |
    

## Scope และตัวแปรภายใน/ภายนอก
- ตัวแปรภายในฟังก์ชันเป็น `local` มองไม่เห็นจากภายนอก
    - เกิดและดับในฟังก์ชัน: สร้างขึ้นเมื่อฟังก์ชั่นถูกเรียก และถูกทำลายเมื่อฟังก์ชันจบ
    - เข้าถึงได้เฉพาะภายใน: ไม่สามารถเรียกใช้ตัวแปรนี้จากภายนอกฟังก์ชันได้
```py
def greet():
    # local variable
    message = 'Hello'
    print('Local', message)

greet()
# try to access message variable
# outside greet() function
print(message)
```
- ใช้ `global` เพื่ออ้างอิงและแก้ตัวแปรระดับโมดูล (ใช้เท่าที่จำเป็น) ตัวแปรที่ถูกประกาศไว้นอกฟังก์ชัน
  - หากต้องการเพียงอ่าน (read) ตัวแปร global ไม่ต้องใช้ keyword `global`
  - แต่หากต้องการแก้ไข (write/modify) ตัวแปร global จำเป็นต้องประกาศ `global` ไว้ข้างต้น
```py
# ตัวอย่างที่ 1: อ่านเฉพาะ (ไม่ต้องใช้ global)
message = 'Hello'
def greet():
    # เข้าถึงตัวแปร global เพื่ออ่านเฉพาะ
    print('Message:', message)

greet()  # Message: Hello
print('Global', message)  # Global Hello

# ตัวอย่างที่ 2: แก้ไขตัวแปร global (ต้องใช้ global)
count = 0

def inc():
    global count  # ต้องประกาศ global ก่อน
    count += 1

inc()
print(count)  # 1
inc()
print(count)  # 2
```

- ใช้ `nonlocal` เพื่ออ้างอิงและแก้ตัวแปรใน enclosing scope (ฟังก์ชันซ้อน)
  - ใช้ในฟังก์ชันชั้นใน (nested function) เพื่ออ้างอิงตัวแปรของฟังก์ชันชั้นนอก
  - `nonlocal` เหมาะสำหรับฟังก์ชันซ้อนเท่านั้น (ไม่ใช้กับตัวแปร global)

```python
# ตัวอย่าง: ฟังก์ชันซ้อน + nonlocal
def outer():
    count = 0  # ตัวแปรของ outer
    
    def inner():
        nonlocal count  # ต้องประกาศ nonlocal เพื่อแก้ไข count ของ outer
        count += 1
    
    inner()
    print("After inner():", count)  # 1
    inner()
    print("After inner():", count)  # 2

outer()

# ตัวอย่างที่ 2: ฟังก์ชันซ้อนหลายชั้น
def level1():
    x = 10
    
    def level2():
        y = 20
        
        def level3():
            nonlocal y  # อ้างอิง y จาก level2
            y += 5
            print(f"level3: y = {y}")
        
        level3()  # level3: y = 25
    
    level2()

level1()
```

```text
ตัวอย่างผลลัพท์
After inner(): 1
After inner(): 2
level3: y = 25
```

## Return หลายค่า (tuple packing/unpacking)
```python
def min_max(nums):
    return min(nums), max(nums)

lo, hi = min_max([3, 1, 4])  # lo=1, hi=4
print(f"ต่ำสุด: {lo}, สูงสุด: {hi}")

# ตัวอย่างอื่น
def divide_with_remainder(a, b):
    return a // b, a % b

quotient, remainder = divide_with_remainder(17, 5)
print(f"17 ÷ 5 = {quotient} เศษ {remainder}")  # 17 ÷ 5 = 3 เศษ 2

# แม้ไม่ unpacking ก็ได้
result = min_max([1, 2, 3])
print(result)  # (1, 3)
```

## ตัวอย่างรวมและ Best Practices
```python
# ตัวอย่างที่ 1: ฟังก์ชันคำนวณง่ายๆ
def calculate_gpa(scores):
    """
    คำนวณคะแนนเฉลี่ย
    
    Args:
        scores: รายการของคะแนน
    
    Returns:
        ค่าเฉลี่ย
    """
    if not scores:
        return 0
    return sum(scores) / len(scores)

scores = [80, 85, 90]
gpa = calculate_gpa(scores)
print(f"GPA: {gpa:.2f}")  # GPA: 85.00

# ตัวอย่างที่ 2: การใช้ positional + keyword + default
def create_profile(name, age, city="Unknown", is_active=True):
    """สร้างโปรไฟล์ผู้ใช้"""
    return {
        "name": name,
        "age": age,
        "city": city,
        "active": is_active
    }

# วิธีการต่างๆ ในการเรียก
profile1 = create_profile("Alice", 25)
profile2 = create_profile("Bob", 30, "Bangkok")
profile3 = create_profile(name="Charlie", age=28, city="Chiang Mai", is_active=False)
profile4 = create_profile("Diana", 35, is_active=False)  # keyword บางตัว

print(profile3)  # {'name': 'Charlie', 'age': 28, 'city': 'Chiang Mai', 'active': False}

# ตัวอย่างที่ 3: ใช้ *args
def sum_numbers(*numbers):
    """บวกจำนวนใดๆ"""
    return sum(numbers)

print(sum_numbers(1, 2, 3))           # 6
print(sum_numbers(10, 20, 30, 40))    # 100

# ตัวอย่างที่ 4: ใช้ **kwargs
def print_details(**details):
    """พิมพ์รายละเอียด"""
    for key, value in details.items():
        print(f"{key}: {value}")

print_details(name="Alice", age=25, city="Bangkok")
# name: Alice
# age: 25
# city: Bangkok

# ตัวอย่างที่ 5: รวม positional, *args, และ **kwargs
def flexible_func(required, *args, **kwargs):
    """ฟังก์ชันที่ยืดหยุ่น"""
    print(f"Required: {required}")
    print(f"Extra positional: {args}")
    print(f"Extra keyword: {kwargs}")

flexible_func(1, 2, 3, 4, name="Alice", age=25)
# Required: 1
# Extra positional: (2, 3, 4)
# Extra keyword: {'name': 'Alice', 'age': 25}
```

## ข้อควรระวังและเคล็ดลับ
1. **Default parameter กับ mutable objects**: ระวังให้มาก
   ```python
   # ❌ เป็นอันตราย
   def append_item(item, items=[]):
       items.append(item)
       return items
   
   print(append_item(1))  # [1]
   print(append_item(2))  # [1, 2] - ไม่ใช่ [2]!

   # ✅ ถูกวิธี
   def append_item(item, items=None):
       if items is None:
           items = []
       items.append(item)
       return items
   
   print(append_item(1))  # [1]
   print(append_item(2))  # [2]
   ```

2. **ลำดับอาร์กิวเมนต์**: positional → *args → keyword → **kwargs
   ```python
   def func(a, b, *args, x=10, y=20, **kwargs):
       pass
   ```

3. **Docstring สำคัญ**: ทำให้โค้ดเข้าใจง่าย
   ```python
   def calculate(x, y, operation="+"):
       """
       คำนวณผลลัพธ์ของสองจำนวน
       
       Args:
           x: จำนวนแรก
           y: จำนวนที่สอง
           operation: "+", "-", "*", "/" (ค่าเริ่มต้น "+")
       
       Returns:
           int/float: ผลลัพธ์
       """
       if operation == "+":
           return x + y
       elif operation == "-":
           return x - y
       # ...
   ```