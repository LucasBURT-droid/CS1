import random
'''
Name: Lucas Burt 
Date: 11/14/24
Bugs:
Bonuses: Score System,Play Again,Extra Weapon,Multiplayer  

'''




score = 0                                                               #
print ("Rock,Paper,Scissors Simulator!") 
list_weapon = ["Rock","Paper","Scissors","Gun"]


gamemode = input("User vs. User or User vs. Computer? user/computer: ").lower()
if gamemode == "computer":
    while True:
        computer =random.choice (list_weapon) 
        user = (input("Choose Weapon: ")).capitalize()
        if user == computer:
            print ("tie")
        elif user == "Rock" and computer == "Paper":
            print ("you Lose")
            score=score-1
            print(score) 
        elif user == "Paper" and computer == "Rock":
            print ("you win")
            score=score+1
            print(score) 
        elif user == "Scissors" and computer == "Paper":
            print ("you win")
            score=score+1
            print(score) 
        elif user == "Paper" and computer == "Scissors":
            print ("you Lose")
            score=score-1
            print(score) 
        elif user == "Rock" and computer == "Scissors":
            print ("you win")
            score=score+1
            print(score) 
        elif user == "Scissors" and computer == "Rock":
            print ("you Lose")
            score=score-1
            print(score)
        elif user == "Gun" and computer == "Rock":
            print ("you win")
            score=score+1
            print(score)
        elif user == "Rock" and computer == "Gun":
            print ("you lose")
            score=score-1
            print(score)
        elif user == "Gun" and computer == "Scissors":
            print ("you win")
            score=score+1
            print(score)
        elif user == "Scissors" and computer == "Gun":
            print ("you lose")
            score=score-1
            print(score)
        elif user == "Gun" and computer == "Paper":
            print ("you win")
            score=score+1
            print(score)
        elif user == "Paper" and computer == "Gun":
            print ("you lose")
            score=score-1
            print(score) 
        else:
            print ("Invalid Response")
            
        play = input ("Play Again? y/n: ")
        
        if play== "y":
            print ("Ok!")
        elif play == "n":
            print ("Thanks For Playing!")
            break
        else:
            print ("Invalid Response")
elif gamemode == "user":
    while True:
        user2 = (input("Choose Weapon: ")).capitalize()
        user1 = (input("Choose Weapon: ")).capitalize()
        if user1 == user2:
            print ("tie")
        elif user1 == "Rock" and user2 == "Paper":
            print ( " user1 lost")
            score=score-1
            print(score) 
            print (" user2 won") 
            score=score+1
            print(score) 
        elif user1 == "Paper" and user2 == "Rock":
            print ( " user1 won")
            score=score-1
            print(score) 
            print (" user2 lost") 
            score=score+1
            print(score) 
        elif user1 == "Scissors" and user2 == "Paper":
            print ( " user1 won")
            score=score+1
            print(score) 
            print (" user2 lost") 
            score=score-1 
            print(score) 
        elif user1 == "Paper" and user2 == "Scissors":
            print ( " user1 lost")
            score=score-1
            print(score) 
            print (" user2 won") 
            score=score+1
            print(score) 
        elif user1 == "Rock" and user2 == "Scissors":
            print ( " user1 won")
            score=score+1
            print(score) 
            print (" user2 lost") 
            score=score-1
            print(score) 
        elif user1 == "Scissors" and user2 == "Rock":
            print ( " user1 lost")
            score=score-1
            print(score) 
            print (" user2 won") 
            score=score+1
            print(score) 
        elif user1 == "Gun" and user2 == "Rock":
            print ( " user1 won")
            score=score+1
            print(score) 
            print (" user2 lost") 
            score=score-1
            print(score) 
        elif user1 == "Rock" and user2 == "Gun":
            print ( " user1 lost")
            score=score-1
            print(score) 
            print (" user2 won") 
            score=score+1
            print(score) 
        elif user1 == "Gun" and user2 == "Scissors":
            print ( " user1 won")
            score=score+1
            print(score) 
            print (" user2 lost") 
            score=score-1
            print(score) 
        elif user1 == "Scissors" and user2 == "Gun":
            print ( " user1 lost")
            score=score-1
            print(score) 
            print (" user2 won") 
            score=score+1
            print(score) 
        elif user1 == "Gun" and user2 == "Paper":
            print ( " user1 won")
            score=score+1
            print(score) 
            print (" user2 lost") 
            score=score-1
            print(score) 
        elif user1 == "Paper" and user2 == "Gun":
            print ( " user1 lost")
            score=score-1
            print(score) 
            print (" user2 won") 
            score=score+1
            print(score) 
        else:
            print ("Invalid Response")
            
        play = input ("Play Again? y/n: ")
        
        if play== "y":
            print ("Ok!")
        elif play == "n":
            print ("Thanks For Playing!")
            break
        else:
            print ("Invalid Response")
