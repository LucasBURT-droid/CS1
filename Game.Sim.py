import random
print ("Rock,Paper,Scissors Simulator!")
list_weapon = ["Rock","Paper","Scissors"]

while True:
    computer =random.choice (list_weapon) 
    user = (input("Choose Weapon")).capitalize()
    if user == computer:
        print ("tie")
    elif user == "Rock" and computer == "Paper":
        print ("you Lose")
    elif user == "Paper" and computer == "Rock":
        print ("you win")
    elif user == "Scissors" and computer == "Paper":
        print ("you win")
    elif user == "Paper" and computer == "Scissors":
        print ("you Lose")
    elif user == "Rock" and computer == "Scissors":
        print ("you win")
    elif user == "Scissors" and computer == "Rock":
        print ("you Lose")
    else:
        print ("Invalid Response")
        
    play = input (" Play Again? y/n: ")
    
    if play== "y":
        print ("Awesome!")
    elif play == "n":
        print ("Bye!")
        break
    else:
        print ("Invalid Response")
