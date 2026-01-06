def count_words(text):
    """
    คืนค่าจํานวนคําในข้อความ (นับจากการเว้นวรรค)

    Parameters:
        text (ข้อความ): ประโยคที่ต้องการนับคํา

    Returns:
        int: จํานวนคําในข้อความ
    """
    words = text.split(" ") # แยกคําโดยใช้ช่องว่างเป็นตัวแบ่ง
    return len(words)

def count_vowels(text):
    """
    คืนค่าจํานวนสระในข้อความ

    Args:
        text (ข้อความ): ประโยคที่ต้องการนับสระ

    Returns:
        count(int): จํานวนสระในข้อความ
    """
    vowels = "a, e, i, o, u"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

def clean_text(text):
    return text.strip().lower()

def highlight(text):
    return f"*** {text} ***"