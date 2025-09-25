import csv


class Customer:
    # 各問のコードが期待通り動作するように実装
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        return f"{self.first_name} {self.family_name}"

    def age(self):
        return f"{self.age}"

    def entry_fee(self):
        if self.age <= 3:
            return f"0"
        elif self.age > 4 and self.age < 20:
            return f"1000"
        elif self.age >= 20 and self.age < 65:
            return f"1500"
        elif self.age < 75:
            return f"1200"
        else:
            return f"500"

    def info_csv(self):
        # csv対応
        return f"{self.full_name()},{self.age},{self.entry_fee()}"
    
    def info_tab(self):
        # タブ対応
        return f"{self.full_name()}\t{self.age}\t{self.entry_fee()}"
    
    def info_pipe(self):
        # タブ対応
        return f"{self.full_name()}|{self.age}|{self.entry_fee()}"


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
tom = Customer(first_name="Tom", family_name="Ford", age=57)
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=75)
michelle = Customer(first_name="Michelle", family_name="Tanner", age=3)
# フルネームを取得
print(ken.full_name())  # "Ken Tanaka" という値を出力
print(tom.full_name())  # "Tom Ford" という値を出力
print(ieyasu.full_name())  # "Ieyasu Tokugawa" という値を出力

# 年齢という概念の追加
print(ken.age)  # 15 という値を出力
print(tom.age)  # 57 という値を出力
print(ieyasu.age)  # 75 という値を出力

print(ken.entry_fee())  # 1000 という値を出力
print(tom.entry_fee())  # 1500 という値を出力
print(ieyasu.entry_fee())  # 1200 という値を出力
print(michelle.entry_fee())

print(ken.info_csv())  # "Ken Tanaka,15,1000" という値を出力
print(tom.info_csv())  # "Tom Ford,57,1500" という値を出力
print(ieyasu.info_csv())  # "Ieyasu Tokugawa,75,1200" という値を出力

print(ken.info_tab())
print(tom.info_tab())
print(ieyasu.info_tab())
print(michelle.info_tab())

print(ken.info_pipe())
print(tom.info_pipe())
print(ieyasu.info_pipe())
print(michelle.info_pipe())
