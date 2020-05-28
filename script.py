import random

# track user and computer wins
user_wins = 0
computer_wins = 0
collective_rounds = user_wins + computer_wins
choices = ["r", "p", "s"]


# keep playing for best of three out of five
while collective_rounds != 5:

    print("=======================")
    print("User: " + str(user_wins))
    print("Computer:" + str(computer_wins))
    print("=======================")
    print

    # prompt user. If user is not r p or s prompt the user again
    user_input = input("r, p, s?: ")
    computer_input = choices[random.randint(0, 2)]

    # if the user inputs something invalid exit out of this iteration
    if user_input != "r" and user_input != "p" and user_input != "s":
        print
        print("Invalid input")
        print

    # Check if the user and
    elif user_input == computer_input:
        print
        print("you tied")
        print

    # Check if the user won a round if yes award the user a point
    elif (user_input == "r" and computer_input == "s") or (user_input == "p" and computer_input == "r") or (user_input == "s" and computer_input == "p"):
        print
        print("You won a round!")
        print
        user_wins += 1

    # If anything else the user lost
    else:
        print("You lost this round")
        computer_wins += 1

    # add the user and computer round to check what round you are on
    collective_rounds = user_wins + computer_wins

if user_wins > computer_wins:
    print
    print("Your won ")

else:
    print
    print("Your lost")
