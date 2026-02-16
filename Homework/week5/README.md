# Week 5 - Python Functions & Modules

โฟลเดอร์นี้รวมแบบฝึกหัดเกี่ยวกับ Functions และ Modules ใน Python

## 📁 โครงสร้างไฟล์

```
week5/
├── lab5_q1.py              # Variable Arguments (*args)
├── lab5_q2.py              # Keyword Arguments (**kwargs)
├── lab5_q3.py              # Recursive Function
├── lab/                    # Module & Package Practice
│   ├── main.py
│   └── my_tools/
│       ├── calculator.py
│       ├── module_test.py
│       └── shapes/
│           └── circle.py
├── lab6_q1/                # Text Utilities Module
│   ├── main.py
│   └── text_utils.py
├── lab6_q2/                # E-commerce Package
│   ├── main.py
│   └── ecommerce/
│       └── cart.py
└── lab6_q3/                # Unit Converter Module
    ├── main.py
    └── converter.py
```

---

## 📝 Lab 5: Advanced Function Parameters

### **Lab 5.1 - Variable Arguments (_*args_)**
**ไฟล์:** [lab5_q1.py](lab5_q1.py)

**คำอธิบาย:** ฟังก์ชันคำนวณสถิติพื้นฐาน (ผลรวม, ค่าเฉลี่ย, ค่าสูงสุด, ค่าต่ำสุด)

### **Lab 5.2 - Keyword Arguments (_**kwargs_)**
**ไฟล์:** [lab5_q2.py](lab5_q2.py)

**คำอธิบาย:** ฟังก์ชันคำนวณราคาสินค้าหลังหักส่วนลดและเพิ่มภาษี

### **Lab 5.3 - Recursive Function**
**ไฟล์:** [lab5_q3.py](lab5_q3.py)

**คำอธิบาย:** คำนวณเลขยกกำลังโดยใช้ Recursion

## 📦 Lab 6: Modules & Packages

### **Lab 6.1 - Text Utilities Module**
**โฟลเดอร์:** [lab6_q1/](lab6_q1/)

**คำอธิบาย:** Module สำหรับจัดการข้อความ

**ไฟล์:**
- `main.py` - โปรแกรมหลัก
- `text_utils.py` - Module ที่มีฟังก์ชัน count_words, reverse_text, capitalize_words

### **Lab 6.2 - E-commerce Cart Package**
**โฟลเดอร์:** [lab6_q2/](lab6_q2/)

**คำอธิบาย:** Package จัดการตะกร้าสินค้า

**ไฟล์:**
- `main.py` - โปรแกรมทดสอบ
- `ecommerce/__init__.py` - Package initializer
- `ecommerce/cart.py` - ShoppingCart class

### **Lab 6.3 - Unit Converter Module**
**โฟลเดอร์:** [lab6_q3/](lab6_q3/)

**คำอธิบาย:** Module แปลงหน่วย

**ไฟล์:**
- `main.py` - โปรแกรมทดสอบ
- `converter.py` - ฟังก์ชันแปลงหน่วยอุณหภูมิและระยะทาง

## 🎯 สิ่งที่ได้เรียนรู้

### Lab 5 - Function Parameters
- ✅ `*args` - Variable length arguments (Tuple)
- ✅ `**kwargs` - Keyword arguments (Dictionary)
- ✅ Default parameters
- ✅ Recursion
- ✅ Docstrings

### Lab 6 - Modules & Packages
- ✅ การสร้าง Module
- ✅ การสร้าง Package (โฟลเดอร์ + `__init__.py`)
- ✅ การ import
- ✅ `if __name__ == "__main__":` pattern

---

## 📚 กฎสำคัญ

1. **Parameter Order:** พารามิเตอร์ปกติ → default parameters → `*args` → `**kwargs`
   ```python
   def func(a, b, c=10, *args, **kwargs):
       pass
   ```

2. **`return` หยุดฟังก์ชันทันที** - โค้ดหลัง return ไม่ทำงาน

3. **Python Package ต้องมี `__init__.py`** - แม้ว่าจะเป็นไฟล์ว่างก็ตาม

4. **Docstring Format:** ใช้ Google Style หรือ NumPy Style เพื่อให้ IDE แสดง parameter description