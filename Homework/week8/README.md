# Web Scraping Lab - Quotes Scraper

## 📖 Lab Overview

บทเรียนการเขียนโปรแกรม Python เพื่อดึงข้อมูลจากเว็บไซต์ (Web Scraping) โดยใช้ไลบรารี **Requests** และ **BeautifulSoup**

## 🎯 Objectives

นักเรียนหลังเรียนเสร็จจะสามารถ:
1. ✅ ส่งคำขอ HTTP ไปยัง URL ด้วย `requests`
2. ✅ แยกวิเคราะห์ (parse) โค้ด HTML ด้วย `BeautifulSoup`
3. ✅ ค้นหาและดึงข้อมูลเฉพาะจากเว็บ
4. ✅ จัดการข้อมูล (cleaning) และเก็บเข้า DataFrame
5. ✅ บันทึกข้อมูลเป็นไฟล์ CSV

---

## 🚀 Getting Started

### Prerequisites
```bash
pip install requests beautifulsoup4 pandas
```

### Files in This Project
- **test.ipynb** - Jupyter Notebook บรรยายขั้นตอนการดึงข้อมูลทีละขั้น
- **quotes.csv** - ผลลัพธ์ที่บันทึกเป็น CSV (คำคม + ผู้เขียน)

---

## 📝 Lab Tasks

### Task 1: Requests - ส่งคำขอ HTTPm
```python
import requests

url = "https://quotes.toscrape.com/"
response = requests.get(url)
print(response.status_code)  # ควรได้ 200 = สำเร็จ
```

**จุดประสงค์:** เข้าใจ HTTP status codes และวิธีส่งคำขอ

---

### Task 2: BeautifulSoup - Parse HTML
```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify())  # ดูโครงสร้าง HTML
```

**จุดประสงค์:** เข้าใจ DOM Tree และโครงสร้าง HTML

---

### Task 3: Find Elements - ค้นหาข้อมูล
```python
# หาทุกคำคม
quotes = soup.find_all(class_='text')
print(f"พบคำคม {len(quotes)} ประโยค")

# หาผู้เขียน
authors = soup.find_all(class_='author')
print(f"พบผู้เขียน {len(authors)} คน")
```

**จุดประสงค์:** ใช้ CSS selectors เพื่อหา elements

---

### Task 4: Extract Data - ดึงข้อมูล
```python
quotes_list = [quote.text.strip() for quote in quotes]
authors_list = [author.text.strip() for author in authors]

print(f"คำคมแรก: {quotes_list[0]}")
print(f"ผู้เขียนแรก: {authors_list[0]}")
```

**จุดประสงค์:** แปลง BeautifulSoup objects เป็น list ที่ใช้งานได้

---

### Task 5: Save to CSV - บันทึกข้อมูล
```python
import pandas as pd

data = {
    'คำคม': quotes_list,
    'ผู้เขียน': authors_list
}

df = pd.DataFrame(data)
df.to_csv('quotes.csv', index=False, encoding='utf-8-sig')
print("บันทึก CSV เสร็จเรียบร้อย!")
```

**จุดประสงค์:** ใช้ Pandas บันทึกข้อมูลเป็นไฟล์

---

## 📊 Expected Output

| คำคม | ผู้เขียน |
|------|--------|
| "The world as we have created it..." | Albert Einstein |
| ""It is our choices, Harry..."" | J.K. Rowling |
| "There are only two ways to live..." | Albert Einstein |

---

## 🔍 Code Walkthrough

### Step-by-step Process

```
1. Requests Library
   ↓ ส่งคำขอ HTTP
   ↓ รับ HTML response

2. BeautifulSoup
   ↓ Parse HTML เป็น DOM Tree
   ↓ เพื่อที่จะค้นหา elements ได้

3. Find Elements
   ↓ ค้นหา <span class="text"> = คำคม
   ↓ ค้นหา <small class="author"> = ผู้เขียน

4. Clean Data
   ↓ ลบ whitespace (.strip())
   ↓ ใส่เข้า list

5. Save to CSV
   ↓ สร้าง DataFrame
   ↓ บันทึกเป็น CSV
```

---

## 💡 Key Concepts

### 1. HTTP Status Codes
- **200 OK** - สำเร็จ
- **404 Not Found** - ไม่พบ
- **403 Forbidden** - ห้ามเข้าถึง
- **500 Server Error** - เซิร์ฟเวอร์ผิดพลาด

### 2. CSS Selectors
```python
soup.find_all('tag')              # หาด้วย tag
soup.find_all(class_='name')      # หาด้วย class
soup.find_all(id='name')          # หาด้วย id
soup.select('.class-name')        # CSS selector
```

### 3. List Comprehension
```python
# แทนที่
quotes_list = []
for quote in quotes:
    quotes_list.append(quote.text)

# ด้วย
quotes_list = [quote.text for quote in quotes]
```

---

### Related Topics in BasicPython
- [17_Web_Scraping.md](../../BasicPython/17_Web_Scraping.md) - เนื้อหาเต็ม