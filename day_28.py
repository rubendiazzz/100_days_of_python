import random as ran
import os
import time

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def generate_epic_names(base_name, count=3):
    epic_suffixes = ["the Brave", "the Mighty", "the Wise", "the Fierce", "of the North", "Shadowbane", "Ironheart", "the Conqueror", "the Mystic", "Starwalker"]
    epic_names = []

    for _ in range(count):
        suffix = ran.choice(epic_suffixes)
        epic_name = f"{base_name} {suffix}"
        epic_names.append(epic_name)

    return epic_names

def character_builder():
    base_name = input("Enter the base name for your legend: ")
    epic_names = generate_epic_names(base_name)
    print("\nGenerated Epic Names:")
    for name in epic_names:
        print(name)
    legend_name = ran.choice(epic_names)  # Randomly choose one of the epic names
    character_type = input("\nCharacter type (Human, Elf, Wizard, Orc): ")
    char_health = health()
    char_strength = strength()
    return {"name": legend_name, "type": character_type, "health": char_health, "strength": char_strength}

def health():
    six_sided_roll = ran.randint(1, 6)
    twelve_sided_roll = ran.randint(1, 12)
    random_health = ((six_sided_roll + twelve_sided_roll) / 2) + 10
    return random_health

def strength():
    six_sided_roll = ran.randint(1, 6)
    twelve_sided_roll = ran.randint(1, 12)
    random_strength = ((six_sided_roll + twelve_sided_roll) / 2) + 12
    return random_strength

def battle(char1, char2):
    round_number = 1
    while char1["health"] > 0 and char2["health"] > 0:
        clear_screen()
        print(f"⚔️ BATTLE TIME ⚔️\nThe battle continues! Round {round_number}\n")

        roll_char1 = ran.randint(1, 6)
        roll_char2 = ran.randint(1, 6)

        if roll_char1 > roll_char2:
            winner, loser = char1, char2
        else:
            winner, loser = char2, char1

        damage = abs(winner["strength"] - loser["strength"]) + 1

        # Check for a critical hit
        if ran.random() < 0.2:  # 20% chance for a critical hit
            damage *= 2
            print("💥 Critical Hit! 💥")

        loser["health"] -= damage

        print(f"{winner['name']} wins this round!")
        print(f"{loser['name']} takes a hit, with {damage} damage")
        print(f"{char1['name']} HEALTH: {char1['health']}")
        print(f"{char2['name']} HEALTH: {char2['health']}")

        if char1["health"] <= 0 or char2["health"] <= 0:
            break

        round_number += 1
        time.sleep(2)

    clear_screen()
    winner_name = char1["name"] if char1["health"] > 0 else char2["name"]
    print(f"⚔️ BATTLE TIME ⚔️\nOh no! {loser['name']} has died!\n{winner_name} wins the battle in {round_number} rounds!")

print("Character builder")
character1 = character_builder()
character2 = character_builder()
battle(character1, character2)