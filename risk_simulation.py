import random

def roll_dice(n):
    return sorted([random.randint(1, 6) for _ in range(n)], reverse=True)

def simulate_battle(num_attackers, num_defenders):
    while num_attackers > 1 and num_defenders > 0:
        num_dice_attackers = min(num_attackers - 1, 3)
        num_dice_defenders = min(num_defenders, 2)

        attacker_dice = roll_dice(num_dice_attackers)
        defender_dice = roll_dice(num_dice_defenders)

        for a, d in zip(attacker_dice, defender_dice):
            if a > d:
                num_defenders -= 1
            else:
                num_attackers -= 1

    return num_attackers, num_defenders

def simulate_game(initial_attackers, initial_defenders, num_simulations= 1000000):
    attacker_wins = 0

    for _ in range(num_simulations):
        num_attackers, num_defenders = simulate_battle(initial_attackers, initial_defenders)
        if num_defenders == 0:
            attacker_wins += 1

    win_rate = attacker_wins / num_simulations
    return win_rate

endit = 0
attackrollers = 11
defendrollers = 11
passon = 0

# Open the file in write mode
with open('output.txt', 'w') as f:
    while(endit == 0):
        # Test the function
        initial_attackers = attackrollers
        initial_defenders = defendrollers
        win_rate = simulate_game(initial_attackers, initial_defenders)
        win_rate_decimal = win_rate * 100
        
        if(win_rate_decimal < 0.01):
            f.write(f"With {initial_attackers -1} attacking dice against {initial_defenders} defending dice, the attackers win {win_rate_decimal}% of the time.\n")
            print(f"With {initial_attackers -1} attacking dice against {initial_defenders} defending dice, the attackers win {win_rate_decimal}% of the time.")
        else:            
        # Write the output to the file
            f.write(f"With {initial_attackers -1} attacking dice against {initial_defenders} defending dice, the attackers win {win_rate_decimal}% of the time.\n")
            print(f"With {initial_attackers -1} attacking dice against {initial_defenders} defending dice, the attackers win {win_rate_decimal}% of the time.")

        attackrollers -= 1

        if(attackrollers == 1 and passon == 0 ):
            defendrollers -= 1
            attackrollers = 11
        if(defendrollers == 0):
            passon = 1
            break  # Use break instead of exit to close the file properly