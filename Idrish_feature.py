# idrish_feature.py — Critical Hits / Misses
# Feature: 10% chance for critical hit (2x damage) or complete miss (0 damage) for both hero and monster

import random
from hero import Hero
from monster import Monster

CRITICAL_CHANCE = 0.1
MISS_CHANCE = 0.1

small_dice_options = list(range(1, 7))

def attack_with_crit(attacker, defender, attacker_type="Hero"):
    roll = random.random()
    damage = attacker.combat_strength

    if roll < MISS_CHANCE:
        damage = 0
        print(f"{attacker_type} MISSED the attack!")
    elif roll < MISS_CHANCE + CRITICAL_CHANCE:
        damage *= 2
        print(f"{attacker_type} landed a CRITICAL HIT! ({damage} damage)")
    else:
        print(f"{attacker_type} hit normally for {damage} damage")

    # Use the take_damage method from Character class to handle health reduction
    defender.take_damage(damage)
    print(f"{attacker_type} dealt {damage} damage. Defender HP now: {defender.health_points}")


def run_critical_combat():
    print("\n=== CRITICAL HIT TEST MODE ===")
    hero = Hero("Hero")  # Initialize with a name for clarity
    monster = Monster("Monster")  # Initialize with a name for clarity

    print(f"Hero HP: {hero.health_points}, CS: {hero.combat_strength}")
    print(f"Monster HP: {monster.health_points}, CS: {monster.combat_strength}")

    round_count = 1
    while hero.health_points > 0 and monster.health_points > 0:
        print(f"\n--- Round {round_count} ---")
        if random.choice([True, False]):
            attack_with_crit(hero, monster, "Hero")
            if monster.health_points > 0:
                attack_with_crit(monster, hero, "Monster")
        else:
            attack_with_crit(monster, hero, "Monster")
            if hero.health_points > 0:
                attack_with_crit(hero, monster, "Hero")
        round_count += 1

    print("\n=== RESULT ===")
    if hero.health_points > 0:
        print("Hero wins!")
    else:
        print("Monster wins!")

if __name__ == "__main__":
    run_critical_combat()
