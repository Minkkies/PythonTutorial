# 10. Python Modules & Packages (โมดูลและแพคเกจ)

## Module คืออะไร?
> **Module** คือไฟล์ Python (`.py`) ที่มีโค้ด Python ซึ่งสามารถนำเข้า (import) และใช้งานในโปรแกรมอื่น ๆ ได้  
> โมดูล อาจมีฟังก์ชัน คลาส ตัวแปร และโค้ด executable

ประโยชน์ของโมดูล:
- **ซ้ำใช้ได้ (Reusability)**: เขียนโค้ดครั้งเดียว ใช้ได้หลายครั้ง
- **จัดระเบียบ (Organization)**: แบ่งโค้ดเป็นส่วนเล็กๆ ที่จัดการได้ง่าย
- **ป้องกันชื่อซ้ำ (Namespace)**: หลีกเลี่ยงการชนกันของชื่อตัวแปร/ฟังก์ชัน

## Import - วิธีการนำเข้าโมดูล

### วิธีที่ 1: Import whole module
```python
import math
print(math.pi)      # 3.14159...
print(math.sqrt(16))  # 4.0
```

### วิธีที่ 2: Import specific items
```python
from math import pi, sqrt
print(pi)           # 3.14159...
print(sqrt(16))     # 4.0
# ไม่ต้องใช้ math.
```

### วิธีที่ 3: Import with alias
```python
import numpy as np
from collections import defaultdict as dd

# ใช้ชื่อย่อง่าย
arr = np.array([1, 2, 3])
counter = dd(int)
```

### วิธีที่ 4: Import all (ไม่ค่อยแนะนำ)
```python
from math import *
print(pi)           # ทำงานแต่ไม่ชัดเจนว่ามาจากไหน
# ⚠️ อาจทำให้เกิด naming conflict
```

## Package คืออะไร?
> **Package** คือโฟลเดอร์ที่มีไฟล์ Python modules และไฟล์พิเศษชื่อ `__init__.py`  
> แบ่งโมดูลแบบลำดับชั้น (hierarchical)

โครงสร้าง:
```
my_package/
├── __init__.py
├── module1.py
├── module2.py
└── sub_package/
    ├── __init__.py
    └── module3.py
```

### ไฟล์ `__init__.py`
> ไฟล์พิเศษที่ทำให้ Python รู้ว่าโฟลเดอร์นี้เป็น package

**ประโยชน์:**
1. **บอก Python ว่านี่คือ package** (ใน Python 3.3+ ไม่จำเป็นแต่แนะนำให้มี)
2. **กำหนดว่าจะ export อะไรเมื่อใช้ `from package import *`**
3. **รันโค้ดเริ่มต้นเมื่อ import package**

```python
# my_package/__init__.py

# ว่างเปล่า - แค่บอกว่าเป็น package
```

หรือมีเนื้อหา:
```python
# my_package/__init__.py

# Import และ expose functions จาก modules
from .module1 import function_a
from .module2 import function_b

# กำหนด __all__ สำหรับ from package import *
__all__ = ['function_a', 'function_b']

# ตัวแปรของ package
VERSION = "1.0.0"

# โค้ดเริ่มต้น
print(f"Loading my_package v{VERSION}")
```

### Import จาก Package
```python
# Import module จาก package
from my_package import module1
from my_package.sub_package import module3

# Import ฟังก์ชันที่ exposed ใน __init__.py
from my_package import function_a, function_b

# ใช้ฟังก์ชัน
module1.my_function()
module3.another_function()
function_a()  # เรียกได้เลยไม่ต้องระบุ module
```

## สร้าง Custom Module 
### ตัวอย่าง: สร้าง `calculator.py`
```python
# calculator.py

def add(a, b):
    """บวกเลขสองตัว"""
    return a + b

def subtract(a, b):
    """ลบเลขสองตัว"""
    return a - b

def multiply(a, b):
    """คูณเลขสองตัว"""
    return a * b

PI = 3.14159

class SimpleCalc:
    """เครื่องคิดเลขอย่างง่าย"""
    
    def __init__(self):
        self.result = 0
    
    def calculate(self, a, b, op):
        if op == '+':
            self.result = add(a, b)
        elif op == '-':
            self.result = subtract(a, b)
        return self.result
```

### ใช้ Custom Module
```python
# main.py

import calculator

# ใช้ฟังก์ชัน
print(calculator.add(5, 3))       # 8
print(calculator.multiply(4, 5))  # 20

# ใช้ค่าคงที่
print(calculator.PI)              # 3.14159

# ใช้คลาส
calc = calculator.SimpleCalc()
print(calc.calculate(10, 3, '+')) # 13
```

หรือใช้ from import:
```python
from calculator import add, multiply, PI

print(add(5, 3))        # 8
print(PI)               # 3.14159
```

