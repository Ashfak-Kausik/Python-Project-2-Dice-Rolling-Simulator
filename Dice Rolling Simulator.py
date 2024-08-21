import random

def roll_dice():
    return random.randint(1, 6)

# Main loop
while True:
    print("Rolling the dice...")
    print(f"You rolled a {roll_dice()}!")
    
    again = input("Roll again? (y/n): ").lower()
    if again != 'y':
        break
