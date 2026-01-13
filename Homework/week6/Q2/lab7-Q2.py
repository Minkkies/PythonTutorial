import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# ตรวจสอบว่าขนาดเวกเตอร์เท่ากันหรือไม่
def is_equal(v1,v2):
    return len(v1) == len(v2)

# หา dot product
def dot(v1,v2):
    total = 0
    for i in range(len(v1)):
        total += v1[i] * v2[i]
    return total

# แปลงข้อมูลในเวกเตอร์เป็น float
def convert_to_float(v):
    for i in range(len(v)):
        v[i] = float(v[i]) # แปลงstring,numberเป็นfloatเท่านั้น
    return v

# อ่านไฟล์และคืนค่าlist
def read_file_vector(filename):
    with open(filename,'r') as file:
        vector = file.readlines()

        result = []
        for line in vector:
            # แยกตัวเลขในแต่ละบรรทัด
            vector = line.strip().split()
            # เรียกใช้ convert_to_float 
            # ส่งค่าเวกเตอร์เข้าไปที่เป็นstring แล้วรับค่ากลับมาเป็น float
            vector = convert_to_float(vector)
            result.append(vector)
    return result

# ===== main program =====
filename = input("Choose your vector file: ")


vector = read_file_vector(filename)
v1 = vector[0]#บรรทัดแรก
v2 = vector[1]#บรรทัดที่สอง

print(f"v1 = {v1}")
print(f"v2 = {v2}")

if is_equal(v1, v2):
    print(f"v1*v2 = {dot(v1, v2)}")
else:
    print("Incompatible size")