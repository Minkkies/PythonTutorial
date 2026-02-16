# ABSTRACT CLASSES

## 1. Introduction to Abstract Classes
>Abstract Class (คลาสแบบนามธรรม) คือคลาสที่ถูกออกแบบมาเพื่อเป็น "แม่แบบ" หรือพิมพ์เขียว (Blueprint) ให้กับคลาสอื่น ๆ

Abstract Classes คือคลาสที่ไม่สามารถสร้าง instance ได้โดยตรง และมักจะมี abstract methods (เมธอดที่ไม่มีการ implement) ที่บังคับให้ subclass ต้อง override

**จุดประสงค์:**
- กำหนด template หรือ blueprint สำหรับ subclass
- บังคับให้ subclass implement เมธอดที่จำเป็น
- สร้าง interface ที่ชัดเจนสำหรับการ inheritance

### เมื่อไหร่ควรใช้ Abstract Class?

<span style="color:lightblue">**ใช้ Abstract Class เมื่อ:**</span>

1. **ต้องการบังคับให้ subclass implement เมธอดบางตัว**
   ```python
   # ทุก Payment Method ต้องมีวิธีการชำระเงิน
   class PaymentMethod(ABC):
       @abstractmethod
       def process_payment(self, amount):
           pass
   ```

2. **มี shared behavior ที่ subclass หลายตัวใช้ร่วมกัน**
   ```python
   # ทุก Shape มี method คำนวณพื้นที่เหมือนกัน แต่วิธีคำนวณต่างกัน
   class Shape(ABC):
       @abstractmethod
       def calculate_area(self):
           pass
   ```

3. **ต้องการสร้าง interface ที่ชัดเจน**
   ```python
   # กำหนดว่า Database ต้องมี connect, query, close
   class Database(ABC):
       @abstractmethod
       def connect(self): pass
       
       @abstractmethod
       def query(self, sql): pass
       
       @abstractmethod
       def close(self): pass
   ```

4. **ป้องกันการใช้คลาสผิดวัตถุประสงค์**
   - ไม่ต้องการให้สร้าง instance จากคลาสแม่
   - ต้องการให้ใช้ผ่าน subclass เท่านั้น

<span style="color:lightcoral">**ไม่ควรใช้ Abstract Class เมื่อ:**</span>
- คลาสแม่สามารถใช้งานได้โดยตรง (ไม่ใช่แค่ template)
- ไม่มีเมธอดที่ต้องบังคับให้ implement
- มี subclass เพียงตัวเดียว (อาจไม่คุ้มค่า)

## 2. Creating Abstract Classes

ใน Python เราใช้ module `abc` (Abstract Base Classes) ในการสร้าง abstract class

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass # ไม่มีการทำงานจริง
```

## 3. Abstract Methods

Abstract method คือเมธอดที่ประกาศไว้ใน abstract class แต่ไม่มี implementation

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        """บังคับให้สัตว์ทุกตัวต้องมีเสียง"""
        pass
```
**Concrete Class: Dog** สร้างคลาส Dog ที่สืบทอดจาก Animal และระบุการทำงานของ sound()
```python
# Dog คือ Concrete Class
# เพราะมีการ implement ครบทุกอย่าง
class Dog(Animal):
    def sound(self):
        return "Woof! Woof!"
```
**การสร้าง Object** เราสามารถสร้าง instance ของ Dog ได้ตามปกติ เพราะมันเป็น Concrete Class แล้ว
```python
dog = Dog()
print(dog.sound())

# Output
# Woof! Woof!
```

<span style="color:red">ข้อควรระวัง:</span> 
- ถ้าเราพยายามสร้าง instance ของ Animal โดยตรง จะเกิดข้อผิดพลาด TypeError
- ไม่สามารถสร้างอ็อบเจกต์จากคลาสที่มีสถานะเป็น Abstract ได้โดยตรง
- ถ้าคลาสลูก (Subclass) ไม่ยอม Implement abstract method ทุกตัวที่รับมาจากแม่ จะทำให้คลาสลูกนั้นกลายเป็น Abstract Class ไปด้วย และจะไม่สามารถสร้าง Object ได้เช่นกัน
```python
animal = Animal()  # TypeError: Can't instantiate abstract class Animal
```

## 4. Implementing Abstract Classes 

Subclass ต้อง implement abstract methods ทั้งหมดจึงจะสามารถสร้าง instance ได้

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# การใช้งาน
dog = Dog()
print(dog.make_sound())  # Output: Woof!

cat = Cat()
print(cat.make_sound())  # Output: Meow!

