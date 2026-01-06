from ecommerce.cart import add_item, remove_item, calculate_total, apply_discount

my_cart = []

print("--- เริ่มการช้อปปิ้ง ---")
add_item(my_cart, 'Mouse', 500)
add_item(my_cart, 'Keyboard', 1500)
add_item(my_cart, 'Monitor', 4000)

print("--- เปลี่ยนใจ ---")
remove_item(my_cart, 'Mouse')

print("--- สรุปยอด ---")
total_price = calculate_total(my_cart)
apply_discount(total_price, 10)

# result:
# --- เริ่มการช้อปปิ้ง ---
# เพิ่ม Mouse ราคา 500 บาท
# เพิ่ม Keyboard ราคา 1500 บาท
# เพิ่ม Monitor ราคา 4000 บาท
# --- เปลี่ยนใจ ---
# ลบ Mouse ออกแล้ว
# --- สรุปยอด ---
# ราคารวม: 5500 บาท
# ราคาหลังหักส่วนลด 10%: 4950.00 บาท