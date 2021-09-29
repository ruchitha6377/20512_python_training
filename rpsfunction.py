def rpc(player1,player2):
    if (player1==player2):
        print("its a tie!!")
    elif player1=="rock":
        if player2=="scissors":
            print("player1 is the winner")
        else:
             print("player2 is winner")
    elif player1=="paper":
        if player2=="rock":
            print("player1 is winner")
        else:
            print("player2 is winner")
    elif player1=="scissors":
        if player2=="paper":
            print("player1 is winner")
        else:
             print("player2 is winner")
    ans = input("wanna play again?(yes or no):")
    if ans == "no":
        print("thanks for playing!!")
rpc("rock","rock")