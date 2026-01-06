# 10. Dictionary (ดิกชันนารี)

> **Dictionary** คือโครงสร้างข้อมูลแบบ key-value pairs ที่ใช้เก็บข้อมูลแบบจับคู่ เป็น **mutable** และเรียกข้อมูลได้เร็วด้วย key

## คุณสมบัติหลักของ Dictionary

1. **เก็บข้อมูลเป็นคู่ (Key-Value Pairs)**: แต่ละข้อมูลมี key และ value
2. **Key ต้องไม่ซ้ำ (Unique Keys)**: แต่ value ซ้ำได้
    - Key ต้องเป็นข้อมูลประเภท Immutable (เปลี่ยนแปลงไม่ได้) String, Integer, Tuple ใช้ได้
    ```py
    my_dict = {"apple": 1, 2: "two", (1, 2): "one two", } # ✅
    my_dict = {[1, 2]: "Hello Hi"} # ❌ จะเกิด TypeError: unhashable type: 'list'
    ```
    - หากมีการกำหนด Key ซ้ำกัน ค่าใหม่จะ เขียนทับ (Overwrite) ค่าเดิมทันที
    ```py
    my_dict = {
        "apple": 1, 
        2: "two", 
        (1, 2): "one two", 
        2: "test"
    }
    print(my_dict) # {'apple': 1, 2: 'test, (1, 2): 'one two'}
    ```
3. **แก้ไขได้ (Mutable)**: สามารถเพิ่ม ลบ แก้ไข key-value ได้
4. **Key ต้อง Immutable**: string, number, tuple (ไม่ใช้ list เป็น key)
5. **เรียงลำดับ (Ordered)** ตั้งแต่ Python 3.7+ (เก็บลำดับที่ insert)

## การสร้าง Dictionary

```python
# ใช้ curly braces {} ใส่คู่ key: value คั่นด้วยเครื่องหมาย ,
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}
print(student) # {"name": "Alice","age": 20,"grade": "A"}

# Dictionary ว่าง
empty = {}
empty2 = dict()

# ใช้ dict() constructor
person = dict(name="Bob", age=25, city="Bangkok")

# จาก list of tuples แก้ไขไม่ได้
pairs = [("a", 1), ("b", 2), ("c", 3)]
d = dict(pairs)                      # {'a': 1, 'b': 2, 'c': 3}

# Dictionary comprehension
squares = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Comprehension มี condition
evens = {x: x**2 for x in range(10) if x % 2 == 0}  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# Swap keys และ values
original = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in original.items()}  # {1: 'a', 2: 'b', 3: 'c'}

# fromkeys() - สร้างจาก keys (value เหมือนกันหมด)
keys = ["a", "b", "c"]
d = dict.fromkeys(keys, 0)           # {'a': 0, 'b': 0, 'c': 0}
```

---

## การเข้าถึงและแก้ไข
เนื่องจาก Dictionary จัดเก็บข้อมูลในรูปแบบ Key-Value pair จึงไม่สามารถใช้ดัชนีตัวเลขเหมือน List
หรือ Tuple ได้
```python
student = {"name": "Alice", "age": 20, "grade": "A"}

# เข้าถึงด้วย key
print(student["name"])               # 'Alice'
print(student["city"])               # ❌ KeyError ถ้าไม่มี key

# เข้าถึงด้วย เมธอด .get()
# รูปแบบ: dictionary_name.get(key, default_value)
print(student.get("age"))            # 20
print(student.get("city", "N/A"))    # 'N/A' (default ถ้าไม่มี key)
print(student.get("city"))           # ✅ คืน None ถ้าไม่มี key        

# แก้ไขค่า
student["age"] = 21                  # แก้ไข
student["city"] = "Bangkok"          # เพิ่มใหม่
print(student) # {'name': 'Alice', 'age': 21, 'grade': 'A', 'city': 'Bangkok'}

# Update หลาย key-value
student.update({"grade": "A+", "gpa": 4.0})
student.update(age=22, major="CS")   # ใช้ keyword arguments
print(student)
# {'name': 'Alice', 'age': 22, 'grade': 'A+', 'city': 'Bangkok', 'gpa': 4.0, 'major': 'CS'}
```

---

## Dictionary Methods

