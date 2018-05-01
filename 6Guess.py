#6 chances to guess a number randomly generated from 1-100
import random
Name = input("Please enter your name:")
Name = str(Name)
print("Let's start the guessing number game,%s"%(Name))
def game():
    num = random.randint(0,100)
    #print(num)
    print("I have selected my number!")
    print("You have 6 chances to guess it!")
    i = 1
    r = 1
    while i < 7:
        GuestGuess = input("Please enter your guess:")
        try:
            if 0<=int(GuestGuess)<=100 and int(GuestGuess) < num:
                print("Your Guess is smaller than my number!")
                print("You still have %d chances!"%(6-i))
                i += 1
                #continue
            elif 0<=int(GuestGuess)<=100 and int(GuestGuess) > num:
                print("Your Guess is larger than my number!")
                print("You still have %d chances!"%(6-i))
                i += 1
                #continue
            elif 0<=int(GuestGuess)<=100 and int(GuestGuess) == num:
                print("You are right!")
                r = 0
                break
            else:
                print("Your number is invalid")
                print("You still have %d chances!"%(6-i+1))
                continue
        except:
            print("You did not enter an integer!")
            print("You still have %d chances!"%(6-i+1))
            continue
    if r == 1:
        print("Sorry! You lose the game! My number is %d"%(num))
game()
while True:
    another_game=input("Would you like another game?(y for yes / n for no):")
    if another_game.lower()=='y':
        game()
    elif another_game.lower()=='n':
        print("No more games!")
        break
    elif another_game.lower()!='y' and another_game.lower()!='n':
        print("Please enter y for yes and n for no!")
        
    
        
















