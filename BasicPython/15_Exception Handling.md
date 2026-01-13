# 15. Exception Handling (การจัดการข้อผิดพลาด)

## Introduction

Exception Handling คือกระบวนการจัดการข้อผิดพลาด (Error) ที่เกิดขึ้นระหว่างที่โปรแกรมกำลังทำงาน (Runtime) แทนที่จะปล่อยให้โปรแกรม "Crash" หรือหยุดทำงานทันที การจัดการข้อผิดพลาดที่ดีจะช่วยให้โปรแกรมของเราไม่หยุดทำงานอย่างกะทันหัน และสามารถแจ้งข้อผิดพลาดให้ผู้ใช้ทราบได้อย่างเหมาะสม

## Types of Errors

### 1. Syntax Errors (ข้อผิดพลาดทางไวยากรณ์)
เกิดจากการเขียนโค้ดที่ไม่ถูกต้องตามกฎของภาษา Python

```python
# ตัวอย่าง Syntax Error
# ลืมวงเล็บปิด
print("Hello World"

# หรือลืม : หลัง if
if 5 > 3

print("Greater")
# ผลลัพธ์: SyntaxError
```
ต้องแก้ที่ตัวโค้ด (Source Code) เท่านั้นไม่สามารถใช้คำสั่งดักจับได้

### 2. Exceptions (ข้อผิดพลาดระหว่างรันโปรแกรม)
เกิดขึ้นขณะที่โปรแกรมกำลังทำงาน แม้ว่าโค้ดจะถูกต้องตามไวยากรณ์

```python
# ตัวอย่าง Exception
print(10 / 0)  # ZeroDivisionError: division by zero
```

## Common Built-in Exceptions

| Exception | คำอธิบาย |
|-----------|----------|
| `ValueError` | ค่าที่ส่งเข้าฟังก์ชันไม่เหมาะสม |
| `TypeError` | ชนิดข้อมูลไม่ถูกต้อง |
| `ZeroDivisionError` | หารด้วยศูนย์ |
| `NameError` | ชื่อตัวแปรยังไม่ได้ประกาศหรือไม่มีอยู่จริง |
| `IndexError` | เข้าถึง index ที่ไม่มีในลิสต์ |
| `KeyError` | เข้าถึง key ที่ไม่มีใน dictionary |
| `FileNotFoundError` | ไม่พบไฟล์ |
| `AttributeError` | เข้าถึง attribute ที่ไม่มี |
| `ImportError` | พบโมดูล แต่ไม่สามารถ Import ค่าหรือฟังก์ชันที่ต้องการออกมาได้ |
| `IndentationError` | การย่อหน้าของโค้ดไม่ถูกต้อง |
| `ModuleNotFoundError` | ไม่พบโมดูลที่พยายามจะ import |
| `OverflowError` | ผลลัพธ์ทางคณิตศาสตร์มีค่าใหญ่เกินขีดจำกัด (มักเกิดกับ Float) |
| `TabError` | ใช้การเว้นวรรคแบบ Tab ผสมกับ Space ปนกันในการย่อหน้า |

## Try-Except Block

### Basic Syntax

```python
try:
    # โค้ดที่อาจเกิดข้อผิดพลาด
    risky_operation()
except ExceptionType:
    # โค้ดที่จะทำงานเมื่อเกิดข้อผิดพลาด
    handle_error()
```

### ตัวอย่างพื้นฐาน

```python
try:
    number = int(input("กรุณาใส่ตัวเลข: "))
    result = 100 / number
    print(f"ผลลัพธ์: {result}")
except ValueError:
    print("❌ กรุณาใส่เฉพาะตัวเลขเท่านั้น")
except ZeroDivisionError:
    print("❌ ไม่สามารถหารด้วยศูนย์ได้")
```

## Multiple Exceptions

### จับหลาย Exception แยกกัน

```python
try:
    file = open("data.txt", "r")
    content = file.read()
    value = int(content)
except FileNotFoundError:
    print("ไม่พบไฟล์")
except ValueError:
    print("ข้อมูลในไฟล์ไม่ใช่ตัวเลข")
except IOError:
    print("เกิดข้อผิดพลาดในการอ่านไฟล์")
```

### จับหลาย Exception พร้อมกัน

```python
try:
    x = int(input("ใส่ตัวเลข: "))
    result = 10 / x
except (ValueError, ZeroDivisionError) as e:
    print(f"เกิดข้อผิดพลาด: {e}")
```

## Try-Except-Else

`else` block จะทำงานเมื่อไม่เกิด exception ใน try block

