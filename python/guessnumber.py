import random
def game(level):
    number = random.randint(1,level)
    level=100
    guess=int(input("Enter the number : "))
    for i in range(0,8):
        guess=int(input("Enter the number : "))
        if guess==number:
            print(f"You won !! Making the game harder")
            level+=100
            game(level)
            continue
        elif guess>number:
            print("Too High")
            continue
        elif guess<number:
            print("Too Low")
            continue
    print("Game Over! You Lost")
game(100)
    