## Virtual Environment

**Virtual Environment** คือสภาพแวดล้อม Python แยกเพื่อจัดการ packages อิสระจากระบบหลัก

### สร้าง venv
```bash
# Windows
python -m venv venv_name

# Linux/Mac
python3 -m venv venv_name
```

### เปิดใช้ venv
```bash
# Windows
venv_name\Scripts\activate

# Linux/Mac
source venv_name/bin/activate

# ตรวจสอบว่าเปิดใช้หรือไม่ (ชื่อ venv อยู่ในหน้า prompt)
# (venv_name) PS C:\project>
```

## ตัวอย่างจริงจากโครงการ: week5/lab

โครงการนี้ใช้โครงสร้าง **Package** ที่มี sub-package โดยเรียบง่าย:

### โครงสร้างโครงการ
```
week5/lab/
    main.py                    # ไฟล์หลัก
    my_tools/                  # Package หลัก
        __init__.py           # ทำให้โฟลเดอร์เป็น package
        calculator.py         # Module: ฟังก์ชันพื้นฐาน
        module_test.py        # Module: ฟังก์ชันและ if __name__
        shapes/               # Sub-package
            __init__.py
            circle.py         # Module: คำนวณพื้นที่วงกลม
```

### ไฟล์ my_tools/calculator.py
```python
def add(a, b):
    return a + b
```

### ไฟล์ my_tools/module_test.py
```python
def greeting(name):
    return f'สวัสดี, {name}'

print('บรรทัดนี้จะทำงานเสมอ ไม่ว่าจะ Run หรือ Import')

if __name__ == '__main__':
    print('>>> ส่วนนี้จะทำงานเฉพาะตอนที่ Run ไฟล์นี้โดยตรง <<<')
    print(greeting('สมชาย'))
```

### ไฟล์ my_tools/shapes/circle.py
```python
import math

def get_area(radius):
    return math.pi * (radius ** 2)
```

### ไฟล์หลัก main.py
```python
# วิธีที่ 1: Import เต็มชื่อ
import my_tools.shapes.circle as circle_tool

# วิธีที่ 2: Import จาก module
import my_tools.module_test as test

# ใช้งาน
area = circle_tool.get_area(7)
print(f'พื้นที่วงกลม: {area:.2f}')

message = test.greeting('kd')
print(message)
```

### วิธีรัน
```bash
# ต้องอยู่ในโฟลเดอร์ week5/lab/
python main.py

# Output:
# บรรทัดนี้จะทำงานเสมอ ไม่ว่าจะ Run หรือ Import
# พื้นที่วงกลม: 153.94
# สวัสดี, kd
```

### Key Points จากตัวอย่างนี้
1. **Package structure**: โครงสร้างแบบซ้อนระดับ (shapes เป็น sub-package ของ my_tools)
2. **Import patterns**: 
   - `import my_tools.shapes.circle as circle_tool` (ชัดเจน)
   - `import my_tools.module_test as test` (alias สั้น)
3. **if __name__ == '__main__'**: จะทำงานเมื่อ module_test.py ถูกรันโดยตรง แต่ไม่ทำงานเมื่อถูก import
4. **Side effects**: โค้ดที่วิ่งเมื่อ import (`print('บรรทัดนี้...')`) จะรันทุกครั้งที่ import

---

## `if __name__ == '__main__'` (อธิบายเพิ่มเติม)

### ทำไมต้องใช้?
เมื่อ Python รันไฟล์ จะตั้งค่าตัวแปรพิเศษ `__name__`:
- ถ้า**รันไฟล์โดยตรง**: `__name__ == '__main__'`
- ถ้า**import ไฟล์**: `__name__ == 'ชื่อโมดูล'`

### ตัวอย่างการใช้งาน

```python
# utils.py

def add(a, b):
    """ฟังก์ชันบวกเลข"""
    return a + b

def subtract(a, b):
    """ฟังก์ชันลบเลข"""
    return a - b

# โค้ดส่วนนี้รันเฉพาะตอน python utils.py
if __name__ == '__main__':
    # Testing/Demo code
    print("Testing utils module:")
    print(f"add(5, 3) = {add(5, 3)}")
    print(f"subtract(10, 4) = {subtract(10, 4)}")
```

**เมื่อรัน `python utils.py`:**
```
Testing utils module:
add(5, 3) = 8
subtract(10, 4) = 6
```

**เมื่อ import:**
```python
# main.py
import utils

result = utils.add(10, 20)  # ทำงานปกติ
# ส่วน if __name__ == '__main__' ใน utils.py ไม่ทำงาน
```

### Use Cases ที่พบบ่อย
1. **Testing** - ทดสอบฟังก์ชันในโมดูล
2. **Demo** - แสดงตัวอย่างการใช้งาน
3. **CLI Script** - รันเป็น command line tool
4. **Development** - debug code ระหว่างพัฒนา