```python
try:
    age = int(input("ใส่อายุของคุณ: "))
except ValueError:
    print("กรุณาใส่ตัวเลข")
else:
    print(f"อายุของคุณคือ {age} ปี")
    if age >= 18:
        print("คุณบรรลุนิติภาวะแล้ว")
```

## Try-Except-Finally

`finally` block จะทำงานเสมอ ไม่ว่าจะเกิด exception หรือไม่

```python
try:
    file = open("data.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("ไม่พบไฟล์")
finally:
    try:
        file.close()
        print("ปิดไฟล์แล้ว")
    except:
        print("ไม่มีไฟล์ให้ปิด")
```

### ตัวอย่างการใช้ Finally ทำความสะอาด

```python
def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("ไม่สามารถหารด้วยศูนย์")
        return None
    except TypeError:
        print("กรุณาใส่ตัวเลข")
        return None
    else:
        print(f"ผลลัพธ์: {result}")
        return result
    finally:
        print("การคำนวณเสร็จสิ้น")

# ทดสอบ
divide_numbers(10, 2)   # ทำงานปกติ
divide_numbers(10, 0)   # เกิด ZeroDivisionError
divide_numbers(10, "a") # เกิด TypeError
```

## Raise Exception

เราสามารถสร้าง exception ขึ้นเองได้ด้วยคำสั่ง `raise`

```python
def check_age(age):
    if age < 0:
        raise ValueError("อายุต้องไม่ติดลบ") # raise สั่งให้ Error ตามเงื่อนไข
    if age > 150:
        raise ValueError("อายุสูงเกินไป")
    return True

try:
    check_age(-5)
except ValueError as e:
    print(f"ข้อผิดพลาด: {e}")
```

## Assert Statement

`assert` ใช้สำหรับตรวจสอบเงื่อนไขที่ควรเป็นจริงเสมอ มักใช้ในการ debug

```python
def calculate_average(numbers):
    assert len(numbers) > 0, "ลิสต์ต้องมีข้อมูลอย่างน้อย 1 ตัว"
    return sum(numbers) / len(numbers)

# ทำงานปกติ
print(calculate_average([1, 2, 3, 4, 5]))  # 3.0

# เกิด AssertionError
try:
    print(calculate_average([]))
except AssertionError as e:
    print(f"Assertion Error: {e}")
```

## Best Practices

### ✅ ควรทำ

```python
# 1. จับ exception ที่เฉพาะเจาะจง
try:
    number = int(input("ใส่ตัวเลข: "))
except ValueError:
    print("กรุณาใส่ตัวเลข")

# 2. ใช้ else สำหรับโค้ดที่ไม่ควรอยู่ใน try
try:
    file = open("data.txt", "r")
except FileNotFoundError:
    print("ไม่พบไฟล์")
else:
    data = file.read()
    file.close()

# 3. ใช้ finally สำหรับทำความสะอาด
try:
    resource = acquire_resource()
    process(resource)
finally:
    release_resource(resource)

# 4. แสดงข้อความที่เป็นประโยชน์
except FileNotFoundError as e:
    print(f"ไม่พบไฟล์: {e.filename}")
```

## Context Manager (with statement)

Context manager จัดการ resource อัตโนมัติ เหมาะสำหรับไฟล์และการเชื่อมต่อ

```python
# แทนที่จะเขียนแบบนี้
try:
    file = open("data.txt", "r")
    content = file.read()
finally:
    file.close()

# ใช้ with statement (แนะนำ)
with open("data.txt", "r") as file:
    content = file.read()
# ไฟล์จะถูกปิดอัตโนมัติ
```

### สร้าง Context Manager เอง

```python
class DatabaseConnection:
    def __enter__(self):
        print("เปิดการเชื่อมต่อฐานข้อมูล")
        self.connection = "Connected"
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("ปิดการเชื่อมต่อฐานข้อมูล")
        self.connection = None
        if exc_type is not None:
            print(f"เกิดข้อผิดพลาด: {exc_type.__name__}")
        return False  # propagate exception

# การใช้งาน
with DatabaseConnection() as db:
    print(f"สถานะ: {db.connection}")
    # ทำงานกับฐานข้อมูล
```

## Summary

### สิ่งที่ควรจำ

1. **ใช้ try-except** เพื่อจัดการข้อผิดพลาดที่คาดการณ์ได้
2. **จับ exception ที่เฉพาะเจาะจง** อย่าใช้ `except Exception:` หรือ `except:` แบบกว้างๆ
3. **ใช้ else block** สำหรับโค้ดที่ควรทำงานเมื่อไม่มี exception
4. **ใช้ finally block** สำหรับการทำความสะอาด resource