# Python OOP - หลักการทั้ง 4 (แบบละเอียด)
## หลักการสำคัญของ OOP
## 1. Encapsulation (การห่อหุ้ม)
>การรวมข้อมูลและฟังก์ชันที่เกี่ยวข้องเข้าด้วยกันในวัตถุเดียว และการซ่อนข้อมูลที่ไม่จำเป็นต้องแสดง โดยใช้ Access Modifiers

### ระดับการเข้าถึงข้อมูล (Access Modifiers)
1. Public (เข้าถึงได้ทุกที่)
- ชื่อ Attribute/Method ปกติ เช่น `self.name`
2. Protected (เข้าถึงได้ภายในคลาสและซับคลาส)
- ชื่อ Attribute/Method ขึ้นต้นด้วย `_` เช่น `self._age`
3. Private (เข้าถึงได้เฉพาะภายในคลาส)
- ชื่อ Attribute/Method ขึ้นต้นด้วย `__` เช่น `self.__salary`

### ตัวอย่าง Encapsulation
```python
class BankAccount:
    def __init__(self):
        self.balance = 1000

    def _show_balance(self):
        # Protected method: ส าหรับแสดงยอดเงิน
        print(f"ยอดเงินคงเหลือ: {self.balance} บาท")

    def __update_balance(self, amount):
        # Private method: ส าหรับอัปเดตยอดเงิน
        self.balance += amount

    def deposit(self, amount):
        if amount > 0:
        # เรียกใช้ private method ภายในคลาส
        self.__update_balance(amount)
        # เรียกใช้ protected method
        self._show_balance()
    else:
        print("จำนวนเงินที่ฝากไม่ถูกต้อง!")

# การใช้งาน
account = BankAccount()
account._show_balance() # ทำงานได้ แต่ตามหลักแล้วไม่ควรเรียกจากภายนอก
# account.__update_balance(500) # บรรทัดนี้จะทำให้เกิด Error
account.deposit(500) # ใช้วิธีที่ถูกต้องผ่าน public method
```

### การเข้าถึง Private Method
ในเมื่อ Private เข้าถึงไม่ได้ จะใช้งานยังไง?
- สามารถสร้าง Public Method เพื่อเรียกใช้ Private Method ภายในคลาสได้ ด้วย Getter & Setter Methods

<span style="color:lightgreen">**ตัวอย่าง Getter Methods**</span>
```python
class Employee:
    def __init__(self):
        self.__salary = 50000 # Private attribute

    # Getter สำหรับเข้าถึงค่า salary
    def get_salary(self):
        return self.__salary
```

<span style="color:lightgreen">**ตัวอย่าง Setter Methods**</span>
```python
# Setter สำหรับกำหนดค่า salary
    def set_salary(self, amount):
        if amount > 0:
            self.__salary = amount
            print(f"Update salary to {amount}")
        else:
            print(" Error: เงินเดือนห้ามติดลบ!")
```
และสามารถเรียกใช้ได้ดังนี้:
```python
emp = Employee()
# emp.__salary = -100 < ท าไม่ได้ (มองไม่เห็น)

# ต้องแก้ผ่าน Setter
emp.set_salary(60000) # ผ่าน: Update salary to 60000
emp.set_salary(-500) # ไม่ผ่าน: Error: เงินเดือนห้ามติดลบ!

# ต้องอ่านผ่าน Getter
print(emp.get_salary()) # ผลลัพธ์: 60000
```

## 2. Abstraction (การซ่อนรายละเอียด)
>การซ่อนรายละเอียดที่ซับซ้อนและแสดงเฉพาะฟังก์ชันหรือเมธอดที่จำเป็น

### ตัวอย่าง Abstraction
```python
class Car:
    def __init__(self, brand):
        self.brand = brand
    
    # วิธีการที่ซับซ้อนแต่ซ่อนอยู่
    def __start_engine(self):
        print("🔧 Starting engine...")
        print("⚡ Charging battery...")
        print("🔥 Igniting fuel...")
    
    # แสดงเฉพาะส่วนที่ผู้ใช้ต้องรู้
    def start(self):
        self.__start_engine()
        print("✅ Car is ready!")

car = Car("Toyota")
car.start()  # ผู้ใช้ไม่ต้องรู้รายละเอียด เพียงเรียก start()
# Output:
# 🔧 Starting engine...
# ⚡ Charging battery...
# 🔥 Igniting fuel...
# ✅ Car is ready!
```

