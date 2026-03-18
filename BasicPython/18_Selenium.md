# Selenium - Browser Automation for Web Scraping
## Introduction

Selenium คือเครื่องมือสำหรับ browser automation ที่จำลองการทำงานของผู้ใช้ เช่น คลิกปุ่ม, กรอกฟอร์ม, และเลื่อนหน้า

### เมื่อใช้ Selenium แทน BeautifulSoup?

**ใช้ BeautifulSoup เมื่อ:**
- เว็บไซต์เป็น Static (HTML ส่งมาครบในครั้งแรก)
- ต้องการความเร็ว
- ข้อมูลอยู่ใน HTML ส่วนแรก

**ใช้ Selenium เมื่อ:**
- เว็บไซต์เป็น Dynamic (ใช้ JavaScript และ AJAX โหลดข้อมูล)
- Real Simulation สํามํารถคลิกปุ่ม, เลื่อนหน้ําจอ, และกรอกฟอร์มได้เหมือนคนจริงๆ
- ข้อมูลปรากฏหลังจากการโต้ตอบ

## Installation

### 1. ติดตั้ง Selenium Library

```bash
pip install selenium
```
Note: อย่ําลืมตรวจสอบว่ํามีเบรําว์เซอร์ Chrome หรือ Firefox ติดตั้งอยู่ในเครื่องแล้ว

### 2. นำเข้าโมดูลและคลาสที่จำเป็น
```python
from selenium import webdriver # ใช้สำหรับควบคุมเบราว์เซอร์
from selenium.webdriver.common.by import By # ใช้สำหรับระบุวิธีการค้นหาองค์ประกอบ
from selenium.webdriver.common.keys import Keys # ใช้สำหรับส่งคีย์บอร์ดจำลองการกดปุ่มบนแป้นพิมพ์
from selenium.webdriver.support.ui import WebDriverWait # ใช้สำหรับรอให้เงื่อนไขเป็นจริง
from selenium.webdriver.support import expected_conditions as EC # ใช้สำหรับกำหนดเงื่อนไขที่ต้องรอ
```

### 3. การตั้งค่า WebDriver
Selenium ต้องใช้ WebDriver เพื่อควบคุมเบราว์เซอร์ เช่น ChromeDriver สำหรับ Google Chrome หรือ GeckoDriver สำหรับ Firefox
```python
chrome_options = webdriver.ChromeOptions()
# Add any desired options here, for example, headless mode:
driver = webdriver.Chrome(options=chrome_options)
```
อ็อบเจกต์chrome_options ใช้สำหรับกำหนดค่ําเบื้องต้นก่อนเปิดเบราว์เซอร์ เช่น ขนาดหน้าต่าง,โหมดการทำงาน หรือการปิดส่วนขยาย

#### โหมด Headless (ไร้หน้ําต่ําง)
```python
chrome_options.add_argument("--headless") # เปิดโหมด headless เพื่อไม่แสดงหน้าต่างเบราว์เซอร์
``` 
โหมด headless ช่วยให้การทำงานเร็วขึ้นและเหมาะสำหรับการรันในเซิร์ฟเวอร์หรือสภาพแวดล้อมที่ไม่มีหน้าจอ

#### การตั้งขนาดหน้าต่าง
```python
chrome_options.add_argument("--window-size=1920,1080") # ตั้งขนาดหน้าต่างเบราว์เซอร์เป็น 1920x1080 พิกเซล
```
การตั้งขนาดหน้าต่างช่วยให้แน่ใจว่าองค์ประกอบต่างๆ บนหน้าเว็บจะถูกโหลดและแสดงผลอย่างถูกต้อง

# Part 1: การนำทางและควบคุมเบราว์เซอร์

### เปิดเว็บไซต์
```python
url = "https://www.lotuss.com/th"
driver.get(url) # เปิดเว็บไซต์ที่ระบุในตัวแปร url ด้วย WebDriver
```
เมธอด get() ใช้สำหรับเปิดเว็บไซต์ที่ระบุในตัวแปร url โดย WebDriver จะควบคุมเบราว์เซอร์ให้ไปยัง URL นั้น เปรียบเสมือนการพิมพ์ URL ใน Address Bar แล้วกด Enter

---

# Part 2: การค้นหาองค์ประกอบ (Finding Elements)

