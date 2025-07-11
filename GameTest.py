# Proto-Game #2
# Version: prototype:2.1

TIME = 0
Max_HP = 100
HP = 100
HEAL = 3
ATK = 10
Max_energy = 10
Energy = 10
Energy_regen = 4
Level = 1
EXP = 0
MIN_EXP = 20

RAND = 2.1234
MULTIPLIER = 7.123456789
ADDITIVE = 3.456789
MODULO_LIMIT = 10.0

current_enemy_hp = 0
current_enemy_name = "None"
current_enemy_atk = 0
enemy_rand = 0

print("Welcome to my new Proto-Game!")
print("\nInstructions:")
print("  Press 'a' to Attack: Deal damage, but be mindful of your energy.")
print("  Press 'h' to Heal: Restore HP, consuming some energy.")
print("  Press 'e' to Defence.")
print("  Press 'q' to Parry.")
print("  Type 'quit' to exit the game at any time.")
print("\nPress 'Enter' to start your adventure!")

while input() != "":
    input("")

while HP > 0:
    TIME += 1
    D = 0
    # --- Game State Calculation ---
    RAND = (RAND * MULTIPLIER + ADDITIVE) % MODULO_LIMIT + (TIME * 0.00001)
    FRAN = RAND % 1.0
    SRAN = FRAN * 10000
    RAN4 = int(SRAN) % 10

    if EXP >= MIN_EXP:
        print("\n--- LEVEL UP! ---")
        EXP -= MIN_EXP
        Max_HP += 50
        HEAL += 1
        Max_energy += 5
        ATK += 1
        Energy_regen += 1
        Level += 1
        MIN_EXP += 10
        print(f"You are now Level {Level}!")
        print(f"Max HP: {Max_HP}, ATK: {ATK}, HEAL: {HEAL}, Max Energy: {Max_energy}")

    Energy += Energy_regen
    if Energy > Max_energy:
        Energy = Max_energy
    if HP > Max_HP: # Ensure HP doesn't exceed Max_HP after healing
        HP = Max_HP

    # --- Display Current Turn and Player Status ---
    print("\n" + "="*30)
    print(f"       Turn: {TIME}")
    print("="*30)

    print("\n--- Your Status ---")
    print(f"HP: {round(HP)}/{Max_HP}", " (Full HP)" if HP == Max_HP else "")
    print(f"Energy: {round(Energy)}/{Max_energy}", " (Low energy)" if Energy < 1 and Energy > 0 else (" (Full energy)" if Energy == Max_energy else ""))
    print(f"Level: {Level}")
    print(f"Current EXP: {EXP}/{MIN_EXP}")


    # --- Enemy Encounter Logic ---
    if current_enemy_hp <= 0:
        print("\n--- A New Enemy Appears! ---")
        if 0 <= RAN4 <= 3 or TIME < 2:
            current_enemy_hp = 20 + Level * 2 # Scale enemy HP slightly with level
            current_enemy_atk = 6 + Level # Scale enemy ATK slightly with level
            current_enemy_name = "Goblin"
            if TIME < 2:
                enemy_rand = 1
            else:
                enemy_rand = RAN4

        elif 3 < RAN4 <= 6:
            current_enemy_hp = 40 + Level * 3
            current_enemy_atk = 10 + Level * 1.5
            current_enemy_name = "Ork"
            enemy_rand = RAN4

        elif 6 < RAN4 <= 9 and TIME >= 2:
            current_enemy_hp = 100 + Level * 5
            current_enemy_atk = 15 + Level * 2
            current_enemy_name = "Ogre"
            enemy_rand = RAN4
        
        print(f"You encounter a {current_enemy_name}!")
        enemy_atk = current_enemy_atk

    # --- Display Enemy Status ---
    print("\n--- Enemy Status ---")
    print(f"Enemy: {current_enemy_name}")
    print(f"HP: {round(current_enemy_hp)}")
    print(f"ATK: {round(current_enemy_atk)}")
    
    # --- Player Action Phase ---
    print("\nWhat will you do? ('a' for Attack, 'h' for Heal, 'e' for Defence, 'q' for Parry, 'quit' to exit)")
    user_input = input("> ").lower()

    if user_input == "quit":
        break
    elif user_input == "a":
        attack_cost = round(0.6 * RAN4 + 1)
        if Energy >= attack_cost:
            current_enemy_hp -= ATK * (0.5 * RAN4)
            Energy -= attack_cost
            print(f"You successfully attacked the {current_enemy_name} for {round(ATK * (0.5 * RAN4))} damage!")
        else:
            print(f"Not enough energy to attack! (Requires {attack_cost} energy)")
    elif user_input == "h":
        heal_cost = round(0.8 * RAN4 + 1)
        if Energy >= heal_cost and HP < Max_HP:
            healed_amount = round(HEAL * RAN4)
            HP += healed_amount
            Energy -= heal_cost
            print(f"You successfully healed for {healed_amount} HP!")
            if HP > Max_HP:
                HP = Max_HP # Cap HP at Max_HP
        elif HP >= Max_HP:
            print("You are already at full HP!")
        else:
            print(f"Not enough energy to heal! (Requires {heal_cost} energy)")
    elif user_input == "p":
        parry_cost = 4 * enemy_rand
        if Energy >= parry_cost:
            current_enemy_hp -= 0.5 * current_enemy_atk
            current_enemy_atk = 0
            print(f"You hane succsfully parry enemy attack! Enemy take {round(0.5 * enemy_atk)} damage!")
        else:
            print(f"Not enough energy to parry! (Requires {parry_cost} energy)")
    elif user_input == "d":
        defence_cost = 2 * enemy_rand
        if Energy >= defence_cost:
            D = 2
            Energy -= defence_cost
            print(f"Enemy damage redused in {D} times")
        else:
            print(f"Not enough energy to defence! (Requires {defence_cost} energy)")
    else:
        print("Invalid action. Please choose 'a', 'h', d, p or 'quit'.")

    # --- Enemy Attack Phase ---
    if current_enemy_hp > 0:
        if user_input == "e":
            print(f"\nThe {current_enemy_name} attacks you for {round(current_enemy_atk/D)} damage!")
            HP -= current_enemy_atk/D
        else:
            print(f"\nThe {current_enemy_name} attacks you for {round(current_enemy_atk)} damage!")
            HP -= current_enemy_atk
    current_enemy_atk = enemy_atk
    # --- Post-Action Updates ---
    if Energy < 0: # Ensure energy doesn't go negative
        Energy = 0

    if current_enemy_hp <= 0 and current_enemy_name != "None":
        print(f"\n--- You defeated the {current_enemy_name}! ---")
        exp_gained = round(0.5 * RAN4 * enemy_rand)
        EXP += exp_gained
        print(f"You gained {exp_gained} EXP!")
        current_enemy_name = "None" # Reset enemy for next encounter

    if HP <= 0:
        print("\n--- You have been defeated! ---")
    
    # Pause for user to read before next turn
    if HP > 0:
        print("\nPress Enter to continue...")
        input()

print("\n\n\n--- GAME OVER ---")

while input() != "":
    input("")