## 3. Inheritance (การสืบทอด)
>เป็นกระบวนการที่คลาสใหม่ (Subclass/Child Class) สามารถสืบทอดคุณสมบัติและพฤติกรรมจากคลาสที่มีอยู่แล้ว (Superclass/Parent Class) ทำให้สามารถนำโค้ดที่มีอยู่มาใช้ซ้ำได้

### Syntax
```python
# คลาสแม่ (Parent/Superclass)
class ParentClass:
    pass

# คลาสลูก (Child/Subclass)
# ใส่ชื่อ Parent ในวงเล็บ เพื่อบอกว่า "ฉันเป็นลูกของคนนี้นะ"
class ChildClass(ParentClass):
    pass
```

### ตัวอย่างการใช้ Inheritance
```python
# 1. สร้างคลาสแม่ (Animal)
class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating")

# 2. สร้างคลาสลูก (Dog) ที่สืบทอดมาจาก Animal
class Dog(Animal):
    # เมธอดใหม่ของ Dog
    def bark(self):
        print(f"{self.name} says: Woof!")

# การใช้งาน
dog = Dog("Buddy")
dog.eat()    # เรียกเมธอดของแม่
dog.bark()   # เรียกเมธอดของตัวเอง
# Output:
# Buddy is eating
# Buddy says: Woof!
```

### ใช้ super() เพื่อเรียกเมธอดของแม่
```python
# 1. คลาสแม่ (พนักงานทั่วไป)
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

# 2. คลาสลูก (Developer) สืบทอดมาจาก Employee
class Developer(Employee):
    def __init__(self, name, salary, lang):
        # "ส่งงานให้แม่ทำ" (โยน name, salary ไปให้ Employee จัดการ)
        super().__init__(name, salary)

        # "ทำส่วนของตัวเอง" (เพิ่ม attribute ใหม่ที่แม่ไม่มี)
        self.prog_lang = lang

# สร้าง Developer
dev = Developer("Somchai", 50000, "Python")
print(f"Name: {dev.name}") # Name: Somchai
print(f"Salary: {dev.salary}") # Salary: 50000
print(f"Language: {dev.prog_lang}") # Language: Python
```

---

### ประเภทของการสืบทอด (Types of Inheritance)

Python รองรับการสืบทอด 5 ประเภท ดังนี้:

#### 1. Single Inheritance (การสืบทอดเดี่ยว)
>คลาสลูกสืบทอดจากคลาสแม่เพียงคลาสเดียว (1 ลูก : 1 แม่)

```python
class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):  # Dog สืบทอดจาก Animal เพียงตัวเดียว
    def bark(self):
        print("Dog is barking")

dog = Dog()
dog.eat()   # Output: Animal is eating
dog.bark()  # Output: Dog is barking
```

**โครงสร้าง:**
```
    Animal
      ↓
     Dog
```

#### 2. Multiple Inheritance (การสืบทอดหลายคลาส)
>คลาสลูกสืบทอดจากหลายคลาสแม่ (1 ลูก : หลายแม่)

```python
class Father:
    def height(self):
        print("Tall")

class Mother:
    def skin(self):
        print("Fair skin")

class Child(Father, Mother):  # สืบทอดทั้ง Father และ Mother
    def personality(self):
        print("Friendly")

child = Child()
child.height()       # Output: Tall (จาก Father)
child.skin()         # Output: Fair skin (จาก Mother)
child.personality()  # Output: Friendly (ของตัวเอง)
```

**โครงสร้าง:**
```
  Father    Mother
     ↘      ↙
      Child
```
<span style="color:red;"><b>ข้อควรระวัง:</b></span> 
- ถ้า Mom และ Dad มี method ชื่อเหมือนกัน
- Python จะใช้ลำดับ MRO (Method Resolution Order)
- ยึดตามลำดับในวงเล็บ (Mom, Dad) -> Mom มาก่อน

#### 3. Multilevel Inheritance (การสืบทอดหลายระดับ)
>คลาสลูกสืบทอดจากคลาสแม่ แล้วคลาสลูกนั้นก็กลายเป็นแม่ให้คลาสถัดไปอีก (ปู่ → พ่อ → ลูก)

```python
class Grandparent:
    def heritage(self):
        print("Family heritage")

class Parent(Grandparent):  # สืบทอดจาก Grandparent
    def house(self):
        print("Family house")

class Child(Parent):  # สืบทอดจาก Parent (ได้ทั้ง Parent และ Grandparent)
    def education(self):
        print("Modern education")

child = Child()
child.heritage()   # Output: Family heritage (จากปู่)
child.house()      # Output: Family house (จากพ่อ)
child.education()  # Output: Modern education (ของตัวเอง)
```

