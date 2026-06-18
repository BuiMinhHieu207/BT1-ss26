# (1) Phân tích lỗi (Code Review)
# a. Vòng lặp
# for hero in team_heroes:
#     hero.use_ultimate()

# thể hiện tính Đa hình (Polymorphism) như thế nào?

# Vòng lặp này không cần biết đối tượng là:

# Mage
# Assassin
# Hay bất kỳ lớp con nào của Hero

# Nó chỉ gọi:

# hero.use_ultimate()

# Mỗi đối tượng sẽ tự thực thi phiên bản use_ultimate() của riêng mình.

# Ví dụ:

# Mage().use_ultimate()

# gọi:

# 🔥 Pháp Sư tung chiêu: MƯA SAO BĂNG!

# Còn:

# Assassin().use_ultimate()

# sẽ gọi chiêu của Sát thủ.

# Đó chính là Polymorphism (Đa hình):

# Cùng một lời gọi phương thức nhưng hành vi khác nhau tùy thuộc vào kiểu đối tượng thực tế.

# Nhờ vậy không cần viết:

# if isinstance(hero, Mage):
#     ...
# elif isinstance(hero, Assassin):
#     ...

# Máy chủ chỉ cần biết:

# "Đã là Hero thì phải có use_ultimate()."

# Đúng kiểu Duck Typing của Python:

# "Nếu nó hành xử như vịt thì cứ xem nó là vịt."

# b. Với code cũ, lỗi xảy ra khi nào?

# Đối tượng:

# Assassin()

# được tạo ra hoàn toàn bình thường:

# team_heroes = [Mage(), Assassin()]

# Console:

# --- LOADING TRẬN ĐẤU ---
# Tải trận đấu thành công!

# không hề báo lỗi.

# Lỗi chỉ xuất hiện khi giao tranh bắt đầu:

# for hero in team_heroes:
#     hero.use_ultimate()

# đến lượt:

# Assassin().use_ultimate()

# Python không tìm thấy hàm trong lớp Assassin, nên kế thừa hàm từ lớp cha:

# def use_ultimate(self):
#     raise NotImplementedError(...)

# và sinh ra:

# NotImplementedError
# Vì sao báo lỗi muộn là thảm họa?

# Nguyên tắc:

# Bug càng phát hiện muộn càng tốn kém.

# Người chơi đã:

# Chờ loading trận đấu.
# Bắt đầu giao tranh.
# Đang chơi giữa trận.

# Thì game đột ngột crash.

# Điều này gây:

# Mất trận.
# Mất dữ liệu.
# Trải nghiệm cực tệ.

# Đáng lẽ lỗi phải được phát hiện ngay khi khởi tạo đội hình.

# c. Nếu dùng ABC và @abstractmethod thì lỗi xuất hiện khi nào?

# Giả sử:

# class Assassin(Hero):
#     def stealth_kill(self):
#         ...

# vẫn quên định nghĩa:

# use_ultimate()

# Khi thực hiện:

# Assassin()

# Python sẽ lập tức báo:

# TypeError:
# Can't instantiate abstract class Assassin
# with abstract method use_ultimate

# Tức là lỗi xuất hiện ngay lúc:

# LOADING TRẬN ĐẤU

# chứ không đợi đến giao tranh.

# d. Fail Fast được thể hiện như thế nào?

# Fail Fast = Báo lỗi càng sớm càng tốt.

# Không để:

# Load thành công
# ↓
# Chơi được vài phút
# ↓
# Vào combat
# ↓
# Crash

# Mà:

# Load trận đấu
# ↓
# Phát hiện thiếu use_ultimate()
# ↓
# Dừng ngay lập tức
# ↓
# Lập trình viên sửa bug

# Abstract Base Class biến lỗi Runtime thành lỗi khi khởi tạo đối tượng.

# Giúp:

# Phát hiện bug sớm.
# Debug dễ hơn.
# Hệ thống ổn định hơn.
# Tránh crash giữa trận.
# (2) Refactoring - Code chuẩn
from abc import ABC, abstractmethod


# Lớp cha trừu tượng
class Hero(ABC):

    @abstractmethod
    def use_ultimate(self):
        pass


# Pháp sư
class Mage(Hero):

    def use_ultimate(self):
        print("🔥 Pháp Sư tung chiêu: MƯA SAO BĂNG!")


# Sát thủ
class Assassin(Hero):

    def use_ultimate(self):
        print("🗡️ Sát Thủ tung chiêu: ÁM SÁT TỪ PHÍA SAU!")


# ==========================
# KỊCH BẢN GAME
# ==========================

print("--- LOADING TRẬN ĐẤU ---")

team_heroes = [Mage(), Assassin()]

print("Tải trận đấu thành công! Các tướng đã sẵn sàng...")

print("\n--- GIAO TRANH TỔNG BẮT ĐẦU ---")

# Đa hình
for hero in team_heroes:
    hero.use_ultimate()
