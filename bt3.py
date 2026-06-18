# (1) Phân tích thiết kế
# Sơ đồ kế thừa
#                 ABC
#                  │
#             Champion
#           (Abstract Class)
#                  │
#         ┌────────┴────────┐
#         │                 │
#      Warrior            Mage
# Champion là lớp trừu tượng, không được phép khởi tạo trực tiếp.
# Warrior, Mage kế thừa từ Champion.
# Các thuộc tính chung được tái sử dụng nhờ super().
# Phân tích tính đa hình (Polymorphism)

# Tất cả các lớp con đều có:

# calculate_skill_damage()

# nhưng cách tính khác nhau:

# Warrior
# base_atk * 2 + shield_bonus
# Mage
# base_atk * ability_power

# Ví dụ:

# for champion in champion_pool:
#     print(champion.calculate_skill_damage())

# Không cần biết đối tượng là Warrior hay Mage.

# Nếu sau này thêm:

# class Assassin(Champion):

# chỉ cần override:

# calculate_skill_damage()

# toàn bộ hệ thống cũ vẫn hoạt động.

# Đó chính là Polymorphism.

# Phân tích Operator Overloading __add__

# Cho phép:

# w1 + w2

# thực chất gọi:

# w1.__add__(w2)

# trả về:

# w1.get_combat_power() + w2.get_combat_power()

# Ngoài ra:

# 0 + w1

# sẽ gọi:

# w1.__radd__(0)

# giúp dùng:

# total_power = sum(team)

# mà không cần viết vòng lặp thủ công.

# (2) Source Code Hoàn Chỉnh
from abc import ABC, abstractmethod


class Champion(ABC):
    """
    Lớp cơ sở trừu tượng của mọi quân cờ.
    """

    def __init__(self, champion_id, name, base_hp, base_atk):
        self.champion_id = champion_id
        self.name = name

        self.base_hp = base_hp if base_hp > 0 else 100
        self.base_atk = base_atk if base_atk > 0 else 100

    @abstractmethod
    def calculate_skill_damage(self):
        """
        Tính sát thương kỹ năng.
        """
        pass

    def get_combat_power(self):
        """
        Tính chiến lực tổng hợp.
        """
        return self.base_hp + self.calculate_skill_damage() * 1.5

    def __add__(self, other):
        """
        Nạp chồng toán tử +
        """

        if isinstance(other, Champion):
            return self.get_combat_power() + other.get_combat_power()

        elif isinstance(other, (int, float)):
            return self.get_combat_power() + other

        return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __gt__(self, other):
        return self.get_combat_power() > other.get_combat_power()


class Warrior(Champion):
    """
    Hệ Chiến Binh.
    """

    def __init__(self, champion_id, name, base_hp, base_atk, shield_bonus):
        super().__init__(champion_id, name, base_hp, base_atk)
        self.shield_bonus = shield_bonus

    def calculate_skill_damage(self):
        return self.base_atk * 2 + self.shield_bonus


class Mage(Champion):
    """
    Hệ Pháp Sư.
    """

    def __init__(self, champion_id, name, base_hp, base_atk, ability_power):
        super().__init__(champion_id, name, base_hp, base_atk)
        self.ability_power = ability_power

    def calculate_skill_damage(self):
        return self.base_atk * self.ability_power


# ==========================
# HÀM HỖ TRỢ
# ==========================

def input_number(message):
    """
    Nhập số an toàn.
    """
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Vui lòng nhập số hợp lệ!")


def find_champion(pool, champion_id):
    """
    Tìm tướng theo mã.
    """
    for champion in pool:
        if champion.champion_id == champion_id:
            return champion
    return None


# ==========================
# CHỨC NĂNG 1
# ==========================

