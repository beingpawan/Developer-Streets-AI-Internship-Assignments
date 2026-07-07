import random as random;
jackpot = random.randint(1,100)
guess = int(input("Guess the number between 1 and 100: "))
counter=1
while(guess !=jackpot):
    if (guess<jackpot):
        print("Guess higher")
    else:
        print("Guess lower")
    guess=int(input("Guess again: "))
    counter+=1
print(f"Sahi jawaab !! You took {counter} guesses.")
