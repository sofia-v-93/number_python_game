#gess my number python game

import random

secret=random.randint(1,30)
attempts=0

with open("score.txt", "r") as score_file:
    best_score = int(score_file.read())
    print("Top score attempts: " + str(best_score))

while True:
    guess=int(input("Guess a number between 1 and 30:"))
    attempts += 1 #attempts=attempts+1

    if guess==secret:
        if attempts  < best_score:
            with open("score.txt","w") as score_file:
                score_file.write(str(attempts))
        print("correct")
        print("attempts needed: " + str(attempts))
        break
    elif guess>secret:
        print("your guess is too high")
    elif guess<secret:
        print("your guess is too small")