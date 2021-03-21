import random

def intro():
    print("Hi welcome to our fun game")
    print("This is a rock paper scissors game with computer")
    print("Choose a value between P R S")


def main_game():
    intro()
    my_point = 0
    op_point = 0
    while True:
        if my_point < 3 and op_point < 3:
            our_choice = input("Enter a value: ")
            choices = ["R" , "P" , "S"]
            opponent_move = random.choice(choices)
            if our_choice == "S" or our_choice == "P" or our_choice == "R":
                print(our_choice,"VS",opponent_move)
                if our_choice == opponent_move:
                    print("Tie")
                elif our_choice == "R" and opponent_move == "S" or our_choice == "P" and opponent_move == "R" or our_choice == "S" and opponent_move == "P":
                    print("User won")
                    my_point += 1
                else:
                    print("computer won!")
                    op_point += 1
            else:
                print("Undifind input")
        else:
            if my_point == 3:
                print("Real user won!")
            else:
                print("Robot won!")
            break
        print("Your score ->",my_point,"Computer score ->",op_point)



main_game()

