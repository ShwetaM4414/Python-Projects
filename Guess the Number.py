from numpy import random

print("------------Number Guessing Game------------\n")
print("You will have 6 turns to win the game.")
print("Pick a number between 0 to 100.\n")
a = 'y'
while a == 'y' or a == 'Y':
    num = random.randint(0, 100)
    i = 1
    turnsLeft = 0
    while i <= 6:
        turnsLeft = 6 - i
        x = input("Guess the number : ")
        while not x.isnumeric():
            print("Invalid Input try again")
            print("Number of turns left : {}\n".format(turnsLeft))
            i += 1
            turnsLeft = 6 - i
            x = input("\nGuess the number : ")

        x1 = int(x)
        if x1 == num:
            print("It took you {} turns to guess the number, which is {} ".format(i, num))
            print("You won!!!!!\n")
            break
        elif x1 > num:
            if x1 - num <= 5:
                print("Your guess is {} which is High and too close to the given number".format(x1))
                print("Number of turns left : {}\n".format(turnsLeft))
            elif x1 - num <= 15:
                print("Your guess is {} which is High and close to the given number".format(x1))
                print("Number of turns left : {}\n".format(turnsLeft))
            elif x1 - num <= 25:
                print("Your guess is {} which is High and away from the given number".format(x1))
                print("Number of turns left : {}\n".format(turnsLeft))
            else:
                print("Your guess is {} which is High and far away from given number".format(x1))
                print("Number of turns left : {}\n".format(turnsLeft))
        else:
            if num - x1 <= 5:
                print("Your guess is {} which is low and too close to the given number".format(x1))
                print("Number of turns left : {}\n".format(turnsLeft))
            elif num - x1 <= 15:
                print("Your guess is {} which is low and close to the given number".format(x1))
                print("Number of turns left : {}\n".format(turnsLeft))
            elif num - x1 <= 25:
                print("Your guess is {} which is low and away from the given number".format(x1))
                print("Number of turns left : {}\n".format(turnsLeft))
            else:
                print("Your guess is {} which is low and far away from given number".format(x1))
                print("Number of turns left : {}\n".format(turnsLeft))

        i += 1
    if i > 6:
        print("Oops!! No turns left. The number is {}.".format(num))
        print("Game Over\n")

    a = input("Do you want to play again if yes then press y else press n : ")

    while a != 'y' and a != 'Y' and a != 'n' and a != 'N':
        print("Invalid Input try again\n")
        a = input("Do you want to play again if yes then press y else press n : ")

    print("---------------------------------------------------------------------------\n")

print("Thanks for playing the game")
