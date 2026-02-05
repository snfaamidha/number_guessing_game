import random, sys
def num_game(max_num):
    while True:
            print(f"The number is between 1 to {max_num}.")
            num=random.randint(1,max_num)
            count=0

            while True:
                guess=int(input("Guess the number: "))
                count+=1

                if guess<=0 or guess>max_num:
                    print(f"The number is between 1 to {max_num}.")

                elif guess>num:
                    print("Too high.")

                elif guess<num:
                    print("Too low.")

                elif guess==num:
                    print(f"Correct! The number was {num}.")
                    print(f"You guessed in {count} times.")
                    break

                else:
                    print("Guess a number.")

            while True:
                play=input("Play again? (Y/N): ").lower()
                if play=="y":
                    break
                elif play=="n":
                    break
                else:
                    print("Enter Y or N.")

            if play=="n":
                break

while True:
    
    print("----Difficulty levels----")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    print("4. Exit")

    ch=int(input("Enter choice:"))

    if ch==1:
        num_game(10)

    elif ch==2:   
        num_game(50)

    elif ch==3:
        num_game(100)

    else:
        sys.exit()