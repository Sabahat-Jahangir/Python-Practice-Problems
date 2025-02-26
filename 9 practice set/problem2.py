from random import randint
def game():
    print("You are playing the game :) ")
    score = randint(1, 100)
    # Fetch the high score
    with open("hi_score.txt") as f:
        hiscore = f.read()
        hiscore = int(hiscore)

    print(f"Your score is :) {score} ")
    if(score > hiscore):
        # Write this hiscore to the file
        with open("hi_score.txt", "w") as f:
            f.write(str(score))
            
game()