### การเพิ่มและลบ
```python
d = {"a": 1, "b": 2}

# เพิ่ม/แก้ไข
d["c"] = 3                           # {'a': 1, 'b': 2, 'c': 3}
d.setdefault("d", 4)                 # เพิ่มถ้ายังไม่มี, คืนค่า
d.setdefault("a", 10)                # มีอยู่แล้วไม่แก้, คืน 1

# ลบ
d.pop("b")                           # ลบและคืนค่า 2
d.pop("z", "Not found")              # คืน default ถ้าไม่มี key
d.popitem()                          # ลบและคืน (key, value) ตัวสุดท้าย
del d["a"]                           # ลบแบบไม่คืนค่า
d.clear()                            # ลบทั้งหมด {}
```

### การเข้าถึง Keys, Values, Items
```python
student = {"name": "Alice", "age": 20, "city": "Bangkok"}

# Keys
keys = student.keys()                # dict_keys(['name', 'age', 'city'])
list(student.keys())                 # ['name', 'age', 'city']

# Values
values = student.values()            # dict_values(['Alice', 20, 'Bangkok'])
list(student.values())               # ['Alice', 20, 'Bangkok']

# Items (key-value pairs)
items = student.items()              # dict_items([('name', 'Alice'), ...])
list(student.items())                # [('name', 'Alice'), ('age', 20), ...]

# การตรวจสอบ
"name" in student                    # True (ตรวจ key)
"Alice" not in student.values()          # False (ตรวจ value)
```

### การวนซ้ำ
```python
student = {"name": "Alice", "age": 20, "city": "Bangkok"}

# วน keys
for key in student:
    print(key, student[key]) # name Alice , age 20 ,city Bangkok

# วน key-value
for key, value in student.items():
    print(f"{key}: {value}") # name: Alice , age: 20 , city: Bangkok

# วน values
for value in student.values(): # Alice , 20 , Bangkok
    print(value)
```
การวนซ้ำด้วยเมธอด items(), keys(), และ values()
- ➢ items(): วนซ้ำเพื่อรับทั้ง Key และ Value ในรูปแบบ Tuple
- ➢ keys(): วนซ้ำเพื่อรับเฉพาะ Keys (เหมือนกับการวนลูปโดยตรง)
- ➢ values(): วนซ้ำเพื่อรับเฉพาะ Values

---

## ตัวอย่างการใช้งานจริง

```python
# นับความถี่
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
# {'apple': 3, 'banana': 2, 'cherry': 1}

# หรือใช้ Counter
from collections import Counter
freq = Counter(words)

# กลุ่มข้อมูล (grouping)
students = [
    {"name": "Alice", "grade": "A"},
    {"name": "Bob", "grade": "B"},
    {"name": "Charlie", "grade": "A"}
]
by_grade = {}
for s in students:
    grade = s["grade"]
    if grade not in by_grade:
        by_grade[grade] = []
    by_grade[grade].append(s["name"])
# {'A': ['Alice', 'Charlie'], 'B': ['Bob']}

# Merge dictionaries
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
merged = {**d1, **d2}                # {'a': 1, 'b': 3, 'c': 4}
# หรือ (Python 3.9+)
merged = d1 | d2

# Nested dictionary
company = {
    "employees": {
        "Alice": {"age": 25, "position": "Developer"},
        "Bob": {"age": 30, "position": "Manager"}
    }
}
print(company["employees"]["Alice"]["position"])  # 'Developer'
```

## Best Practices (แนวทางปฏิบัติที่ดี)

✅ **ควรทำ:**
- ใช้ `.get()` แทนการเข้าถึงด้วย `[]` เมื่อไม่แน่ใจว่ามี key
- ใช้ `defaultdict` จาก collections เมื่อต้องการ default value
- ใช้ dictionary comprehension สำหรับการสร้าง/กรอง dict
- ใช้ `.items()` เมื่อต้องการทั้ง key และ value

```python
# ✅ ดี - ใช้ get() กับ default
count = word_count.get(word, 0) + 1

# ✅ ดี - defaultdict
from collections import defaultdict
word_count = defaultdict(int)
word_count[word] += 1  # ไม่ต้องเช็คว่ามี key

# ✅ ดี - comprehension
squares = {x: x**2 for x in range(10)}
```

❌ **ไม่ควรทำ:**
- ไม่ใช้ list/dict เป็น key (ไม่ immutable)
- ไม่ลืม deep copy เมื่อมี nested structure
- ไม่แก้ไข dict ขณะวนซ้ำ

```python
# ❌ ไม่ดี - ใช้ list เป็น key
d = {[1, 2]: "value"}  # TypeError!

# ❌ ไม่ดี - ลืม check key ก่อนเข้าถึง
value = d["key_that_might_not_exist"]  # อาจ KeyError

# ❌ ไม่ดี - shallow copy nested dict
copy = original.copy()  # nested objects ยังอ้างอิงเดียวกัน
```