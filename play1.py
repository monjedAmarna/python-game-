"""
🔹 لعبة قتال نصية مطورة (Advanced Text-Based Battle Game) 🔹
🚀 استمتع باللعب وحقق النصر! 🎮
"""

from classes.player import Player
from classes.enemy import Enemy
from classes.weapons import weapons_data  # استيراد بيانات الأسلحة
from classes.enemies import get_random_enemy_name  # ✅ استيراد دالة اختيار اسم عشوائي
import random
from classes.bcolors import bcolors  
# 🔹 إنشاء اللاعب واختيار السلاح
player_name = input("Enter your name: ")
weapon_choice = input("Choose your weapon (sword/axe/dagger): ").lower()
player = Player(player_name, 300, weapon_choice)

# 🔹 إنشاء العدو
enemy_name = get_random_enemy_name()
enemy = Enemy(enemy_name, (40, 100))

print(f"\n🔥 {bcolors.BOLD}{player.name} is fighting against {enemy.name}!{bcolors.ENDC} 🔥\n")

# 🔹 قائمة التعاويذ المتاحة
magic_attacks = {
    "dom": (90, 110),  # تعويذة دوم
    "big dom": (120, 140),  # تعويذة بيج دوم
    "none": None  # خيار عدم استخدام تعويذة
}

# 🔹 حلقة القتال
while player.hp > 0 and enemy.hp > 0:
    action = input("\nDo you want to (A)ttack or (D)efend?  ").lower()

    if action == 'a':
        if player.getmana() > 0:
            print(f"\n{bcolors.HEADER}Choose your magic attack:{bcolors.ENDC}")
            for spell in magic_attacks.keys():
                print(f"{bcolors.OKCYAN}- {spell}{bcolors.ENDC}")

            while True:
                action2 = input("Select your magic: ").lower()
                if action2 in magic_attacks:
                    break  
                else:
                    print(f"{bcolors.FAIL}❌ Invalid choice, please select a valid magic attack.{bcolors.ENDC}")
        else:
            print(f"{bcolors.WARNING}⚡ Not enough mana! Defaulting to weapon attack.{bcolors.ENDC}")
            action2 = "none"

        # 🔹 حساب الضرر
        weapon_min, weapon_max = player.atk_range
        weapon_dmg = random.randint(weapon_min, weapon_max)

        if magic_attacks[action2] is not None:
            min_dmg, max_dmg = magic_attacks[action2]
            magic_dmg = random.randint(min_dmg, max_dmg)
            player.usemana(10)
        else:
            magic_dmg = 0

        player_dmg = weapon_dmg + magic_dmg
        enemy.hp -= player_dmg
        print(f"\n{bcolors.FAIL}🔥 {player.name} used {action2} and dealt {player_dmg} damage! Enemy HP: {enemy.hp}{bcolors.ENDC}")

    elif action == 'd':
        print(f"\n{bcolors.OKBLUE}🛡️ {player.name} defends against {enemy.name}'s attack! Damage reduced.{bcolors.ENDC}")

    if enemy.hp <= 0:
        break

    enemy_dmg = enemy.attack()

    if action == 'd':
        enemy_dmg = player.defend(enemy_dmg)

    player.hp -= enemy_dmg
    print(f"\n{bcolors.FAIL}⚔️ {enemy.name} attacked {player.name} for {enemy_dmg} damage! {player.name} HP: {player.hp}{bcolors.ENDC}")

    if player.hp <= 0:
        break

# 🔹 التحقق من الفائز
if player.hp <= 0 and enemy.hp <= 0:
    if player.hp > enemy.hp:
        print(f"\n{bcolors.WARNING}💀 Both fighters fell! But {player.name} had more health left. Declaring {player.name} the winner!{bcolors.ENDC}")
    elif enemy.hp > player.hp:
        print(f"\n{bcolors.WARNING}💀 Both fighters fell! But {enemy.name} had more health left. Declaring {enemy.name} the winner!{bcolors.ENDC}")
    else:
        print(f"\n{bcolors.WARNING}⚖️ It's a draw! Both fighters fell at the same time!{bcolors.ENDC}")  

elif player.hp > 0:
    print(f"\n{bcolors.OKGREEN}🏆 {player.name} defeated {enemy.name}! You win!{bcolors.ENDC}")
elif enemy.hp > 0:
    print(f"\n{bcolors.FAIL}💀 {player.name} has died. {enemy.name} is victorious!{bcolors.ENDC}")
