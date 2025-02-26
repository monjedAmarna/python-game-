import random

# 🔹 قائمة بأسماء الأعداء العشوائية
enemy_names = [
    "mosab", "yazan ", "yousef ",
    "laith", "asad ", "ashraf",
    "majd ", "ahmad ", "mode "
]

def get_random_enemy_name():
    """إرجاع اسم عشوائي من القائمة"""
    return random.choice(enemy_names)