### การค้นหาด้วย ID
```python
button = driver.find_element(By.ID, "onetrust-accept-btn-handler")  # ค้นหาองค์ประกอบปุ่มยอมรับ cookie โดยใช้ ID
button.click()  # คลิกที่ปุ่มยอมรับ cookie
```
การค้นหาด้วย ID เป็นวิธีที่เร็วและแม่นยำที่สุด เพราะ ID ควรไม่ซ้ำกันบนหน้าเว็บ

### การค้นหาด้วย XPath
```python
ck = driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/img")  # ค้นหาองค์ประกอบรูปภาพโดยใช้ XPath
ck.click()  # คลิกที่รูปภาพที่ค้นพบ
```
XPath คือเส้นทางที่อธิบายตำแหน่งขององค์ประกอบในหน้า HTML เหมาะสำหรับองค์ประกอบที่ไม่มี ID ที่ชัดเจน

---

# Part 3: การโต้ตอบกับองค์ประกอบ (Interacting with Elements)

### การส่งข้อความ (Text Input)
```python
textbox = driver.find_element(By.ID, "search-bar-input")  # ค้นหาองค์ประกอบกล่องค้นหาโดยใช้ ID
textbox.send_keys("น้ำดื่มตราสิงห์")  # ส่งข้อความ "น้ำดื่มตราสิงห์" ไปยังกล่องค้นหา
```
เมธอด send_keys() ใช้สำหรับป้อนข้อความในกล่องข้อมูลหรือทำการเรียกใช้ปุ่มบนแป้นพิมพ์

### การส่งคีย์บอร์ด (Keyboard Keys)
```python
textbox.send_keys(Keys.RETURN)  # ส่งคีย์ Enter เพื่อเริ่มการค้นหา
```
คลาส Keys มีค่าคงที่ที่แทนปุ่มพิเศษบนแป้นพิมพ์ เช่น RETURN, TAB, ESCAPE, ARROW_DOWN เป็นต้น

---

# Part 4: การจัดการหน้าเว็บ (Page Management)

### การเลื่อนหน้า (Scrolling)
```python
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # เลื่อนหน้าจอลงไปยังส่วนล่างสุดของหน้าเว็บ
```
เมธอด execute_script() ใช้สำหรับรัน JavaScript code ในบราว์เซอร์ script นี้จะเลื่อนหน้าลงไปจนถึงส่วนล่างสุด

### การรับแหล่งที่มา (Getting Page Source)
```python
html = driver.page_source  # ดึงแหล่งที่มาของหน้าเว็บปัจจุบันเป็น HTML
print(html)  # แสดงแหล่งที่มาของหน้าเว็บในคอนโซล
```
คุณสมบัติ page_source ให้เข้าถึง HTML ที่สมบูรณ์ของหน้าเว็บปัจจุบัน เหมาะสำหรับใช้กับ BeautifulSoup ในการวิเคราะห์เพิ่มเติม

---

# Part 5: การรวมกับ BeautifulSoup

### ประมวลผล HTML ด้วย BeautifulSoup
```python
from bs4 import BeautifulSoup  # ใช้สำหรับวิเคราะห์และดึงข้อมูลจาก HTML

soup = BeautifulSoup(html, "html.parser")  # สร้างวัตถุ BeautifulSoup จากแหล่งที่มาของหน้าเว็บ
soup.find_all(class_="MuiTypography-root MuiTypography-body1 mui-style-1jzbc9c")  # ค้นหาองค์ประกอบทั้งหมดที่มีคลาส "MuiTypography-root MuiTypography-body1 mui-style-1jzbc9c"
```
หลังจากได้ HTML จาก Selenium คุณสามารถใช้ BeautifulSoup ในการวิเคราะห์และดึงข้อมูลที่ต้องการได้

---

# Part 6: การปิดเบราว์เซอร์ (Closing Browser)

### ปิดเบราว์เซอร์
```python
driver.quit()  # ปิดเบราว์เซอร์และสิ้นสุดการทำงานของ WebDriver
```
เมธอด quit() ใช้สำหรับปิดเบราว์เซอร์และปลดปล่อยทรัพยากรที่ใช้ คุณควรเรียก quit() เมื่อ script เสร็จสิ้น