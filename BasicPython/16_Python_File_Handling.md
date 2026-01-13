# 16. Python File Handling (การจัดการไฟล์)

## Introduction

File Handling คือการทำงานกับไฟล์ใน Python ซึ่งเป็นทักษะสำคัญในการเขียนโปรแกรม เพราะเราต้องมีการอ่าน เขียน และจัดการข้อมูลจากไฟล์ต่างๆ เช่น text files, CSV, JSON และอื่นๆ การจัดการไฟล์ที่ดีจะช่วยให้โปรแกรมของเราสามารถเก็บข้อมูล ประมวลผล และแชร์ข้อมูลได้อย่างมีประสิทธิภาพ

## File Operations

การทำงานกับไฟล์มี 4 ขั้นตอนหลัก:
1. **เปิดไฟล์** (Open) - เปิดไฟล์เพื่อเข้าถึงข้อมูล
2. **อ่าน/เขียนข้อมูล** (Read/Write) - ดำเนินการกับข้อมูลในไฟล์
3. **ปิดไฟล์** (Close) - ปิดไฟล์เพื่อปล่อย resource
4. **จัดการข้อผิดพลาด** (Handle Exceptions) - จัดการกับสถานการณ์ที่ไม่คาดคิด

## 1. Opening Files

### Syntax พื้นฐาน

```python
file = open(filename, mode, encoding)
```
- filename: ชื่อไฟล์หรือ path ของไฟล์
- mode: รูปแบบการเปิด (อ่าน/เขียน)
- encoding: การเข้ารหัสภาษา (แนะนำ utf-8 สำหรับภาษาไทย)

### โหมดการเปิดไฟล์ (File Modes)

| Mode | คำอธิบาย | การทำงาน |
|------|----------|----------|
| `'r'` | Read (อ่าน) | เปิดไฟล์เพื่ออ่าน (default) ไฟล์ต้องมีอยู่แล้ว หากไม่พบไฟล์จะเกิด FileNotFoundError |
| `'w'` | Write (เขียน) | เปิดไฟล์เพื่อเขียน สร้างไฟล์ใหม่หรือเขียนทับไฟล์เดิม |
| `'a'` | Append (เพิ่มต่อท้าย) | เปิดไฟล์เพื่อเขียนต่อท้าย สร้างไฟล์ใหม่ถ้ายังไม่มี |
| `'x'` | Exclusive creation | สร้างไฟล์ใหม่ ถ้าไฟล์มีอยู่แล้วจะ error |
| `'r+'` | Read + Write | เปิดไฟล์เพื่ออ่านและเขียน |
| `'w+'` | Write + Read | เปิดไฟล์เพื่อเขียนและอ่าน (เขียนทับ) |
| `'a+'` | Append + Read | เปิดไฟล์เพื่อเพิ่มข้อมูลและอ่าน |
| `'rt'` | Read text | อ่านไฟล์แบบตัวอักษร |
| `'rb'` | Read Binary | อ่านไฟล์แบบ binary |
| `'wb'` | Write Binary | เขียนไฟล์แบบ binary |

### ตัวอย่างการเปิดไฟล์

```python
# เปิดไฟล์เพื่ออ่าน
file = open("data.txt", "r", encoding="utf-8")

# เปิดไฟล์เพื่อเขียน
file = open("output.txt", "w", encoding="utf-8")

# เปิดไฟล์เพื่อเพิ่มข้อมูล
file = open("log.txt", "a", encoding="utf-8")
```

## 2.Reading Files

### read() - อ่านทั้งไฟล์

```python
# อ่านเนื้อหาทั้งหมด
file = open("data.txt", "r", encoding="utf-8")
content = file.read()
print(content)
file.close() # หลังใช้งานเสร็จต้องปิดไฟล์เสมอ
```
<span style ="color:red;"><b>ข้อควรระวัง: </b></span>ถ้าไฟล์ไม่มีอยู่จริง โปรแกรมจะหยุดทำงานและแจ้งเตือนFileNotFoundError

### read(size) - อ่านจำนวนตัวอักษรที่กำหนด

```python
file = open("data.txt", "r", encoding="utf-8")
content = file.read(100)  # อ่าน 100 ตัวอักษรแรก
print(content)
file.close()
```

### readline() - อ่านทีละบรรทัด

```python
file = open("data.txt", "r", encoding="utf-8")
line1 = file.readline()  # อ่านบรรทัดแรก
line2 = file.readline()  # อ่านบรรทัดที่สอง
print(line1)
print(line2)
file.close()
```

### readlines() - อ่านทุกบรรทัดเป็น List

