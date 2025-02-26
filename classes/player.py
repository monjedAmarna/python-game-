import random
from classes.weapons import weapons_data  # استيراد بيانات الأسلحة
mana =200

class Player:
    mana =200

    def __init__(self, name, hp, weapon_choice):
        """تهيئة اللاعب مع اسمه، نقاط صحته، وسلاحه"""
        self.name = name
        mana =200

        self.hp = hp
        self.atk_range = weapons_data.get(weapon_choice, (100, 120))  # اختيار نطاق الضرر حسب السلاح

    def attack(self):
        """تنفيذ هجوم اللاعب"""
        return random.randint(*self.atk_range)

    def defend(self, damage):
        """تقليل الضرر عند الدفاع"""
        return damage // 2
    
    def getmana(self):
        return self.mana 
    
    def usemana(self, amount):
      self.mana -= amount
      if self.mana < 0:
        self.mana = 0
