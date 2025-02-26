import random

class Enemy:
    default_hp = 300
    default_enemy_damage_range = (40, 100)

    def __init__(self, name, atk_range=None):
        """تهيئة العدو مع اسم ونطاق ضرر مخصص (إذا لم يُحدد يتم استخدام الافتراضي)"""
        self.name = name
        self.hp = Enemy.default_hp
        self.atk_range = atk_range if atk_range else Enemy.default_enemy_damage_range

    def attack(self):
        """تنفيذ هجوم العدو"""
        return random.randint(*self.atk_range)

    def get_hp(self):
        """طباعة نقاط صحة العدو"""
        print(f"{self.name} has {self.hp} HP.")

    def get_atk(self):
        """طباعة نطاق هجوم العدو"""
        print(f"{self.name}'s attack range is {self.atk_range}.")
