import random


def use_loot(belt, health_points):
    good_loot_options = ["Health Potion", "Leather Boots"]
    bad_loot_options = ["Poison Potion"]

    print("    |    !!You see a monster in the distance! So you quickly use your first item:")
    first_item = belt.pop(0)
    if first_item in good_loot_options:
        health_points = min(20, health_points + 2)
        print("    |    You used " + first_item + " to up your health to " + str(health_points))
    elif first_item in bad_loot_options:
        health_points = max(0, health_points - 2)
        print("    |    You used " + first_item + " and it hurt your health to " + str(health_points))
    else:
        print("    |    You used " + first_item + " but it's not helpful")
    return belt, health_points


def collect_loot(loot_options, belt):
    ascii_image3 = """
                      @@@ @@                
             *# ,        @              
           @           @                
                @@@@@@@@                
               @   @ @% @*              
            @     @   ,    &@           
          @                   @         
         @                     @        
        @                       @       
        @                       @       
        @*                     @        
          @                  @@         
              @@@@@@@@@@@@          
              """
    print(ascii_image3)
    loot_roll = random.choice(range(1, len(loot_options) + 1))
    loot = loot_options.pop(loot_roll - 1)
    belt.append(loot)
    print("    |    Your belt: ", belt)
    return loot_options, belt


def inception_dream(num_dream_lvls):
    num_dream_lvls = int(num_dream_lvls)
    if num_dream_lvls == 1:
        print("    |    You are in the deepest dream level now")
        input("    |    Start to go back to real life? (Press Enter)")
        print("    |    You start to regress back through your dreams to real life.")
        return 2
    else:
        return 1 + int(inception_dream(num_dream_lvls - 1))


def load_game():
    try:
        with open("save.txt", "r") as file:
            lines = file.readlines()
            total_monsters = None
            for line in reversed(lines):
                if line.startswith("Total monsters killed:"):
                    total_monsters = int(line.strip().split(":")[1])
                    break
            if total_monsters is not None:
                print("Total monsters killed (including all past games):", total_monsters)
                return total_monsters
            else:
                print("No total monsters count found.")
                return 0
    except FileNotFoundError:
        print("No previous game found. Starting fresh.")
        return 0


def save_game(winner, hero_name="", num_stars=0):
    total = 0
    try:
        with open("save.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith("Total monsters killed:"):
                    total = int(line.strip().split(":")[1])
    except FileNotFoundError:
        total = 0

    if winner == "Hero":
        total += 1

    with open("save.txt", "a") as file:
        if winner == "Hero":
            file.write(f"Hero {hero_name} has killed a monster and gained {num_stars} stars.\n")
        elif winner == "Monster":
            file.write("Monster has killed the hero previously\n")
        file.write(f"Total monsters killed: {total}\n")


def adjust_combat_strength(hero_cs, monster_cs):
    # this partt will Use the last total monsters killed from the save file as a simple adjustment metric.
    last_total = load_game()
    if last_total and last_total > 3:
        print("    |    ... Increasing the monster's combat strength since you won so easily last time")
        monster_cs += 1
    else:
        print("    |    ... No adjustments to combat strength based on previous game.")
    return hero_cs, monster_cs
