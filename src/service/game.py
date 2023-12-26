import random

def play_game():
    generated_number = random.randint(0,5)
    print("Your task is to guess the random number generated. Guess the number now.")
    number = int(input("Your guess:"))
    moves_taken=0
    while(number!=generated_number):
        number = int(input("Your guess:"))
        moves_taken+=1
    return moves_taken