# ไม่สามารถสร้าง instance ของ Animal ได้
# animal = Animal()  # TypeError: Can't instantiate abstract class Animal
```

## 5. Combining Abstract and Concrete Methods

### ความแตกต่างระหว่าง Abstract Methods และ Concrete Methods

**Abstract Methods (เมธอดแบบนามธรรม)**
- เป็นเมธอดที่ **ประกาศไว้แต่ไม่มีการทำงานจริง** (ไม่มี implementation)
- ใช้ decorator `@abstractmethod` ในการประกาศ
- **บังคับให้ subclass ทุกตัวต้อง implement** (เขียนทับ) เมธอดนี้
- ถ้า subclass ไม่ implement จะไม่สามารถสร้าง instance ได้

**Concrete Methods (เมธอดแบบคอนกรีต)**
- เป็นเมธอดที่ **มีการทำงานจริงครบถ้วน** (มี implementation)
- ไม่ต้องใช้ decorator พิเศษ เขียนเหมือนเมธอดปกติ
- **ไม่บังคับให้ subclass ต้อง override** (แต่สามารถ override ได้ถ้าต้องการ)
- Subclass สามารถใช้เมธอดนี้ได้เลยโดยไม่ต้องเขียนใหม่

### ตัวอย่างการใช้งานร่วมกัน

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    # เมธอดแบบนามธรรม
    @abstractmethod
    def make_sound(self):
        pass

    # เมธอดแบบคอนกรีต
    def move(self):
        return "Moving"

class Dog(Animal):
    def make_sound(self):
        return "Bark"

dog = Dog()

# ใช้เมธอดแบบคอนกรีตจาก Animal
print(dog.move()) # Output: Moving
print(dog.make_sound()) # Output: Bark
```

## 6. Multiple Abstract Base Classes

Class สามารถ inherit จาก abstract class หลายตัวได้

```python
from abc import ABC, abstractmethod

class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass

class Swimmable(ABC):
    @abstractmethod
    def swim(self):
        pass

class Duck(Flyable, Swimmable):
    def fly(self):
        return "Duck is flying"
    
    def swim(self):
        return "Duck is swimming"

duck = Duck()
print(duck.fly())   # Duck is flying
print(duck.swim())  # Duck is swimming
```

## 7. Abstract Properties

นอกจาก abstract methods แล้ว ยังสามารถสร้าง abstract properties ได้

```python
from abc import ABC, abstractmethod

class Person(ABC):
    @property 
    @abstractmethod
    def name(self): # บังคับให้ลูกต้องมี property ชื่อ name
        pass
    
    @property
    @abstractmethod
    def age(self): # บังคับให้ลูกต้องมี property ชื่อ age
        pass

class Student(Person):
    def __init__(self, name, age, student_id):
        self._name = name
        self._age = age
        self.student_id = student_id
    
    # implement property name ถูกบังคับให้ต้องกำหนดค่า name ไม่งั้นจะสร้าง object ไม่ได้
    @property 
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age

student = Student("Alice", 20, "S001")
print(student.name)  # Alice
print(student.age)   # 20
```

## 8.1 Practical Example - รูปทรงเรขาคณิต
โจทย์: โปรแกรมคำนวณพื้นที่ (Area)
- รูปทรงทุกชนิดต้องมีพื้นที่
- แต่วิธีคำนวณพื้นที่ของแต่ละรูปทรงไม่เหมือนกัน (วงกลมใช้ Pi, สี่เหลี่ยมใช้ ด้าน*ด้าน)
- เราต้องการบังคับให้ทุกรูปทรงมี Property area

1. สร้าง Base Class: Shape
2. สร้างคลาส Circle 
3. สร้างคลาส Square
```python
from abc import ABC, abstractmethod

#1. Base Class
class Shape(ABC):
    @property # กำหนดให้ area เป็น property การเข้าถึงได้เหมือน attribute
    @abstractmethod 
    def area(self):
        pass

#2. Circle Class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

#3. Square Class
class Square(Shape):
    def __init__(self, side):
        self.side = side

    @property
    def area(self):
        return self.side ** 2

# การใช้งาน
shapes = [ Circle(5), Square(4) ]

for s in shapes:
    # Polymorphism: เรียกใช้ .area ได้เลย
    # โดยไม่ต้องสนว่าเป็นรูปทรงอะไร
    print(f"Area: {s.area:.2f}")

# Output:
# Area: 78.54
# Area: 16.00
```
## 8.2 Practical Example - Payment Gateway
โจทย์: ระบบ E-commerce ที่ต้องรองรับการจ่ายเงินหลายแบบ
- อาจจะใช้ Stripe, PayPal, หรือโอนเงินธนาคาร
- ระบบหลัก (Core System) ไม่ควรผูกติดกับเจ้าใดเจ้าหนึ่ง
- ต้องการ "มาตรฐานกลาง" ในการสั่งจ่ายเงิน

```python
from abc import ABC, abstractmethod

#1. Base Class:Abstract PaymentProcessor
class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass

#2. Concrete Class: StripePayment
class StripePayment(PaymentProcessor):
    def pay(self, amount):
        print(f"Paying ${amount} via Stripe API")

    def refund(self, amount):
        print("Refunding via Stripe...")

#3. Concrete Class: PayPalPayment
class PayPalPayment(PaymentProcessor):
    def pay(self, amount):
        print(f"Paying ${amount} via PayPal API")

    def refund(self, amount):
        print("Refunding via PayPal...")

# การใช้งาน
def process_transaction(processor, amount):
    # ไม่ว่าจะเป็น Stripe หรือ PayPal ก็ใช้คำสั่งเดียวกัน
    processor.pay(amount)

# เมื่อใช้งานจริง
stripe = StripePayment()
paypal = PayPalPayment()

process_transaction(stripe, 100) # Output: Paying $100 via Stripe API
process_transaction(paypal, 100) # Output: Paying $100 via PayPal API