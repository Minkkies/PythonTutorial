import math

def distance1(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def distance2(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def distance3(c1, c2):
    # ระยะระหว่างจุดศูนย์กลาง
    d = math.sqrt((c2[0] - c1[0])**2 + (c2[1] - c1[1])**2)

    # เช็คแตะหรือทับกัน
    overlap = d <= (c1[2] + c2[2])

    return d, overlap

def perimeter(points):
    total = 0

    for i in range(len(points)):
        p1 = points[i]
        p2 = points[(i + 1) % len(points)]  # จุดถัดไป (วนกลับจุดแรก)
        total += distance2(p1, p2)

    return total


print("distance1: ",distance1(0,0,3,4))
print("distance2: ",distance2([0, 0], [3, 4]))

a, b = distance3([0, 0, 1], [5, 0, 2])
print("distance3: ", a, b)
# print(type(a) , type(b)) #a เก็บค่า d, b เก็บค่า bool overlap

print("perimeter: ", perimeter([[0, 0], [0, 2], [2, 2], [2, 0]]))

# ผลลัพธ์ที่ได้ควรเป็น
# distance1:  5.0
# distance2:  5.0
# distance3:  5.0 False
# perimeter:  8.0