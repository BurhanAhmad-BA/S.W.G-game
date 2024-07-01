import random

draw = 0
comp_wins = 0
user_wins = 0

while True:
    dict = {"s":1, "w": -1, "g": 0}
    reverse_dict= {1:"Snake", -1:"Water", 0:"Gun"}

    user_choice=input("Enter S for snake, W for water, G for gun: ")
    user_num= dict[user_choice.lower()]

    comp_choice= random.choice([-1, 0, 1])

    print(f"Computer choice is {reverse_dict[comp_choice]} and User choice is {reverse_dict[user_num]}.")
    
    if comp_choice == user_num:
        print ("Its a draw!")
        draw += 1
    else:
        if comp_choice == 1 and user_num == -1:
            print("Computer wins!")
            comp_wins += 1
        elif comp_choice == -1 and user_num == 1:
            print("User wins!")
            user_wins += 1
        elif comp_choice == 0 and user_num == 1:
            print("Computer wins!")
            comp_wins += 1
        elif comp_choice == 1 and user_num == 0:
            print("User wins!")
            user_wins += 1
        elif comp_choice == -1 and user_num == 0:
            print("Computer wins!")
            comp_wins += 1
        elif comp_choice == 0 and user_num == -1:
            print("User wins!")
            user_wins += 1
        else:
            print("Something went Wrong!")
    ext_cont = input("Enter E to exit or any other key to continue: ").lower()
    if ext_cont == "e":
        break

print(f"Total draws: {draw}\nComputer wins: {comp_wins}\nUser wins: {user_wins}")