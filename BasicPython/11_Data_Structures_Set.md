# 11. Set (เซต)

> **Set** คือโครงสร้างข้อมูลที่เก็บข้อมูลที่ไม่ซ้ำกัน ไม่มีลำดับ และเป็น **mutable** เหมาะสำหรับการหาค่าที่ไม่ซ้ำและการดำเนินการทางคณิตศาสตร์

## คุณสมบัติหลักของ Set

1. **ไม่มีลำดับ (Unordered)**: ไม่มี index, ลำดับไม่แน่นอน
2. **ไม่ซ้ำ (Unique Elements)**: ค่าซ้ำจะถูกเก็บแค่ครั้งเดียว
3. **แก้ไขได้ (Mutable)**: เพิ่ม/ลบสมาชิกได้ แต่สมาชิกต้อง immutable
    - สมาชิกภายในต้องเป็นชนิดคงที่เช่น String, Number, Tuple(ห้าม List)
4. **เร็ว**: การค้นหาและตรวจสอบการมีอยู่เร็วกว่า list

## การสร้าง Set
1. ใช้ Curley Braces {}
- ใส่สมาชิกทั้งหมดไว้ใน{} และคั่นด้วยเครื่องหมาย , (จุลภาค)
- Set สามารถมีสมาชิกได้หลายรายการและหลายชนิดข้อมูล เช่น integer, float, string, หรือ Tuple
- Set ไม่สามารถมีสมาชิกที่เป็นชนิดข้อมูลที่เปลี่ยนแปลงได้ (mutable) อย่าง List, Set, หรือ Dictionary ได้
```python
# ใช้ curly braces {}
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 4, 5}

# Set ว่าง - ต้องใช้ set() (ไม่ใช้ {} เพราะจะเป็น dict)
empty = set()

# จาก list (ลบค่าซ้ำอัตโนมัติ)
nums = set([1, 2, 2, 3, 3, 4])       # {1, 2, 3, 4}

# จาก string
chars = set("hello")                 # {'h', 'e', 'l', 'o'} - ลบ 'l' ซ้ำ

# Set comprehension
squares = {x**2 for x in range(5)}   # {0, 1, 4, 9, 16}
```

---

## Set Methods

### การเพิ่มและลบ
```python
fruits = {"apple", "banana"}

# add() เพิ่มสมาชิกเพียงตัวเดียว
fruits.add("cherry")                 # {'apple', 'banana', 'cherry'}
fruits.add("apple")                  # ไม่เปลี่ยน (มีอยู่แล้ว)

# update() เพิ่มสมาชิกหลายตัว (ที่ไม่ซ้ากัน) จาก Iterable อื่น
fruits.update(["date", "elderberry"])  # เพิ่มจาก iterable
# {'date', 'apple', 'cherry', 'banana', 'elderberry'}
fruits.update({1, 2}, [3, 4])        # เพิ่มได้หลาย iterable
# {1, 2, 3, 4, 'date', 'apple', 'cherry', 'banana', 'elderberry'}

# ลบสมาชิก
fruits.remove("banana")              # ❌ KeyError ถ้าไม่มี
fruits.discard("banana")             # ✅ ไม่ error ถ้าไม่มี
item = fruits.pop()                  # ลบและคืนค่าสมาชิกสุ่ม Error ถ้า Set ว่าง
fruits.clear()                       # ลบทั้งหมด
```

### การตรวจสอบ
```python
fruits = {"apple", "banana", "cherry"}

# ตรวจสอบสมาชิก
"apple" in fruits                    # True
"grape" not in fruits                # True

# ความยาว
len(fruits)                          # 3
```

---

## Set Operations (การดำเนินการทางคณิตศาสตร์)

```python
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

# Union (รวม) - ค่าที่อยู่ใน a หรือ b
a.union(b)                           # {1, 2, 3, 4, 5, 6, 7, 8}
a | b                                # เหมือนกัน

# Intersection (ซ้ำกัน) - ค่าที่อยู่ทั้ง a และ b
a.intersection(b)                    # {4, 5}
a & b                                # เหมือนกัน

# Difference (ส่วนต่าง) - ค่าที่อยู่ใน a แต่ไม่อยู่ใน b
a.difference(b)                      # {1, 2, 3}
a - b                                # เหมือนกัน

# Symmetric Difference (ไม่ซ้ำกัน) - ค่าที่อยู่ใน a หรือ b แต่ไม่ทั้งคู่
a.symmetric_difference(b)            # {1, 2, 3, 6, 7, 8}
a ^ b                                # เหมือนกัน

# Subset/Superset
{1, 2}.issubset({1, 2, 3})          # True (1,2 เป็น subset ของ 1,2,3)
{1, 2, 3}.issuperset({1, 2})        # True (1,2,3 เป็น superset ของ 1,2)
{1, 2}.isdisjoint({3, 4})           # True (ไม่มีสมาชิกร่วม)
```

### Update Methods (แก้ไข set เดิม)
```python
a = {1, 2, 3}
b = {3, 4, 5}

a.update(b)                          # a = {1, 2, 3, 4, 5}
a |= b                               # เหมือนกัน

a.intersection_update(b)             # a = ค่าร่วม
a &= b                               # เหมือนกัน

a.difference_update(b)               # a = ค่าที่ไม่ซ้ำ
a -= b                               # เหมือนกัน

a.symmetric_difference_update(b)     # a = ค่าที่ไม่ร่วม
a ^= b                               # เหมือนกัน
```

