# Python OOP Concepts - พื้นฐาน
## บทนำ OOP (Object-Oriented Programming)
### OOP คืออะไร?
OOP (Object-Oriented Programming) คือ แนวคิดการเขียนโปรแกรมที่เน้นการใช้ "วัตถุ" (Objects) ซึ่งเป็นการรวมข้อมูลและฟังก์ชันที่เกี่ยวข้องเข้าด้วยกัน เพื่อให้โค้ดมีความยืดหยุ่นและง่ายต่อการบำรุงรักษา

### ประโยชน์ของ OOP
- ✅ **Code Reusability** - นำโค้ดกลับมาใช้ได้
- ✅ **Modularity** - แบ่งโค้ดเป็นส่วนๆ จัดการง่าย
- ✅ **Maintainability** - แก้ไขบำรุงรักษาง่าย
- ✅ **Scalability** - ขยายระบบได้ง่าย

---

## แนวคิดพื้นฐานของ OOP ใน Python
## คลาส (Class)
>คลาส เปรียบเสมือน "พิมพ์เขียว" (Blueprint) ที่ใช้ในการสร้างวัตถุ (Object) โดยกำหนดคุณสมบัติ (Attributes) และพฤติกรรม (Methods) ของวัตถุนั้นๆ

## อ็อบเจกต์(Object)
>อ็อบเจกต์ คือ อินสแตนซ์ (Instance) ของคลาส ซึ่งเป็นการสร้างวัตถุจริงจากพิมพ์เขียวที่กำหนดไว้ในคลาส มีตัวตน จับต้องได้ หรือใช้งานได้จริงในหน่วยความจำ

<span style="color:lightgreen">**ตัวอย่างอ็อบเจกต์(Object)**</span>
- Object = คือ "บ้านที่สร้างเสร็จจริง" (Instance)
จากพิมพ์เขียวของบ้าน (Class)
- บ้านแต่ละหลังอาจมีสีต่างกัน ของตกแต่งต่างกัน (State)
- บ้านแต่ละหลังมีที่อยู่ไปรษณีย์ต่างกัน (Identity)
- บ้านแต่ละหลังสามารถเปิด-ปิดประตู (Behavior)

<span style="font-size:20px;"><b>ส่วนประกอบของ Object</b></span>

1. <span style="color:lightblue">**Attributes**</span>
: ข้อมูล/คุณสมบัติหรือสถานะของอ็อบเจกต์ เช่น สี, ขนาด, น้ำหนัก

2. <span style="color:lightblue">**Methods**</span>
: ฟังก์ชันหรือพฤติกรรมที่อ็อบเจกต์สามารถทำได้ เช่น เดิน, วิ่ง, พูด

### ตัวอย่างการสร้างคลาสและอ็อบเจกต์ใน Python
<span style="color:lightblue"><b>การสร้างclass:</b></span>
>สร้างขึ้นโดยใช้ Keyword ว่า class ตามด้วยชื่อคลาส ชื่อคลาสนิยมใช้ตัวพิมพ์ใหญ่ขึ้นต้น

<span style="color:lightblue"><b>การสร้างobject:</b></span>
>สร้างขึ้นโดยการเรียกใช้คลาสเหมือนเป็นฟังก์ชัน กระบวนการสร้างเรียกว่า Instantiation

<span style="color:lightblue"><b>การเข้าถึงคุณสมบัติ (Accessing Attributes):</b></span>
>ใช้เครื่องหมายจุด (.) หรือ Dot Notation ในการเข้าถึง Attributes และ Methods ของอ็อบเจกต์ 

```python
class Bike:
    # ตัวกำหนดคุณสมบัติ (Attributes)
    def __init__(self, color, model):
        self.color = color  # สีของจักรยาน 
        self.model = model  # รุ่นของจักรยาน

    # ตัวกำหนดพฤติกรรม (Methods)
    def ride(self):
        return f"The {self.color} {self.model} bike is being ridden."

# การสร้างอ็อบเจกต์ (Instance)
my_bike = Bike("red", "Mountain")
print(my_bike.ride())  # Output: The red Mountain bike is being ridden.

# การเข้าถึง Attributes
print(my_bike.color)  # Output: red
```

## เมธอด (Methods)
>Method คือฟังก์ชันที่ประกาศอยู่ภายในคลาส
>ใช้กำหนดพฤติกรรม (Behavior) ของอ็อบเจกต์
>ต้องมีพารามิเตอร์ตัวแรกเป็น self เสมอ (สำหรับ Instance Method) 

