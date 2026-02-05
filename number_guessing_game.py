import random, sys
while True:
    
    print("----Difficulty levels----")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    print("4. Exit")

    ch=int(input("Enter choice:"))

    if ch==1:
        while True:
            print("The number is between 1 to 10.")
            num=random.randint(1,10)
            count=0

            while True:
                guess=int(input("Guess the number: "))
                count+=1

                if guess<=0 or guess>10:
                    print("The number is between 1 to 10.")

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
    elif ch==2:
        while True:
            print("The number is between 1 to 50.")
            num=random.randint(1,50)
            count=0

            while True:
                guess=int(input("Guess the number: "))
                count+=1

                if guess<=0 or guess>50:
                    print("The number is between 1 to 10.")

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

    elif ch==3:
        while True:
            print("The number is between 1 to 100.")
            num=random.randint(1,100)
            count=0

            while True:
                guess=int(input("Guess the number: "))
                count+=1

                if guess<=0 or guess>100:
                    print("The number is between 1 to 100.")

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