```python
file = open("data.txt", "r", encoding="utf-8")
lines = file.readlines()  # ได้ list ของแต่ละบรรทัด
for line in lines:
    print(line.strip())  # strip() เอา \n ออก
file.close()
```

<h4 style="font-size:20px;">สรุป:</h4>

| วิธี | ผลลัพธ์ | รายละเอียด |
|------|---------|-----------|
| `for line in file:` | string (ทีละบรรทัด) | วนอ่านทีละบรรทัด |
| `file.readline()` | string (1 บรรทัด) | อ่าน 1 บรรทัด |
| `file.readlines()` | **list** of strings | อ่านทั้งหมดเป็น list |
| `file.read()` | string (ทั้งหมด) | อ่านทั้งไฟล์เป็น string เดียว |
>ดังนั้น: มีเพียง `readlines()` เท่านั้นที่ได้ list ส่วนที่เหลือได้ string ทั้งหมด

### Loop through file - วนอ่านทีละบรรทัด (แนะนำ)

```python
file = open("data.txt", "r", encoding="utf-8")
for line in file:
    print(line.strip())
file.close()
```

## 3. Writing Files

### write() - เขียนข้อความ

```python
file = open("output.txt", "w", encoding="utf-8")
file.write("Hello World\n") #Cursor เริ่มต้นที่ตำแหน่งแรก
file.write("Python File Handling\n")
file.close()
```
<span style ="color:orange;"><b>คำเตือนสำคัญ: </b></span>หากไฟล์มีอยู่แล้ว ข้อมูลเดิมจะถูกลบทิ้งทั้งหมด (Overwritten) และ write() ไม่เติม \n (ขึ้นบรรทัดใหม่) ให้ เราต้องใส่เอง

### writelines() - เขียนหลายบรรทัด

```python
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
file = open("output.txt", "w", encoding="utf-8")
file.writelines(lines)
file.close()
```

### Append Mode - เพิ่มข้อมูลต่อท้าย

```python
file = open("log.txt", "a", encoding="utf-8")
file.write("New log entry\n")
file.close()
```

## 4. Closing Files

การปิดไฟล์เป็นสิ่งสำคัญเพื่อปล่อย resource และป้องกันการสูญหายของข้อมูล

### การปิดไฟล์แบบ Manual

```python
file = open("data.txt", "r", encoding="utf-8")
content = file.read()
file.close()  # ต้องปิดไฟล์เสมอ
```

**ปัญหา:** ถ้าเกิด error ก่อนถึง `file.close()` ไฟล์จะไม่ถูกปิด

### การปิดไฟล์แบบปลอดภัย (with statement)

```python
# แนะนำ - ไฟล์จะถูกปิดอัตโนมัติ
with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()
# ไฟล์ถูกปิดอัตโนมัติแม้เกิด error
```

## The with Statement (Context Manager)

`with` statement เป็นวิธีที่ดีที่สุดในการจัดการไฟล์ เพราะจะปิดไฟล์อัตโนมัติแม้เกิดข้อผิดพลาด

### ตัวอย่างการใช้ seek() และ tell()

```python
with open("data.txt", "r", encoding="utf-8") as file:
    # อ่าน 10 ตัวอักษรแรก
    first_10 = file.read(10)
    print(f"ตำแหน่งปัจจุบัน: {file.tell()}")  # 10
    
    # กลับไปอ่านจากต้นไฟล์
    file.seek(0)
    all_content = file.read()
    
    # ไปที่ตำแหน่ง 20
    file.seek(20)
    from_20 = file.read()
```

## Checking Files and Directories

### ใช้ os module

```python
import os

# ตรวจสอบว่าไฟล์มีอยู่หรือไม่
if os.path.exists("data.txt"):
    print("✅ ไฟล์มีอยู่")
else:
    print("❌ ไม่พบไฟล์")

# ตรวจสอบว่าเป็นไฟล์หรือไม่
if os.path.isfile("data.txt"):
    print("เป็นไฟล์")

# ตรวจสอบว่าเป็น directory หรือไม่
if os.path.isdir("my_folder"):
    print("เป็น directory")

# ขนาดไฟล์
if os.path.exists("data.txt"):
    size = os.path.getsize("data.txt")
    print(f"ขนาดไฟล์: {size} bytes")
    print(f"ขนาดไฟล์: {size/1024:.2f} KB")

# ดูไฟล์ใน directory ปัจจุบัน
files = os.listdir(".")
print("ไฟล์ในโฟลเดอร์:")
for file in files:
    print(f"  - {file}")

# ดู path แบบเต็ม
current_dir = os.getcwd()
print(f"Directory ปัจจุบัน: {current_dir}")

# รวม path
file_path = os.path.join("folder", "subfolder", "file.txt")
print(file_path)  # folder/subfolder/file.txt (หรือ folder\subfolder\file.txt บน Windows)
```

