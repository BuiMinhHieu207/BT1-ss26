# (1) Phân tích lỗi (Code Review)
# a. Vì sao print(f"Chiến binh {w1.name} xuất trận!") gây ra AttributeError?

# Trong lớp cha Character, thuộc tính name, hp, attack_power được tạo trong hàm:

# def __init__(self, name, hp, attack_power):
#     self.name = name
#     self.hp = hp
#     self.attack_power = attack_power

# Nhưng trong lớp Warrior, lập trình viên đã ghi đè (override) phương thức __init__():

# class Warrior(Character):
#     def __init__(self, name, hp, attack_power, bonus_armor):
#         self.bonus_armor = bonus_armor

# Khi tạo:

# w1 = Warrior("Arthur", 1000, 150, 50)

# Python chỉ chạy __init__() của Warrior, còn __init__() của Character hoàn toàn không được gọi.

# Do đó đối tượng w1 chỉ có:

# self.bonus_armor

# mà không có:

# self.name
# self.hp
# self.attack_power

# Vì vậy:

# print(w1.name)

# sẽ gây lỗi:

# AttributeError: 'Warrior' object has no attribute 'name'
# Thiếu cú pháp gì?

# Thiếu:

# super().__init__(name, hp, attack_power)
# b. Nếu không dùng super(), có thể gọi trực tiếp lớp cha như thế nào?

# Có thể gọi:

# Character.__init__(self, name, hp, attack_power)

# Ví dụ:

# class Warrior(Character):
#     def __init__(self, name, hp, attack_power, bonus_armor):
#         Character.__init__(self, name, hp, attack_power)
#         self.bonus_armor = bonus_armor

# Cách này vẫn chạy được nhưng không được khuyến khích vì:

# Khó bảo trì.
# Không hỗ trợ tốt đa kế thừa (Multiple Inheritance).
# super() linh hoạt và an toàn hơn.
# c. Nếu sửa lỗi 1 xong, chương trình sẽ lỗi gì ở:
# if w1 > w2:

# Lỗi:

# TypeError

# Cụ thể:

# TypeError: '>' not supported between instances of 'Warrior' and 'Warrior'
# Tại sao?

# Python không biết tiêu chí để so sánh hai đối tượng Warrior.

# Đối với số nguyên:

# 5 > 3

# Python biết cách so sánh.

# Nhưng đối với:

# w1 > w2

# Python không biết nên so:

# Máu?
# Sát thương?
# Giáp?
# Hay tổng sức mạnh?

# Do đó phải tự định nghĩa cách so sánh.

# d. Cần khai báo Magic Method nào?

# Cần khai báo:

# __gt__()

# (Greater Than)

# Nó nhận 2 tham số:

# def __gt__(self, other):
# self: đối tượng bên trái dấu >
# other: đối tượng bên phải dấu >

# Ví dụ:

# w1 > w2

# sẽ được Python chuyển thành:

# w1.__gt__(w2)
# (2) Refactoring - Sửa code chuẩn
# Lớp cha
class Character:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power


# Lớp con
class Warrior(Character):
    def __init__(self, name, hp, attack_power, bonus_armor):
        # Kế thừa thuộc tính từ Character
        super().__init__(name, hp, attack_power)

        # Thuộc tính riêng của Warrior
        self.bonus_armor = bonus_armor

    # Tổng sức mạnh
    def get_total_power(self):
        return self.attack_power + self.bonus_armor

    # Nạp chồng toán tử >
    def __gt__(self, other):
        return self.get_total_power() > other.get_total_power()


# ---- KỊCH BẢN MATCHMAKING ----

# Tạo 2 chiến binh
w1 = Warrior("Arthur", 1000, 150, 50)      # 200
w2 = Warrior("Lancelot", 900, 180, 10)     # 190

# Xuất trận
print(f"Chiến binh {w1.name} xuất trận!")

# So sánh sức mạnh
if w1 > w2:
    print(f"{w1.name} mạnh hơn {w2.name}!")
else:
    print(f"{w2.name} mạnh hơn hoặc hòa!")
