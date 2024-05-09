import random as rd

number = rd.randint(1,20)
date = rd.randint(23,56)
print("The result is :" , number, date)

def dice_game():
    # Generate a number beetwen 1-6, as a dice.
    return rd.randint(1, 6)

# game dice and print the result.
for _ in range(5):
    result = dice_game()
    print("Result:", result)


