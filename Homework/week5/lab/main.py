# import math
# import my_tools.calculator
# # เวลาเรียกใช้ต้องระบุชื่อเต็ม
# print(math.sqrt(4))
# result = my_tools.calculator.add(10, 5)
# print(f"ผลบวก: {result}")
import my_tools.module_test as test
import my_tools.shapes.circle as circle_tool
area = circle_tool.get_area(7)
print(f"พื้นที่วงกลม: {area:.2f}")

print(test.greeting('kd'))