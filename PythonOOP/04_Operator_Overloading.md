# Operator Overloading

## 1. Introduction to Operator Overloading

**Operator Overloading** (การสร้างตัวดำเนินการใหม่) คือการกำหนดให้ operator (เช่น `+`, `-`, `*`, `/`, `==`, `>`) ทำงานกับ class ที่เราสร้างขึ้นเอง

ตัวอย่างเช่น:
```python
# โดยปกติ + ใช้กับตัวเลข
print(5 + 3)  # Output: 8

# แต่ถ้าเรา overload + ในคลาส Vector ก็สามารถนำ vectors มาบวกกันได้
v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2  # (4, 6)
```
**ความสัมพันธ์กับ Polymorphism**
>Polymorphism คือความสามารถในการใช้เมธอดหรือ operator เดียวกันกับ object หลายๆ ประเภทได้
- Operator Overloading เป็นตัวอย่างหนึ่งของ Polymorphism เพราะเราสามารถใช้ operator เดียวกันกับ object หลายๆ ประเภทได้ (เช่น ตัวเลข, สตริง, หรือคลาสที่เราสร้างเอง)

### Special Methods(Dunder Methods)

Python ใช้ **magic methods** (special methods) ในการ implement operator overloading

Magic methods มีชื่อที่เริ่มต้นและสิ้นสุดด้วย double underscore `__method__`
ตัวอย่างเช่น:
- `__init__` สำหรับการสร้าง object
- `__add__` สำหรับ operator `+`
- `__sub__` สำหรับ operator `-`

## 2. Arithmetic Operators

### Arithmetic Magic Methods

| Operator | Method | ตัวอย่าง |
|----------|--------|---------|
| `+` | `__add__` | `a + b` |
| `-` | `__sub__` | `a - b` |
| `*` | `__mul__` | `a * b` |
| `/` | `__truediv__` | `a / b` |
| `//` | `__floordiv__` | `a // b` |
| `%` | `__mod__` | `a % b` |
| `**` | `__pow__` | `a ** b` |

### ตัวอย่าง: Vector Addition (จุดพิกัด)

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # กำหนดการทำงานของ + operator
    def __add__(self, other):
        """บวก vectors ทั้งสองตัว"""
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    
    # กำหนดการทำงานของ - operator
    def __sub__(self, other):
        """ลบ vectors"""
        x = self.x - other.x
        y = self.y - other.y
        return Vector(x, y)
    
    # กำหนดการทำงานของ * operator (scalar multiplication)
    def __mul__(self, scalar):
        """คูณ vector ด้วยตัวเลข"""
        return Vector(self.x * scalar, self.y * scalar)
    
    # แสดงผล vector
    def __repr__(self): 
        return f"Vector({self.x}, {self.y})"

# การใช้งาน
v1 = Vector(1, 2)
v2 = Vector(3, 4)

print(v1 + v2)      # Vector(4, 6)
print(v1 - v2)      # Vector(-2, -2)
print(v1 * 2)       # Vector(2, 4)
```

### Reverse Operators

ถ้าต้องการให้ scalar อยู่ด้านซ้าย (เช่น `2 * v1` แทน `v1 * 2`) ใช้ `__rmul__`

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __mul__(self, scalar):
        """v * 2"""
        return Vector(self.x * scalar, self.y * scalar)
    
    def __rmul__(self, scalar):
        """2 * v"""
        return Vector(self.x * scalar, self.y * scalar)
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v = Vector(1, 2)
print(v * 2)    # Vector(2, 4)
print(2 * v)    # Vector(2, 4)
```

## 3. Comparison Operators

### Comparison Magic Methods

| Operator | Method | ตัวอย่าง |
|----------|--------|---------|
| `==` | `__eq__` | `a == b` |
| `!=` | `__ne__` | `a != b` |
| `<` | `__lt__` | `a < b` |
| `<=` | `__le__` | `a <= b` |
| `>` | `__gt__` | `a > b` |
| `>=` | `__ge__` | `a >= b` |

### ตัวอย่าง: Student Comparison

```python
class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
    
    # เปรียบเทียบตามคะแนน GPA
    def __eq__(self, other):
        """ตรวจสอบว่า GPA เท่ากันหรือไม่"""
        return self.gpa == other.gpa
    
    def __lt__(self, other):
        """ตรวจสอบว่า GPA ต่ำกว่า"""
        return self.gpa < other.gpa
    
    def __le__(self, other):
        """ตรวจสอบว่า GPA ต่ำกว่าหรือเท่า"""
        return self.gpa <= other.gpa
    
    def __gt__(self, other):
        """ตรวจสอบว่า GPA สูงกว่า"""
        return self.gpa > other.gpa
    
    def __ge__(self, other):
        """ตรวจสอบว่า GPA สูงกว่าหรือเท่า"""
        return self.gpa >= other.gpa
    
    def __repr__(self):
        return f"Student({self.name}, {self.gpa})"

# การใช้งาน
s1 = Student("Alice", 3.8)
s2 = Student("Bob", 3.5)
s3 = Student("Charlie", 3.8)

print(s1 == s3)  # True (GPA เท่ากัน)
print(s1 > s2)   # True (Alice มี GPA สูงกว่า Bob)
print(s2 < s1)   # True
```

