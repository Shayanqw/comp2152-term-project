import os
import platform
import random
from hero import Hero
from monster import Monster
import functions

print("Operating System:", os.name)
print("Python version:", platform.python_version())


# dice options:
small_dice_options = list(range(1, 7))
big_dice_options = list(range(1, 21))

# the Weapons:
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

# the Loot options and belt:
loot_options = ["Health Potion", "Poison Potion", "Secret Note", "Leather Boots", "Flimsy Gloves"]
belt = []

# Monster's Powers:
monster_powers = {
    "Fire Magic": 2,
    "Freeze Time": 4,
    "Super Hearing": 6
}

# number of stars awarded at the end:
num_stars = 0

# The Hero and Monster objects
hero = Hero()
monster = Monster()

print("Hero's initial combat strength:", hero.combat_strength)
print("Hero's initial health points:", hero.health_points)
print("Monster's initial combat strength:", monster.combat_strength)
print("Monster's initial health points:", monster.health_points)

# Roll for the Hero's Weapon

print("    |", end="    ")
input("Roll the dice for your weapon (Press Enter)")

ascii_image5 = """
              , %               .           
   *      @./  #         @  &.(         
  @        /@   (      ,    @       # @ 
  @        ..@#% @     @&*#@(         % 
   &   (  @    (   / /   *    @  .   /  
     @ % #         /   .       @ ( @    
                 %   .@*                
               #         .              
             /     # @   *              
                 ,     %                
            @&@           @&@
            """
print(ascii_image5)

weapon_roll = random.choice(small_dice_options)
print("    |    The hero's weapon is", weapons[weapon_roll - 1])

# Adjust hero's combat strength using the weapon roll (limit maximum to 6)
hero.combat_strength = min(6, hero.combat_strength + weapon_roll)

# this part will Adjust combat strength based on previous game results

new_hero_cs, new_monster_cs = functions.adjust_combat_strength(hero.combat_strength, monster.combat_strength)
hero.combat_strength = new_hero_cs
monster.combat_strength = new_monster_cs

# Analyze the Weapon Roll
input("Analyze the Weapon roll (Press Enter)")
if weapon_roll <= 2:
    print("--- You rolled a weak weapon, friend")
elif weapon_roll <= 4:
    print("--- Your weapon is meh")
else:
    print("--- Nice weapon, friend!")

if weapons[weapon_roll - 1] != "Fist":
    print("--- Thank goodness you didn't roll the Fist...")

print("    |", end="    ")
input("Roll the dice for your health points (Press Enter)")
print("    |    Your health points:", hero.health_points)

# Roll for the Monster's Health Points
#  already have random HP from Monster class constructor

print("    |", end="    ")
input("Roll the dice for the monster's health points (Press Enter)")
print("    |    Monster's health points:", monster.health_points)

# Collect Loot
print("    |    !!You find a loot bag!! You look inside to find 2 items:")
print("    |", end="    ")
input("Roll for first item (Press Enter)")
loot_options, belt = functions.collect_loot(loot_options, belt)
print("    |    Belt after first loot:", belt)

print("    |", end="    ")
input("Roll for second item (Press Enter)")
loot_options, belt = functions.collect_loot(loot_options, belt)
print("    |    You're super neat, so you organize your belt alphabetically:")
belt.sort()
print("    |    Your belt:", belt)

# Use Loot
belt, updated_health = functions.use_loot(belt, hero.health_points)
hero.health_points = updated_health

# Dream Levels input that usess try-except for validation

while True:
    try:
        num_dream_lvls = int(input("How many dream levels do you want to go down? (Enter a number 0-3): "))
        if 0 <= num_dream_lvls <= 3:
            break
        else:
            print("Please enter an integer between 0 and 3.")
    except ValueError:
        print("Invalid input. Please enter a whole number between 0 and 3.")

if num_dream_lvls != 0:
    # Deduct a small health penalty and adjust combat strength based on dream level
    hero.health_points = max(0, hero.health_points - 1)
    crazy_level = functions.inception_dream(num_dream_lvls)
    hero.combat_strength += crazy_level
    print("After dream levels, hero's combat strength:", hero.combat_strength)
    print("After dream levels, hero's health points:", hero.health_points)

# Roll for the Monster's Power
print("    |", end="    ")
input("Roll for Monster's Magic Power (Press Enter)")

ascii_image4 = """
                @%   @                      
         @     @                        
             &                          
      @      .                          

     @       @                    @     
              @                  @      
      @         @              @  @     
       @            ,@@@@@@@     @      
         @                     @        
            @               @           
                 @@@@@@@                

                                      """
print(ascii_image4)

# Randomly pick one of the monster's powers and boost monster's combat strength
power_roll = random.choice(list(monster_powers.keys()))
monster.combat_strength += min(6, monster_powers[power_roll])
print(f"    |    The monster's combat strength is now {monster.combat_strength} using the {power_roll} magic power")

# Fight Sequence:

print("    |    You meet the monster. FIGHT!!")
while monster.health_points > 0 and hero.health_points > 0:
    input("Roll to see who strikes first (Press Enter)")
    attack_roll = random.choice(small_dice_options)
    if attack_roll % 2 != 0:
        input("You strike (Press Enter)")
        hero.hero_attacks(monster)
        if monster.health_points == 0:
            num_stars = 3
            break
        else:
            input("Monster strikes (Press Enter)")
            monster.monster_attacks(hero)
            if hero.health_points == 0:
                num_stars = 1
                break
            else:
                num_stars = 2
    else:
        input("Monster strikes (Press Enter)")
        monster.monster_attacks(hero)
        if hero.health_points == 0:
            num_stars = 1
            break
        else:
            input("The hero strikes (Press Enter)")
            hero.hero_attacks(monster)
            if monster.health_points == 0:
                num_stars = 3
                break
            else:
                num_stars = 2

if monster.health_points <= 0:
    winner = "Hero"
else:
    winner = "Monster"

# Final Score Display: ask for hero name (two words) and validate

tries = 0
short_name = "Hero"  # fallback if user fails
while tries < 5:
    hero_name = input("Enter your Hero's name (in two words): ")
    name_parts = hero_name.split()
    if len(name_parts) != 2:
        print("Please enter a name with two parts (separated by a space).")
        tries += 1
    elif not (name_parts[0].isalpha() and name_parts[1].isalpha()):
        print("Please enter an alphabetical name.")
        tries += 1
    else:
        short_name = name_parts[0][:2] + name_parts[1][0]
        print("I'm going to call you", short_name, "for short")
        break

stars_display = "*" * num_stars
print("Hero", short_name, "gets <", stars_display, "> stars")

# Save the game result inside a text file called save.txt
functions.save_game(winner, hero_name=short_name, num_stars=num_stars)
