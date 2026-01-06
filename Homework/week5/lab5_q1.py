def calculate_stats(*args): # *รับได้หลายค่าแบบข้อมูลชนิดtuple
    """
    คำนวณสถิติพื้นฐานของตัวเลข
    
    Args:
        *args(เป็น Tuple): จำนวนตัวเลขที่ต้องการหลายค่า 
        
    Returns:
        dict: Dictionary ที่มี key ดังนี้:
            - 'total': ผลรวม
            - 'average': ค่าเฉลี่ย
            - 'max': ค่าสูงสุด
            - 'min': ค่าต่ำสุด
        กรณีไม่มีการส่งค่ามา ให้คืนค่า Dictionary ที่ทุกค่าเป็น 0
    """
    if not args:
        return {"sum": 0, "average": 0, "max": 0, "min": 0} # กรณีไม่มีค่าเข้ามา

    total = sum(args)
    average = total / len(args)
    maximum = max(args)
    minimum = min(args)
    return {"sum": total, "average": average, "max": maximum, "min": minimum}
   
print(calculate_stats(10, 20, 30, 40, 50))
print(calculate_stats(5, 5))
print(calculate_stats())

# reult:
# {'sum': 150, 'average': 30.0, 'max': 50, 'min': 10}
# {'sum': 10, 'average': 5.0, 'max': 5, 'min': 5}
# {'sum': 0, 'average': 0, 'max': 0, 'min': 0}