## 4. String Representation Methods

### `__str__` vs `__repr__`

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        """ส่วนดีต่อผู้ใช้งาน - สำหรับการแสดงผล"""
        return f"{self.name} is {self.age} years old"
    
    def __repr__(self):
        """สำหรับผู้พัฒนา - เหมือนโค้ด Python"""
        return f"Person('{self.name}', {self.age})"

p = Person("Alice", 25)
print(str(p))   # Alice is 25 years old
print(repr(p))  # Person('Alice', 25)
```

### `__len__` - กำหนดความยาว

```python
class MyList:
    def __init__(self, items):
        self.items = items
    
    def __len__(self):
        """คืนจำนวนสมาชิก"""
        return len(self.items)
    
    def __repr__(self):
        return f"MyList({self.items})"

my_list = MyList([1, 2, 3, 4, 5])
print(len(my_list))  # 5
```

### `__getitem__` - เข้าถึงสมาชิกด้วย index

```python
class MyList:
    def __init__(self, items):
        self.items = items
    
    def __getitem__(self, index):
        """เข้าถึงสมาชิกด้วย [] operator"""
        return self.items[index]
    
    def __setitem__(self, index, value):
        """กำหนดค่าสมาชิก"""
        self.items[index] = value

my_list = MyList([10, 20, 30])
print(my_list[0])      # 10
my_list[1] = 25
print(my_list[1])      # 25
```

## 5. Practical Example - Complex Number

```python
class Complex:
    def __init__(self, real, imag=0):
        self.real = real
        self.imag = imag
    
    def __add__(self, other):
        """บวกจำนวนเชิงซ้อน"""
        return Complex(
            self.real + other.real,
            self.imag + other.imag
        )
    
    def __sub__(self, other):
        """ลบจำนวนเชิงซ้อน"""
        return Complex(
            self.real - other.real,
            self.imag - other.imag
        )
    
    def __mul__(self, other):
        """คูณจำนวนเชิงซ้อน (a+bi)(c+di) = (ac-bd) + (ad+bc)i"""
        return Complex(
            self.real * other.real - self.imag * other.imag,
            self.real * other.imag + self.imag * other.real
        )
    
    def __eq__(self, other):
        """เปรียบเทียบจำนวนเชิงซ้อน"""
        return self.real == other.real and self.imag == other.imag
    
    def __str__(self):
        if self.imag >= 0:
            return f"{self.real}+{self.imag}i"
        else:
            return f"{self.real}{self.imag}i"
    
    def __repr__(self):
        return f"Complex({self.real}, {self.imag})"

# การใช้งาน
c1 = Complex(3, 4)
c2 = Complex(1, 2)

print(c1 + c2)  # 4+6i
print(c1 - c2)  # 2+2i
print(c1 * c2)  # -5+10i
print(c1 == c2) # False
```

## 6. Container Emulation

การทำให้คลาสมีพฤติกรรมเหมือน list, dict

```python
class Shelf:
    """คลาสที่ทำให้เหมือน list"""
    def __init__(self):
        self.books = []
    
    def __len__(self):
        """จำนวนหนังสือ"""
        return len(self.books)
    
    def __getitem__(self, index):
        """เอาหนังสือ"""
        return self.books[index]
    
    def __setitem__(self, index, book):
        """วางหนังสือ"""
        self.books[index] = book
    
    def __contains__(self, book):
        """ตรวจสอบว่ามีหนังสือ (in operator)"""
        return book in self.books
    
    def add(self, book):
        """เพิ่มหนังสือ"""
        self.books.append(book)
    
    def __repr__(self):
        return f"Shelf({self.books})"

# การใช้งาน
shelf = Shelf()
shelf.add("Python 101")
shelf.add("OOP Guide")

print(len(shelf))                    # 2
print(shelf[0])                      # Python 101
print("Python 101" in shelf)         # True
```

## 7. Callable Objects - `__call__`

ทำให้ object สามารถเรียกแบบฟังก์ชั่นได้

```python
class Multiplier:
    """คลาสที่สามารถเรียกแบบฟังก์ชัน"""
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, x):
        """กำหนดการทำงานเมื่อเรียกแบบ object(x)"""
        return x * self.factor

times3 = Multiplier(3)
print(times3(5))   # 15 (เรียก times3 เหมือนฟังก์ชัน)
print(times3(10))  # 30
```

## Summary

**Operator Overloading คือการ:**
- ใช้ magic methods (`__method__`) ในการ implement operators
- ทำให้ class สามารถใช้งาน operators ธรรมชาติ
- เพิ่มความสัญชาตญาณและอ่านได้ง่ายขึ้น

**Common Magic Methods:**
- Arithmetic: `__add__`, `__sub__`, `__mul__`, `__truediv__`
- Comparison: `__eq__`, `__lt__`, `__le__`, `__gt__`, `__ge__`
- String: `__str__`, `__repr__`
- Container: `__len__`, `__getitem__`, `__setitem__`, `__contains__`
- Callable: `__call__`