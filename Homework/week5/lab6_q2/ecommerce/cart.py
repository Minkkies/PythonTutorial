def add_item(cart_list, item_name, price):
    cart_list.append({
        'name': item_name,
        'price': price
    })
    print(f"เพิ่ม {item_name} ราคา {price} บาท ")

def remove_item(cart_list, item_name):
    for key in cart_list:
        if key['name'] == item_name:
            print(f"ลบ {item_name} ออกแล้ว")
            cart_list.remove(key)
        


def calculate_total(cart_list):
    total = 0
    for item in cart_list:
        total += item['price']
    print(f"ราคารวม: {total} บาท")

    return total
    

def apply_discount(total_price, percent):
    discounted = total_price * (1 - percent / 100)
    print(f"ราคาหลังหักส่วนลด {percent}%: {discounted:.2f} บาท")
    return discounted