### ใช้ pathlib module (แนะนำ - Python 3.4+)

```python
from pathlib import Path

# สร้าง Path object
file_path = Path("data.txt")
folder_path = Path("my_folder")

# ตรวจสอบว่ามีไฟล์หรือไม่
if file_path.exists():
    print("✅ ไฟล์มีอยู่")

# ตรวจสอบว่าเป็นไฟล์
if file_path.is_file():
    print("เป็นไฟล์")

# ตรวจสอบว่าเป็น directory
if folder_path.is_dir():
    print("เป็น directory")

# อ่านไฟล์ทั้งหมด
if file_path.exists():
    content = file_path.read_text(encoding="utf-8")
    print(content)

# เขียนไฟล์
file_path.write_text("Hello World", encoding="utf-8")

# ข้อมูลไฟล์
if file_path.exists():
    print(f"ชื่อไฟล์: {file_path.name}")
    print(f"นามสกุล: {file_path.suffix}")
    print(f"ชื่อไม่มีนามสกุล: {file_path.stem}")
    print(f"Parent directory: {file_path.parent}")
    print(f"ขนาด: {file_path.stat().st_size} bytes")

# รวม path
new_path = Path("folder") / "subfolder" / "file.txt"
print(new_path)

# ดูไฟล์ใน directory
folder = Path(".")
for item in folder.iterdir():
    if item.is_file():
        print(f"📄 {item.name}")
    elif item.is_dir():
        print(f"📁 {item.name}")

# หาไฟล์ตาม pattern
for py_file in folder.glob("*.py"):
    print(f"Python file: {py_file}")

# หาไฟล์แบบ recursive
for txt_file in folder.rglob("*.txt"):
    print(f"Text file: {txt_file}")
```

### Syntax

```python
with open(filename, mode, encoding) as file:
    # ทำงานกับไฟล์
    content = file.read()
# ไฟล์ถูกปิดอัตโนมัติที่นี่
```

### ตัวอย่างการใช้งาน

```python
# อ่านไฟล์
with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)

# เขียนไฟล์
with open("output.txt", "w", encoding="utf-8") as file:
    file.write("Hello World\n")
    file.write("Python is awesome!\n")

# เพิ่มข้อมูลท้ายไฟล์
with open("log.txt", "a", encoding="utf-8") as file:
    file.write("New log entry\n")
```

### ทำงานกับหลายไฟล์พร้อมกัน

```python
# คัดลอกเนื้อหาจากไฟล์หนึ่งไปอีกไฟล์
with open("source.txt", "r", encoding="utf-8") as source, \
     open("destination.txt", "w", encoding="utf-8") as dest:
    content = source.read()
    dest.write(content)

# อ่าน 2 ไฟล์และเปรียบเทียบ
with open("file1.txt", "r", encoding="utf-8") as f1, \
     open("file2.txt", "r", encoding="utf-8") as f2:
    content1 = f1.read()
    content2 = f2.read()
    if content1 == content2:
        print("ไฟล์เหมือนกัน")
    else:
        print("ไฟล์ต่างกัน")
```

## File Position and Seek

### tell() - บอกตำแหน่งปัจจุบัน

```python
with open("data.txt", "r") as file:
    print(file.tell())  # 0 (เริ่มต้น)
    file.read(10)
    print(file.tell())  # 10 (อ่านไป 10 ตัวอักษร)
```

### seek(offset, whence) - ย้ายตำแหน่งอ่าน/เขียน

```python
with open("data.txt", "r") as file:
    file.seek(0)    # ไปที่ตำแหน่งเริ่มต้น
    file.seek(10)   # ไปที่ตำแหน่ง 10
    file.seek(0, 2) # ไปที่ท้ายไฟล์
```

**whence values:**
- `0` - จากต้นไฟล์ (default)
- `1` - จากตำแหน่งปัจจุบัน
- `2` - จากท้ายไฟล์

## Summary

### สิ่งที่ควรจำ

1. **ใช้ with statement** เพื่อจัดการไฟล์อัตโนมัติ
2. **ระบุ encoding="utf-8"** สำหรับภาษาไทย
3. **จัดการข้อผิดพลาด** ด้วย try-except
4. **เลือก mode ที่เหมาะสม** (`r`, `w`, `a`, `r+`)
5. **ใช้ pathlib** สำหรับการทำงานกับ path
6. **ปิดไฟล์เสมอ** หรือใช้ with statement
7. **ระวังเรื่อง encoding** โดยเฉพาะกับภาษาไทย