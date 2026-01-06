def final_price(price,tax_rate=0.07,**discounts): # **รับค่าแบบdictionary
    """
    คำนวณราคาสินค้าหลังหักส่วนลดแล้วเพิ่มภาษี
    
    Args:
        price : ราคาสินค้า
        tax_rate (float): อัตราภาษี (default: 0.07 = 7%)
        **discounts (dictionary): ส่วนลดต่างๆ เป็น keyword arguments
            - ที่ขึ้นต้นด้วย `special_`: ส่วนลดพิเศษ (คูณ 2 เท่า)
            - ที่ขึ้นต้นด้วย `expired_`: ส่วนลดหมดอายุ (ไม่ได้รับส่วนลด)
            - อื่นๆ: ส่วนลดปกติ
    
    Returns:
        float: ราคาสุดท้ายจากหักส่วนลดแล้วเพิ่มภาษี (ปัดเศษ 2 ตำแหน่ง)
    """
    # กรอกส่วนลดทั้งหมดจาก discounts
    for key, value in discounts.items():
        if key.startswith("special_"):
            discounts[key] = value * 2 # ส่วนลดพิเศษคูณ2เท่า
        elif key.startswith("expired_"):
            discounts[key] = 0  # ส่วนลดหมดอายุไม่ได้รับส่วนลด
        else:
            discounts[key] = value  # ส่วนลดปกติ
    total_discount = sum(discounts.values()) # รวมส่วนลดทั้งหมด

    # คำนวณราคารวมหลังหักส่วนลดและภาษี
    price = price - total_discount
    if price < 0:
        price = 0  # ราคาไม่ควรติดลบ
    
    price = price * (1 + tax_rate)
    return round(price, 2) #ทศยิม2ตำแหน่ง 


print(f"Case 1: {final_price(1000, discount_nov=100, expired_dec=500)}")
print(f"Case 2: {final_price(2000, special_vip=200)}")
print(f"Case 3: {final_price(3000, promo=100, special_year=200, expired_old=1000)}")
print(f"Case 4: {final_price(500, special_clearance=300)}")
print(f"Case 5: {final_price(2000, tax_rate=0, member=500)}")

# result:
# Case 1: 963.0
# Case 2: 1712.0
# Case 3: 2675.0
# Case 4: 0.0
# Case 5: 1500