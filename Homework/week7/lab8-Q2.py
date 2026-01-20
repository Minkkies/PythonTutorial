# 2.1 สร้างคลาสแม่ (Parent Class)
class BankAccount:
    def __init__(self,account_number,balance):
        self.account_number = account_number
        self._balance = 0 # Protected attribute

    def deposit(self,amount):
        if amount > 0:
            self._balance += amount
            print(f'ฝากเงินจำนวน {amount} บาท เข้าบัญชี {self.account_number}')
            print(f'ยอดคงเหลือ {self._balance} บาท')
        else:
            print("จํานวนเงินต้องมากกว่า 0")

    def withdraw(self,amount):
        if amount > 0 & amount <= self._balance:
            self._balance -= amount
            print(f'ถอนเงินจำนวน {amount} บาท จากบัญชี {self.account_number}')
            print(f'ยอดคงเหลือ {self._balance} บาท')
        else:
            print("ยอดเงินไม่พอหรือจํานวนเงินไม่ถูกต้อง")

    def get_balance(self):
        return self._balance
    
# 2.2 สร้างคลาสลูก (Child Class)
class SavingsAccount(BankAccount):
    interest_rate = 0.015 # Class Attribute

    def __init__(self, account_number, balance = 0):
        super().__init__(account_number, balance)

    def add_interest(self):
        interest = self._balance * self.interest_rate
        self._balance += interest
        print(f"เพิ่มดอกเบี้ย {interest:2f} บัญชี {self.account_number}")

# 2.3 การทดสอบ (Testing)
save = SavingsAccount("123-456-789")
save.deposit(10000)
print('-'*40)
save.add_interest()
print('-'*40)
save.withdraw(2000)