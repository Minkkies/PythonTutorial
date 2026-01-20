class PhoneBattery:
    def __init__(self):
        # 1.1 private attribute ค่าเริ่มต้น 100
        self.__percent = 100

    def use_battery(self, amount):
        # 1.2 ลดแบตเตอรี่ตามจํานวนที่ระบุ
        self.__percent -= amount

        # 1.4 ลดระดับแบตเตอรี่ไม่ให้ต่ำกว่า 0
        if self.__percent < 0:
            self.__percent = 0
    
    def charge_battery(self, amount):
        # 1.3 เพิ่มปริมาณแบตเตอรี่ตามจํานวนที่ระบุ
        self.__percent += amount

        # 1.4 ลดระดับแบตเตอรี่ไม่ให้มากกว่า 100
        if self.__percent > 100:
            self.__percent = 100

    def get_percent(self):
        # 1.5 Getter อ่านค่าเปอร์เซ็นต์แบต
        return self.__percent
    
# การเรียกใช้
battery = PhoneBattery()
print(f"แบตเตอรี่เริ่มต้น: {battery.get_percent()} %") # เข้าคอนสตรัคกำหนดให้ 100

# ลดแบตเตอรี่ = use
battery.use_battery(32)
print(f"แบตเตอรี่คงเหลือ: {battery.get_percent()} หลังใช้แบต 32%") 

# ชาร์จแบต
battery.charge_battery(26)
print("หลังชาร์จ 26%:", battery.get_percent(), "%")


print("-"*6,"ทดสอบใส่ค่าเกิน","-"*6)
# ลดแบตเตอรี่ทดสอบเมื่อใส่เกิน100
battery.use_battery(120)
print(f"แบตเตอรี่คงเหลือ: {battery.get_percent()} หลังใช้แบต 120%")

# ชาร์จเกิน
battery.charge_battery(120)
print("หลังชาร์จเกิน 100%:", battery.get_percent(), "%")