---

## Module Search Path (`sys.path`)

เมื่อ import module, Python จะค้นหาตามลำดับใน `sys.path`:

```python
import sys

# ดู search path
print(sys.path)
# [
#   '',  # โฟลเดอร์ปัจจุบัน
#   'C:\\Python39\\lib',  # Standard library
#   'C:\\Python39\\lib\\site-packages',  # Installed packages
#   ...
# ]
```

### เพิ่ม Path แบบชั่วคราว
```python
import sys

# เพิ่ม custom path
sys.path.append('C:/my_modules')

# ตอนนี้ import ได้จาก C:/my_modules
import my_custom_module
```

### ปัญหาที่พบบ่อย: ModuleNotFoundError

```python
# ❌ ผิด - module ไม่อยู่ใน sys.path
import my_module  # ModuleNotFoundError

# ✅ ถูก - เพิ่ม path หรือย้ายไฟล์มาที่ถูกต้อง
```

**วิธีแก้:**
1. วางไฟล์ module ในโฟลเดอร์เดียวกับ script
2. เพิ่ม path ด้วย `sys.path.append()`
3. ติดตั้ง module เป็น package (`pip install`)

---

## Built-in Modules ที่ควรรู้จัก

### 1. `os` - ระบบปฏิบัติการ
```python
import os

os.getcwd()              # โฟลเดอร์ปัจจุบัน
os.listdir('.')          # ไฟล์ในโฟลเดอร์
os.path.exists('file.txt')  # ตรวจสอบไฟล์
os.mkdir('new_folder')   # สร้างโฟลเดอร์
```

### 2. `sys` - ระบบและ interpreter
```python
import sys

sys.version              # Python version
sys.argv                 # Command line arguments
sys.path                 # Module search paths
sys.exit()               # ออกจากโปรแกรม
```

### 3. `datetime` - วันเวลา
```python
from datetime import datetime, timedelta

now = datetime.now()
print(now.strftime('%Y-%m-%d'))
tomorrow = now + timedelta(days=1)
```

### 4. `json` - จัดการ JSON
```python
import json

data = {'name': 'Alice', 'age': 25}
json_str = json.dumps(data)  # dict → JSON string
data_back = json.loads(json_str)  # JSON string → dict
```

### 5. `random` - สุ่มตัวเลข
```python
import random

random.randint(1, 10)     # สุ่ม 1-10
random.choice([1, 2, 3])  # เลือกสุ่มจาก list
random.shuffle([1, 2, 3]) # สลับลำดับ
```

### 6. `re` - Regular Expressions
```python
import re

text = "Email: user@example.com"
match = re.search(r'(\w+)@(\w+\.\w+)', text)
if match:
    print(match.group())  # user@example.com
```

### 7. `collections` - โครงสร้างข้อมูลพิเศษ
```python
from collections import defaultdict, Counter

# defaultdict - มี default value
word_count = defaultdict(int)
word_count['hello'] += 1

# Counter - นับความถี่
words = ['a', 'b', 'a', 'c', 'a', 'b']
count = Counter(words)  # Counter({'a': 3, 'b': 2, 'c': 1})
```

### 8. `pathlib` - จัดการ path (สมัยใหม่)
```python
from pathlib import Path

path = Path('data/file.txt')
path.exists()            # ตรวจสอบ
path.read_text()         # อ่านไฟล์
path.parent              # โฟลเดอร์แม่
```

## ตารางเปรียบเทียบรูปแบบการ Import

| ประเภท       | ชื่อเรียก       | รูปแบบคำสั่ง                       | คำอธิบาย                                                           | ตัวอย่างการใช้งาน                 |
| ------------ | --------------- | ---------------------------------- | ------------------------------------------------------------------ | --------------------------------- |
| แบบพื้นฐาน   | Basic Import    | `import math`                      | นำเข้าทั้งโมดูล เวลาใช้งานต้องอ้างชื่อโมดูลเต็ม ช่วยป้องกันชื่อซ้ำ | `math.sqrt(16)`                   |
| ตั้งชื่อเล่น | Aliasing        | `import pandas as pd`              | ตั้งชื่อย่อให้เรียกง่ายขึ้น นิยมใช้กับไลบรารีชื่อยาว               | `pd.read_csv("data.csv")`         |
| หลายโมดูล    | Multiple Import | `import os, sys, time`             | นำเข้าหลายโมดูลในบรรทัดเดียว โดยใช้จุลภาค ( , ) คั่น               | `os.getcwd()`                     |
| ระบุเจาะจง   | Specific Import | `from sklearn import linear_model` | ดึงเฉพาะส่วนที่ต้องการมาใช้งาน ทำให้โค้ดกระชับและชัดเจน            | `linear_model.LinearRegression()` |