**โครงสร้าง:**
```
 Grandparent
     ↓
   Parent
     ↓
   Child
```

#### 4. Hierarchical Inheritance (การสืบทอดแบบลำดับชั้น)
>หลายคลาสลูกสืบทอดจากคลาสแม่เพียงคลาสเดียว (1 แม่ : หลายลูก)

```python
class Vehicle:
    def start(self):
        print("Vehicle started")

class Car(Vehicle):  # ลูกคนที่ 1
    def drive(self):
        print("Car is driving")

class Bike(Vehicle):  # ลูกคนที่ 2
    def ride(self):
        print("Bike is riding")

class Boat(Vehicle):  # ลูกคนที่ 3
    def sail(self):
        print("Boat is sailing")

car = Car()
car.start()   # Output: Vehicle started
car.drive()   # Output: Car is driving

bike = Bike()
bike.start()  # Output: Vehicle started
bike.ride()   # Output: Bike is riding
```

**โครงสร้าง:**
```
      Vehicle
     ↙   ↓   ↘
  Car  Bike  Boat
```

#### 5. Hybrid Inheritance (การสืบทอดแบบผสม)
>การผสมผสานหลายประเภทของการสืบทอดเข้าด้วยกัน

```python
class University:
    def institution(self):
        print("Educational Institution")

class Department(University):  # Multilevel
    def dept_name(self):
        print("Computer Science")

class Student:
    def role(self):
        print("Student")

class Teacher:
    def role(self):
        print("Teacher")

class TeachingAssistant(Student, Teacher, Department):  # Multiple + Hierarchical
    def duty(self):
        print("Assisting in teaching")

ta = TeachingAssistant()
ta.institution()  # Output: Educational Institution
ta.dept_name()    # Output: Computer Science
ta.duty()         # Output: Assisting in teaching
```

**โครงสร้าง:**
```
    University
        ↓
   Department    Student  Teacher
          ↘        ↓       ↙
        TeachingAssistant
```

**สรุปความแตกต่าง:**

| ประเภท | จำนวนแม่ | จำนวนลูก | ตัวอย่าง |
|--------|----------|----------|---------|
| Single | 1 แม่ | 1 ลูก | Animal → Dog |
| Multiple | หลายแม่ | 1 ลูก | Father, Mother → Child |
| Multilevel | 1 แม่ต่อ 1 ลูก (ต่อกันหลายชั้น) | 1 ลูก | Grandparent → Parent → Child |
| Hierarchical | 1 แม่ | หลายลูก | Vehicle → Car, Bike, Boat |
| Hybrid | ผสมผสาน | ผสมผสาน | การรวมหลายแบบเข้าด้วยกัน |

---

## 4. Polymorphism (การมีหลายรูปแบบ)
>ความสามารถของวัตถุในการตอบสนองต่อฟังก์ชันเดียวกันในรูปแบบที่แตกต่างกัน

### ตัวอย่าง Polymorphism แบบต่างๆ

**ฟังก์ชัน len()**
```python
# ฟังก์ชัน len() ทำงานกับ type ต่างๆ ได้
print(len("Hello"))         # Output: 5 (String - นับตัวอักษร)
print(len([1, 2, 3]))       # Output: 3 (List - นับสมาชิก)
print(len({"a": 1, "b": 2})) # Output: 2 (Dictionary - นับคู่ Key-Value)
```

**Polymorphism with Class Methods (Method Overriding)**
- คือการที่ Child Class เขียนทับเมธอด
ที่ได้รับมาจาก Parent Class
```python
class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof! Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

class Bird(Animal):
    def sound(self):
        return "Tweet! Tweet!"

# การใช้ Polymorphism
animals = [Dog(), Cat(), Bird()]

for animal in animals:
    print(animal.sound())  # เมธอดเดียวกัน แต่ผลต่างกัน

# Output:
# Woof! Woof!
# Meow!
# Tweet! Tweet!
```

---

## 📚 สรุป
### 4 หลักการของ OOP

| หลักการ | จุดประสงค์ | ตัวอย่างการใช้งาน |
|---------|-----------|-------------------|
| **Encapsulation** | ห่อหุ้มข้อมูล ควบคุมการเข้าถึง | Private attributes, Getter/Setter |
| **Abstraction** | ซ่อนรายละเอียด แสดงเฉพาะที่จำเป็น | Abstract classes, Private methods |
| **Inheritance** | สืบทอดคุณสมบัติ นำโค้ดมาใช้ซ้ำ | Parent-Child relationship |
| **Polymorphism** | เมธอดเดียว ทำงานหลายรูปแบบ | Method overriding |

---