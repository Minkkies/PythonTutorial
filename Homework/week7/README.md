# Homework Week7 (Lab 8)

สรุปแบบฝึกหัดในโฟลเดอร์นี้ พร้อมแนวคิดและวิธีรันตัวอย่าง

## โครงสร้างไฟล์
- Assignment 8.pdf — โจทย์และข้อกำหนดของงาน
- lab8-Q1.py — คลาสจำลองแบตเตอรี่โทรศัพท์ (Encapsulation, getter)
- lab8-Q2.py — คลาสบัญชีเงินฝากออมทรัพย์ (Inheritance, protected attribute, class attribute)

## สาระสำคัญ
### lab8-Q1: PhoneBattery
- มี private attribute `__percent` เริ่มต้นที่ 100
- เมธอด `use_battery(amount)` ลดเปอร์เซ็นต์ ไม่ต่ำกว่า 0
- เมธอด `charge_battery(amount)` เพิ่มเปอร์เซ็นต์ ไม่เกิน 100
- เมธอด `get_percent()` สำหรับอ่านค่าเปอร์เซ็นต์ (getter)
- ตัวอย่างทดสอบครอบคลุมกรณีปกติและกรณีใส่ค่ามาก/น้อยเกินขอบเขต

### lab8-Q2: SavingsAccount
- คลาสแม่ `BankAccount` มี `_balance` (protected), เมธอด `deposit`, `withdraw`, `get_balance`
- คลาสลูก `SavingsAccount` สืบทอด `BankAccount` และมี `interest_rate` (class attribute)
- เมธอด `add_interest()` คำนวณดอกเบี้ยจาก `_balance` แล้วบวกกลับ
- ตัวอย่างทดสอบ: ฝากเงิน → คิดดอกเบี้ย → ถอนเงิน

## วิธีรันตัวอย่าง
เปิดเทอร์มินัลที่โฟลเดอร์นี้แล้วรันไฟล์ที่ต้องการ
```
python lab8-Q1.py
python lab8-Q2.py
```