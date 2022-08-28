import random

# suit = ['Spade', 'Heart', 'Club', 'Diamond']
# rank = ['Ace', 'King', 'Queen', 'Joker', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']


Cards = {
    "Spade": ['Ace', 'King', 'Queen', 'Joker', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
    "Heart": ['Ace', 'King', 'Queen', 'Joker', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
    "Club": ['Ace', 'King', 'Queen', 'Joker', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
    "Diamond": ['Ace', 'King', 'Queen', 'Joker', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
}


def PickACard():
    X = random.choice((list(Cards.keys())))
    print(X, end=" ")
    print(Cards[X][random.randint(0, 13)])


a = 1
while a == 1:
    try:
        x = int(input("How many playing cards you want to pick : "))
        while x > 52:
            print("Value must be less than or equal to 52, Try again\n")
            x = int(input("How many playing cards you want to pick : "))
        a = 0

    except ValueError:
        print("Invalid Input, Try again\n")
        a = 1
    else:
        for i in range(x):
            PickACard()