>self เป็นตัวแปรอ้างอิง (Reference) ที่ชี้ไปยังตัวอ็อบเจกต์ปัจจุบันที่กำลังทำงานอยู่

### ตัวอย่างการสร้าง Method
```python
class Room:
    length = 0.0 
    width = 0.0
    
    # การสร้าง Method เพื่อคำนวณพื้นที่
    def calculate_area(self):
        print("Area =", self.length * self.width)

study_room = Room() # สร้างอ็อบเจกต์
study_room.length = 42.5 # กำหนดความยาว Attributes
study_room.width = 30.8 # กำหนดความกว้าง Attributes
study_room.calculate_area() # เรียกใช้ Method
# Output: Area = 1309.0
```

### เมธอด `__init__`
>เป็นเมธอดพิเศษที่ใช้ในการกำหนดค่าเริ่มต้นให้กับ Attributes ของอ็อบเจกต์เมื่อมีการสร้างอ็อบเจกต์ใหม่ มักเรียกว่า Constructor ซึ่งจะถูกเรียกใช้อัตโนมัติเมื่อมีการสร้างอ็อบเจกต์ใหม่ทุกครั้ง

#### ตัวอย่างการใช้เมธอด `__init__`
```python
class Dog:
    def __init__(self, name, age):
        self.name = name # สร้าง instance variable
        self.age = age

# สร้าง Object ชื่อ dog1 
dog1 = Dog("บัดดี้", 3) # ส่งค่าเข้าไปทันทีตอนสร้าง object

# สั่งปริ้นชื่อ
print(dog1.name) # Output: บัดดี้
``` 

### เมธอด `__str__`
>เป็นเมธอดพิเศษที่ใช้กำหนดรูปแบบการแสดงผลของอ็อบเจกต์เมื่อมีการเรียกใช้ฟังก์ชัน print() หรือแปลงอ็อบเจกต์เป็นสตริง

>กำหนดการแสดงผลเมื่อ Object ถูกสั่ง print() → print(object)

#### ตัวอย่างการใช้เมธอด `__str__`
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # ฟังก์ชันนี้จะถูกเรียกอัตโนมัติเมื่อมีการสั่ง print(object)
    def __str__(self):
        return f"{self.name}({self.age})"

p1 = Person("John", 30)
print(p1) # ผลลัพธ์: John(30)
```
ถ้าไม่มีฟังก์ชั่น __str__() ผลลัพธ์จะเป็นการแสดงที่อยู่หน่วยความจำของอ็อบเจกต์แทน เช่น `<__main__.Person object at 0x7f9c8c2d1d60>`

## Instance Variables vs Class Variables
>ตารางสรุปความแตกต่างระหว่างตัวแปรระดับอินสแตนซ์และตัวแปรระดับคลาส

| หัวข้อ | Instance Variable (ต่ออ็อบเจกต์) | Class Variable (ร่วมกันทั้งคลาส) |
| --- | --- | --- |
| การประกาศ | ประกาศใน `__init__` หรือเมธอดอื่นด้วย `self.attr` | ประกาศในระดับคลาสนอกเมธอดด้วย `ClassName.attr` |
| ขอบเขต/การใช้ | เฉพาะอ็อบเจกต์นั้นๆ เปลี่ยนได้ไม่กระทบอ็อบเจกต์อื่น | แชร์ค่าร่วมกันทุกอ็อบเจกต์ของคลาสนั้น |
| การเข้าถึง | ผ่านอ็อบเจกต์: `obj.attr` | ผ่านคลาสหรืออ็อบเจกต์: `ClassName.attr` หรือ `obj.attr` |
| การเปลี่ยนค่า | `obj.attr = ...` เปลี่ยนเฉพาะอินสแตนซ์นั้น | เปลี่ยนที่คลาส: `ClassName.attr = ...` จะสะท้อนทุกอ็อบเจกต์ (ที่ยังไม่ override) |
| เหมาะใช้เมื่อ | ค่าต้องแยกตามอินสแตนซ์ เช่น ชื่อ อายุ ยอดคงเหลือ | ค่าคงที่หรือต้องใช้ร่วม เช่น ตัวนับจำนวนอินสแตนซ์ ค่า config ร่วม |
| ตัวอย่าง | `self.name`, `self.balance` | `interest_rate = 0.03`, `instance_count = 0` |


---