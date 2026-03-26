from abc import ABC, abstractmethod

# คลาสพื้นฐานสำหรับยานพาหนะเป็นคลาสนามธรรม
class Vehical(ABC):
    def __init__(self,license_plate,brand,base_rate_per_day):
        self.license_plate = license_plate
        self.brand = brand
        self.base_rate_per_day = base_rate_per_day
        self.is_rented = False

    def rent_vehicle(self):
        if self.is_rented:
            print(f"ไม่สามารถดำเนินการได้ ทะเบียน {self.license_plate} ถูกเช่าอยู่")
        else:
            self.is_rented = True
            print(f"ดำเนินการเรียบร้อย ทะเบียน {self.license_plate} ถูกเช่าแล้ว")

    def return_vehicle(self):
        if not self.is_rented:
            print(f"ไม่สามารถดำเนินการได้ ทะเบียน {self.license_plate} ไม่ได้ถูกเช่าอยู่")
        else:
            self.is_rented = False
            print(f"ดำเนินการเรียบร้อย ทะเบียน {self.license_plate} ถูกคืนแล้ว")

    def get_status(self):
        status = "ถูกเช่า" if self.is_rented else "ว่าง"
        print(f"สถานะปัจจุบัน: {status}")

    @abstractmethod
    def calculate_rental_fee(self, days):
        pass
    
    @abstractmethod
    def display_details(self):
        pass

# คลาสสำหรับรถยนต์ เป็น concrete class ที่สืบทอดจาก Vehical
class Car(Vehical):
    def __init__(self, license_plate, brand, base_rate_per_day, seat_capacity ):
        super().__init__(license_plate, brand, base_rate_per_day) # เรียก constructor ของคลาสแม่
        self.seat_capacity = seat_capacity

    # override method สำหรับคำนวณค่าธรรมเนียมการเช่า
    def calculate_rental_fee(self, days):
        if self.seat_capacity > 5:
            total_standard= self.base_rate_per_day * days 
            total_fee= total_standard * 1.15
            print(f"คำนวณค่าเช่า {self.license_plate}")
            print(f"คำนวณ(รถขนาดใหญ่): {total_standard} (ราคาพื้นฐาน) + {total_fee - total_standard}(ที่นั่ง > 5)= {total_fee} บาท")
            return total_fee
        else:
            total_fee = self.base_rate_per_day * days
            print(f"คำนวณค่าเช่า {self.license_plate}")
            print(f"คำนวณ(รถขนาดมาตราฐาน): {total_fee} บาท")
            return total_fee

    # override method สำหรับแสดงรายละเอียดของรถยนต์
    def display_details(self):
        print(f"ทะเบียน: {self.license_plate}, ยี่ห้อ: {self.brand}, ที่นั่ง: {self.seat_capacity}")

# main function 
car1_large = Car("กข1234", "Toyota", 1500, 7)
car2_small = Car("บบ5678", "Honda", 1000, 4)

print("--แสดงข้อมูลรถในระบบ--")
car1_large.display_details()
car1_large.get_status()

car2_small.display_details()
car2_small.get_status()

print("--การเช่ารถ--")
car1_large.rent_vehicle()
car1_large.rent_vehicle()
car1_large.get_status()

print("--คำนวณค่าเช่า--")
fee1 = car1_large.calculate_rental_fee(3)
fee2 = car2_small.calculate_rental_fee(3)
print(f"ค่าธรรมเนียมรวมทั้งหมด:{fee1 + fee2} บาท")