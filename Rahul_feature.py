# status_effect_feature.py — Status Effects System
# Feature: Apply status effects like poison, burn, regeneration, stun to characters

import random
from hero import Hero
from monster import Monster


def apply_status_effect(entity, effect):
    if effect == 'poison':
        damage = 2
        entity.health_points = max(0, entity.health_points - damage)
        print(f"💀 {entity.__class__.__name__} is poisoned! Loses {damage} HP. Current HP: {entity.health_points}")

    elif effect == 'burn':
        damage = 3
        entity.health_points = max(0, entity.health_points - damage)
        print(f"🔥 {entity.__class__.__name__} is burned! Loses {damage} HP. Current HP: {entity.health_points}")

    elif effect == 'regen':
        if entity.health_points < 20:
            heal = 2
            entity.health_points = min(20, entity.health_points + heal)
            print(f"✨ {entity.__class__.__name__} regenerates {heal} HP. Current HP: {entity.health_points}")

    elif effect == 'stun':
        stunned = random.choice([True, False])
        if stunned:
            print(f"⚡ {entity.__class__.__name__} is stunned and loses a turn!")
        return stunned

    return False


def test_status_effects():
    hero = Hero()
    monster = Monster()
    hero.health_points = 15
    monster.health_points = 10

    print("\n=== STATUS EFFECT TEST MODE ===")
    effects = ['poison', 'burn', 'regen', 'stun']

    for effect in effects:
        print(f"\nApplying '{effect}' to Hero:")
        apply_status_effect(hero, effect)
        print(f"Applying '{effect}' to Monster:")
        apply_status_effect(monster, effect)


if __name__ == "__main__":
    test_status_effects()
