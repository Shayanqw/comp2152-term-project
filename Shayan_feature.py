# 5V5_battle.py
# Shayan Pourahmad
#Student ID: 101474651
import random
from hero import Hero
from monster import Monster
import functions

loot_options_master = [
    "Health Potion", "Poison Potion", "Secret Note", "Leather Boots", "Flimsy Gloves"
]
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]
small_dice_options = list(range(1, 7))
monster_powers = {
    "Fire Magic": 2,
    "Freeze Time": 4,
    "Super Hearing": 6
}

def prepare_hero(hero, loot_options):
    print("\n--- Preparing a Hero ---")
    print(f"Hero's initial combat strength: {hero.combat_strength}")
    print(f"Hero's initial health points: {hero.health_points}")

    weapon_roll = random.choice(small_dice_options)
    hero.combat_strength = min(6, hero.combat_strength + weapon_roll)
    print(f"Weapon roll: {weapon_roll} → weapon: {weapons[weapon_roll - 1]} → CS: {hero.combat_strength}")

    belt = []
    loot_pool = loot_options.copy()
    for _ in range(2):
        loot_pool, belt = functions.collect_loot(loot_pool, belt)

    belt.sort()
    print("Hero's belt:", belt)

    belt, updated_hp = functions.use_loot(belt, hero.health_points)
    hero.health_points = updated_hp

    while True:
        try:
            lvl = int(input("Choose dream level for hero (0-3): "))
            if 0 <= lvl <= 3:
                break
            else:
                print("Enter value 0 to 3 only.")
        except ValueError:
            print("Invalid number. Try again.")

    if lvl != 0:
        hero.health_points = max(0, hero.health_points - 1)
        dream_buff = functions.inception_dream(lvl)
        hero.combat_strength += dream_buff
        print(f"Dream Buff → +{dream_buff} CS → Now: {hero.combat_strength}")
        print(f"Post-dream HP: {hero.health_points}")

def prepare_monster(monster):
    print(f"Monster's initial combat strength: {monster.combat_strength}")
    print(f"Monster's initial health points: {monster.health_points}")
    power_roll = random.choice(list(monster_powers.keys()))
    buff = monster_powers[power_roll]
    monster.combat_strength += min(6, buff)
    print(f"Monster boosted with {power_roll} → +{buff} CS → Now: {monster.combat_strength}")

def print_final_scoreboard(heroes, monsters):
    print("\n====== FINAL SCOREBOARD ======")
    print("\nHeroes:")
    for i, hero in enumerate(heroes, 1):
        status = " ☠️" if hero.health_points == 0 else ""
        print(f"Hero #{i}: HP = {hero.health_points}, CS = {hero.combat_strength}{status}")

    print("\nMonsters:")
    for i, monster in enumerate(monsters, 1):
        status = " ☠️" if monster.health_points == 0 else ""
        print(f"Monster #{i}: HP = {monster.health_points}, CS = {monster.combat_strength}{status}")

def run_team_battle():
    print("\n============================")
    print("     5v5 TEAM BATTLE MODE")
    print("============================\n")

    heroes = [Hero() for _ in range(5)]
    monsters = [Monster() for _ in range(5)]

    print("\n--- PREPARING HERO TEAM ---")
    for i, hero in enumerate(heroes):
        print(f"\nHero #{i+1} Setup")
        prepare_hero(hero, loot_options_master)

    print("\n--- ENCHANTING MONSTERS ---")
    for i, monster in enumerate(monsters):
        print(f"\nMonster #{i+1} Magic Roll")
        prepare_monster(monster)

    round_count = 1

    while any(h.health_points > 0 for h in heroes) and any(m.health_points > 0 for m in monsters):
        print(f"\n-------- ROUND {round_count} --------")

        for hero in [h for h in heroes if h.health_points > 0]:
            target = next((m for m in monsters if m.health_points > 0), None)
            if target:
                hero.hero_attacks(target)

        for monster in [m for m in monsters if m.health_points > 0]:
            target = next((h for h in heroes if h.health_points > 0), None)
            if target:
                monster.monster_attacks(target)

        round_count += 1

    print_final_scoreboard(heroes, monsters)

    heroes_alive = [h for h in heroes if h.health_points > 0]
    monsters_alive = [m for m in monsters if m.health_points > 0]

    if len(heroes_alive) > 0:
        print("\n>>> HEROES WIN THE TEAM BATTLE! <<<")
        stars = 1 + len(heroes_alive)
        short_name = "H5v5"
        functions.save_game("Hero", hero_name=short_name, num_stars=stars)
        print(f"Heroes get <{'*' * stars}> stars")
    else:
        print("\n>>> MONSTERS WIN THE TEAM BATTLE! <<<")
        functions.save_game("Monster")


if __name__ == "__main__":
    run_team_battle()
