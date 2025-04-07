# maaz_feature.py — Inventory System + Durability
# Feature:
# - Loot belt size limit
# - Equip one item, rest stored in inventory
# - Weapon durability (breaks after 2–3 uses)

import random

belt_limit = 3
loot_items = ["Health Potion", "Poison Potion", "Secret Note", "Leather Boots", "Flimsy Gloves"]
weapons = ["Knife", "Club", "Gun"]  # Simplified weapon pool with durability

class Player:
    def __init__(self):
        self.health = 10
        self.belt = []
        self.weapon = None
        self.weapon_uses_left = 0

    def collect_loot(self, item):
        if len(self.belt) < belt_limit:
            self.belt.append(item)
            print(f"Added {item} to belt.")
        else:
            print("Belt full! Choose one item to drop:")
            for i, it in enumerate(self.belt, 1):
                print(f"{i}. {it}")
            drop = int(input("Drop item #: ")) - 1
            print(f"Dropped {self.belt[drop]}")
            self.belt[drop] = item
            print(f"Added {item} to belt.")

    def equip_weapon(self, weapon):
        self.weapon = weapon
        self.weapon_uses_left = random.randint(2, 3)
        print(f"Equipped {weapon} with {self.weapon_uses_left} durability")

    def attack(self):
        if self.weapon is None or self.weapon_uses_left == 0:
            print("No usable weapon equipped!")
            return 0
        self.weapon_uses_left -= 1
        print(f"Attacked with {self.weapon}. Uses left: {self.weapon_uses_left}")
        if self.weapon_uses_left == 0:
            print(f"Your {self.weapon} broke!")
            self.weapon = None
        return 1


def run_inventory_test():
    print("\n=== INVENTORY SYSTEM TEST ===")
    player = Player()

    for _ in range(5):
        item = random.choice(loot_items)
        player.collect_loot(item)

    print("\nYour belt:", player.belt)

    # Equip weapon with durability
    weapon = random.choice(weapons)
    player.equip_weapon(weapon)

    for i in range(4):
        print(f"\nAttack #{i+1}")
        player.attack()

if __name__ == "__main__":
    run_inventory_test()