def display_pool(pool):
    print("\n--- DANH SÁCH QUÂN CỜ ---")

    for champion in pool:

        if isinstance(champion, Warrior):
            role = "Warrior"
            extra = f"Armor: {champion.shield_bonus}"

        else:
            role = "Mage"
            extra = f"Mana: {champion.ability_power}"

        print(
            f"{champion.champion_id} | "
            f"{champion.name} | "
            f"{role} | "
            f"HP:{champion.base_hp:.0f} | "
            f"ATK:{champion.base_atk:.0f} | "
            f"{extra} | "
            f"Combat:{champion.get_combat_power():.0f}"
        )


# ==========================
# CHỨC NĂNG 2
# ==========================

def add_champion(pool):

    role = input("1-Warrior | 2-Mage: ")

    champion_id = input("Nhập mã tướng: ")

    if find_champion(pool, champion_id):
        print("Mã tướng đã tồn tại!")
        return

    name = input("Tên tướng: ")

    hp = input_number("HP: ")
    atk = input_number("ATK: ")

    if role == "1":

        armor = input_number("Armor: ")

        champion = Warrior(
            champion_id,
            name,
            hp,
            atk,
            armor
        )

    elif role == "2":

        ap = input_number("Ability Power: ")

        champion = Mage(
            champion_id,
            name,
            hp,
            atk,
            ap
        )

    else:
        print("Lựa chọn không hợp lệ!")
        return

    pool.append(champion)

    print("Thêm tướng thành công!")
    print(
        f"{champion.name} | Combat Power = {champion.get_combat_power():.0f}"
    )


# ==========================
# CHỨC NĂNG 3
# ==========================

def compare_champions(pool):

    id1 = input("Mã tướng thứ nhất: ")
    id2 = input("Mã tướng thứ hai: ")

    c1 = find_champion(pool, id1)
    c2 = find_champion(pool, id2)

    if c1 is None or c2 is None:
        print("Không tìm thấy tướng!")
        return

    if c1 > c2:
        stronger = c1
        weaker = c2
    else:
        stronger = c2
        weaker = c1

    print(
        f"{stronger.champion_id} - {stronger.name} mạnh hơn "
        f"{weaker.champion_id} - {weaker.name}"
    )


# ==========================
# CHỨC NĂNG 4
# ==========================

def calculate_team_power(pool):

    ids = input(
        "Nhập danh sách mã tướng (cách nhau dấu phẩy): "
    )

    ids = ids.split(",")

    team = []

    for champion_id in ids:

        champion_id = champion_id.strip()

        champion = find_champion(pool, champion_id)

        if champion:
            team.append(champion)
        else:
            print(
                f"Mã tướng {champion_id} không hợp lệ, bỏ qua!"
            )

    total_power = sum(team)

    print("\nĐội hình:")

    for champion in team:
        print(
            f"{champion.champion_id} - "
            f"{champion.name} | "
            f"{champion.get_combat_power():.0f}"
        )

    print(
        f"\nTổng chiến lực đội hình: {total_power:.0f}"
    )


# ==========================
# DỮ LIỆU MẪU
# ==========================

champion_pool = [
    Warrior("WAR01", "Rikkei Knight", 1200, 300, 150),
    Warrior("WAR02", "Steel Guardian", 1500, 250, 200),
    Mage("MAG01", "Rikkei Wizard", 800, 500, 2)
]


# ==========================
# MENU
# ==========================

while True:

    print("""
1. Hiển thị bể tướng
2. Thêm tướng
3. So sánh sức mạnh
4. Tính tổng chiến lực đội hình
5. Thoát
""")

    choice = input("Chọn chức năng: ")

    if choice == "1":
        display_pool(champion_pool)

    elif choice == "2":
        add_champion(champion_pool)

    elif choice == "3":
        compare_champions(champion_pool)

    elif choice == "4":
        calculate_team_power(champion_pool)

    elif choice == "5":
        print(
            "Cảm ơn bạn đã sử dụng Rikkei RPG - Auto-Battler Manager!"
        )
        break

    else:
        print("Lựa chọn không hợp lệ!")
