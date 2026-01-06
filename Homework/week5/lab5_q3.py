def power_recursive(base, exponent):
    """
    คำนวณเลขยกกำลังโดยใช้ Recursion
    
    Args:
        base (int/float): เลขฐาน
        exponent (int): เลขชี้กำลัง (ต้องเป็นจำนวนเต็มไม่เป็นลบ)
    
    Returns:
        int/float: ผลลัพธ์ของ base^exponent
        ตัวอย่าง: power_recursive(2, 3) = 8
    """
    if exponent == 0:
        return 1
    else:
        return base * power_recursive(base, exponent - 1)
    
print(f"2^3 = {power_recursive(2, 3)}")
print(f"5^0 = {power_recursive(5, 0)}")
print(f"5^2 = {power_recursive(5, 2)}")

# result:
# 2^3 = 8
# 5^0 = 1
# 5^2 = 25