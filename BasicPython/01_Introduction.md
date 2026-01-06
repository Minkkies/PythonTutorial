# 1. บทนำ (Introduction)

## ภาษา Python ใช้ทำอะไรได้บ้าง

1. **Web Development**: Python สามารถใช้พัฒนาเว็บด้วย framework ต่าง ๆ เช่น FastAPI, Django, Flask หรือ Pyramid ซึ่งทำให้การพัฒนาเว็บเป็นเรื่องง่ายและรวดเร็ว

2. **Data Science & Data Analysis**: Python มี library มากมาย เช่น Pandas, NumPy, และ Matplotlib ที่ช่วยในการวิเคราะห์และจัดการข้อมูล รวมถึงการทำ Machine Learning ด้วย library อย่าง Scikit-learn, TensorFlow, และ Keras

3. **Automation/Scripting**: Python เป็นภาษายอดนิยมสำหรับการเขียน script เพื่อทำงานซ้ำ ๆ หรืออัตโนมัติ เช่น การจัดการไฟล์ การส่งอีเมล หรือการทำงานกับ API (ด้วยความที่ภาษามันง่ายด้วยแหละ)

4. **Game Development**: มีเครื่องมือและ library อย่าง Pygame ที่ช่วยให้สามารถสร้างเกมสองมิติได้ง่าย ๆ

5. **AI/Machine Learning**: Python ถูกใช้กันอย่างแพร่หลายในการพัฒนา AI และ Machine Learning เนื่องจากมี library ที่ทรงพลังเช่น TensorFlow, PyTorch, และ OpenCV

6. **IoT**: Python สามารถใช้ในการพัฒนา IoT ด้วยการเชื่อมต่อกับอุปกรณ์ hardware ผ่าน Raspberry Pi หรือบอร์ด micro controller ต่าง ๆ

ถ้าเราลองดูตามความนิยมของภาษา Python ในการ survey ต่างๆ เราก็จะเจอว่า เป็นภาษาที่ developer ชอบเป็นอันดับต้นๆ เลย (บางสำนักก็เป็นอันดับ 1 เลย) ดังนั้น หากใครที่ยังไม่มีความรู้ในการเขียน program หรือยังเขียน program มาไม่มาก python ถือเป็นภาษาที่เหมาะแก่การเริ่มต้นด้วยเช่นเดียวกัน

## ลง Python

สำหรับการลง Python นั้น ให้ทำการเข้าเว็บ python เพื่อ download มา: https://www.python.org/downloads/

หลังจากนั้น Download มา และทำการ install ตามขั้นตอนให้เรียบร้อย

หลังจากนั้นให้ลองเปิด:
- **Windows**: เปิด cmd
- **Mac**: เปิด terminal

แล้วลองพิมพ์คำสั่ง: `python --version`

หากดำเนินการเรียบร้อย จะสามารแสดงเลข version ออกมาได้

## ใช้งาน Python กับ VS Code

เพื่อให้เราสามารถใช้งาน Python ร่วมกับ editor ได้ เราจะใช้งาน VS Code กัน สามารถ download ได้ที่: https://code.visualstudio.com/download

### การทดสอบการใช้ Python

1. สร้างไฟล์ `main.py` ขึ้นมา 1 file พร้อมกับ code สำหรับการแสดงผลทาง Console

```python
print("Hello World")
```

2. เปิด terminal ขึ้นมา และ run ด้วยคำสั่ง: `python main.py`

หากทำทุกอย่างถูกต้อง ก็จะแสดงคำว่า "Hello World" ออกมาทาง terminal ได้

---

## watch: [Basic Python](https://www.youtube.com/watch?v=ESNFhgRqeow&list=PLwZ0y9k-cYXALFTl5X2A3IPNTyK-9vm-v&index=6)

สามารถรัน Python ได้ 2 วิธี :
1. พิมใน Terminal => python (..ชื่อไฟล์..)
2. กด Run code ใน VSC Ctrl+Alt+N (ก่อนกดโหลด Python extension ใน VSC ก่อน)
