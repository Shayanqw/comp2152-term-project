# tawsif_feature.py — Experience Points & Leveling Up

# Feature: XP & Leveling Up system
# 1. Hero gains XP each round won
# 2. Every 3 XP → level up → +1 combat strength
# 3. Displays new level and updated strength after each level-up

import random

def get_combat_strength_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if 1 <= value <= 6:
                return value
            else:
                print("Enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

combat_strength = get_combat_strength_input("Enter your combat strength (1-6): ")
monster_combat_strength = get_combat_strength_input("Enter monster's combat strength (1-6): ")

xp = 0
level = 1
xp_threshold = 3

for round_number in range(1, 20, 2):
    if round_number == 11:
        print("\nBattle Truce declared in Round 11. Game Over!")
        break

    hero_roll = random.randint(1, 6)
    monster_roll = random.randint(1, 6)

    hero_total = combat_strength + hero_roll
    monster_total = monster_combat_strength + monster_roll

    print(f"\nRound {round_number}: Hero rolled {hero_roll}, Monster rolled {monster_roll}.")
    print(f"Hero Total Strength: {hero_total}, Monster Total Strength: {monster_total}.")

    if hero_total > monster_total:
        print("Hero wins the round!")
        xp += 1
        if xp >= xp_threshold:
            level += 1
            combat_strength += 1
            xp = 0
            print(f"Level Up! Hero reached Level {level}. New base combat strength: {combat_strength}.")
    elif monster_total > hero_total:
        print("Monster wins the round!")
    else:
        print("It's a tie!")
