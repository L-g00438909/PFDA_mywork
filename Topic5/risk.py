import numpy as np
import matplotlib.pyplot as plt

# Number of rounds to simulate
n_repeats = 1000

# To store the number of losses for attacker and defender
attacker_losses = 0
defender_losses = 0

# Simulate 1000 battle rounds
for _ in range(n_repeats):
    # Step 1: Simulate dice rolls (attacker and defender have varying units)
    # Let's assume the attacker has 3 units and defender has 2 units (you can change these values)
    attacker_units = 3  # Example: attacker has 3 units
    defender_units = 2  # Example: defender has 2 units

    # Attacker rolls up to 3 dice, defender rolls up to 2 dice, based on their units
    attacker_dice_count = min(attacker_units, 3)  # Attacker can roll at most 3 dice
    defender_dice_count = min(defender_units, 2)  # Defender can roll at most 2 dice
    
    # Simulate the dice rolls for attacker and defender
    attacker_dice = np.sort(np.random.randint(1, 7, attacker_dice_count))[::-1]  # Sort in descending order
    defender_dice = np.sort(np.random.randint(1, 7, defender_dice_count))[::-1]  # Sort in descending order

    # Step 2: Compare dice rolls (highest attacker die vs highest defender die, etc.)
    for i in range(min(len(attacker_dice), len(defender_dice))):  # Compare based on the number of dice
        if attacker_dice[i] > defender_dice[i]:  # Attacker wins this comparison
            defender_losses += 1
        else:  # Defender wins this comparison
            attacker_losses += 1

# Step 3: Plot the results
attacker_loss_percentage = (attacker_losses / (n_repeats * 2)) * 100  # 2 is the total number of comparisons per round
defender_loss_percentage = (defender_losses / (n_repeats * 2)) * 100  # 2 comparisons per round

# Plotting the bar chart
labels = ['Attacker Losses', 'Defender Losses']
values = [attacker_loss_percentage, defender_loss_percentage]

plt.bar(labels, values, color=[ 'darkblue', 'magenta'])
plt.ylabel('Losses Percentage (%)')
plt.title('Attacker and Defender Losses in Risk Battle Simulation')
plt.show()
#save the plot
plt.savefig('risk_battle_simulation.png')