---

## Frozenset (Set ที่แก้ไขไม่ได้)

```python
# Frozenset - immutable set
fs = frozenset([1, 2, 3, 4])
# fs.add(5)                          # ❌ AttributeError

# ใช้เป็น key ใน dict หรือสมาชิกใน set ได้
d = {frozenset([1, 2]): "value"}   # ✅
s = {frozenset([1, 2]), frozenset([3, 4])}  # ✅

# การดำเนินการได้ปกติ
fs1 = frozenset([1, 2, 3])
fs2 = frozenset([2, 3, 4])
print(fs1 | fs2)                     # frozenset({1, 2, 3, 4})
print(fs1 & fs2)                     # frozenset({2, 3})
```

## Common Mistakes (ข้อผิดพลาดทั่วไป)

### ❌ Mistake 1: สร้าง set ว่างด้วย {}
```python
# ❌ ผิด - {} เป็น dict ไม่ใช่ set
empty = {}
print(type(empty))  # <class 'dict'>

# ✅ ถูก - ใช้ set()
empty = set()
print(type(empty))  # <class 'set'>
```

### ❌ Mistake 2: เพิ่ม list หรือ dict ใน set
```python
# ❌ ผิด - list/dict ไม่ใช่ immutable
my_set = {[1, 2], [3, 4]}  # TypeError: unhashable type: 'list'
my_set = {{"a": 1}}        # TypeError: unhashable type: 'dict'

# ✅ ถูก - ใช้ tuple หรือ frozenset
my_set = {(1, 2), (3, 4)}  # ✅
my_set = {frozenset([1, 2])}  # ✅
```

### ❌ Mistake 3: คาดหวังลำดับที่แน่นอน
```python
# ❌ ผิด - set ไม่มีลำดับ
my_set = {3, 1, 2}
print(my_set[0])  # TypeError: 'set' object is not subscriptable

# ✅ ถูก - แปลงเป็น list ก่อน (แต่ลำดับไม่การันตี)
my_list = list(my_set)
# หรือเรียง
sorted_list = sorted(my_set)  # [1, 2, 3]
```

### ❌ Mistake 4: ใช้ remove() แทน discard()
```python
my_set = {1, 2, 3}

# ❌ อันตราย - KeyError ถ้าไม่มี
my_set.remove(5)  # KeyError: 5

# ✅ ปลอดภัย - ไม่ error ถ้าไม่มี
my_set.discard(5)  # ไม่เกิดอะไร
```

---

## Best Practices (แนวทางปฏิบัติที่ดี)

✅ **ควรทำ:**
- ใช้ set เมื่อต้องการหาค่าที่ไม่ซ้ำ (เร็วกว่า list)
- ใช้ set สำหรับการตรวจสอบ membership (`in`) เร็วกว่า list มาก
- ใช้ set operations (union, intersection) แทน loop เมื่อเป็นไปได้
- ใช้ `discard()` แทน `remove()` เพื่อหลีกเลี่ยง KeyError

```python
# ✅ ดี - ใช้ set สำหรับ membership test
allowed_users = {"alice", "bob", "charlie"}  # O(1) lookup
if username in allowed_users:  # รวดเร็ว
    grant_access()

# ❌ ไม่ดี - ใช้ list
allowed_users = ["alice", "bob", "charlie"]  # O(n) lookup
if username in allowed_users:  # ช้ากว่า
    grant_access()

# ✅ ดี - ใช้ set operations
common = set1 & set2

# ❌ ไม่ดี - loop
common = []
for item in set1:
    if item in set2:
        common.append(item)
```

❌ **ไม่ควรทำ:**
- ไม่ใช้ set เมื่อต้องการรักษาลำดับ (ใช้ list หรือ dict)
- ไม่ลืมว่า set elements ต้อง immutable
- ไม่พึ่งพาลำดับของ set

```python
# ❌ ไม่ดี - ใช้ set เมื่อต้องการลำดับ
items = {3, 1, 2}  # ลำดับไม่แน่นอน

# ✅ ดี - ใช้ list หรือ sorted list
items = [3, 1, 2]  # รักษาลำดับ
items = sorted({3, 1, 2})  # [1, 2, 3]
```

---

## Set vs List: เลือกใช้อย่างไร?

| คุณสมบัติ | Set | List |
|-----------|-----|------|
| **ลำดับ** | ❌ ไม่มี | ✅ มี |
| **ค่าซ้ำ** | ❌ ไม่ได้ | ✅ ได้ |
| **Indexing** | ❌ ไม่ได้ | ✅ ได้ |
| **Membership test** | ⚡ O(1) เร็ว | 🐌 O(n) ช้า |
| **Use case** | หาค่าไม่ซ้ำ, set operations | เก็บข้อมูลตามลำดับ |

**ใช้ Set เมื่อ:**
- ต้องการเก็บค่าที่ไม่ซ้ำ
- ต้องการตรวจสอบ membership บ่อย ๆ
- ต้องการทำ mathematical operations (union, intersection, etc.)
- ไม่สนใจลำดับ

**ใช้ List เมื่อ:**
- ต้องการรักษาลำดับ
- ต้องการ indexing/slicing
- ยอมรับค่าซ้ำได้
- ต้องการ append/insert ตามตำแหน่ง