from days_13_15_text_based_games_classes.day_13.dnd_game.actors import Creature, Tiger, RatKing, Wizard
import random


def print_header():
    print("==============================")
    print("==== W I Z A R D  G A M E ====")
    print("==============================")
    print("== Dungeon Exploration Game ==")


def game_loop():
    creatures = [
        Creature(name="Bat", level=15, habitat="Sewer"),
        Creature(name="Rat", level=5, habitat="Sewer"),
        RatKing(name="Leader of the Rats", level=25, habitat="Sewer", number_of_underlings=15),
        Creature(name="Spider", level=20, habitat="Jungle"),
        Tiger(name="Jungle King", level=50, habitat="Jungle", intimidation=1.5, color="Orange"),
    ]
    hero = Wizard(name="Steven", level=15)
    scenes = {'Sewer': ["around the corner", "out of a nearby grate", "a dark spot above you"],
              'Jungle': ['behind a tree', 'within a bush', 'from underfoot']}
    current_scene = random.choice(list(scenes.keys()))  # Randomly choose a scene
    possible_creatures = []
    for creature in creatures:
        if creature.habitat == current_scene:
            possible_creatures.append(creature)
    selected_creature = random.choice(possible_creatures)
    creature_location = random.choice(scenes.get(current_scene))
    print(f"You find yourself in a {current_scene.lower()}")
    while True:
        print(f"A level {selected_creature.level} {selected_creature.name} has appeared from {creature_location}\n")
        cmd = input("Do you: [a]ttack, [r]un away, or [l]ook around?\n")
        if cmd == 'a' or cmd == 'attack':
            if hero.attack(selected_creature):
                possible_creatures.remove(selected_creature)
            else:
                break
        elif cmd == 'r' or cmd == 'run':
            print(f"{hero.name} runs away like a little sissy.")
        elif cmd == 'l' or cmd == 'look':
            print(f"You are in the middle of a {current_scene.lower()}.")
            print(f"You sense some creatures:")
            for c in possible_creatures:
                print(f"{c.name} -- {c.level}")
                print('----------------------')
            continue

        creature_location = random.choice(scenes.get(current_scene))
        selected_creature = random.choice(possible_creatures)

        if not creatures:
            print(f"{hero.name} has defeated all of the creatures! Congratulations!")
            break


def main():
    print_header()
    game_loop()

if __name__ == '__main__':
    main()