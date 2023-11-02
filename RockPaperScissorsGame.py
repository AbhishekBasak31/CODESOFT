import os
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Put rock paper and scissors in a list named as game.
game=[rock,paper,scissors]

#Initialize the user_score and system_score.
user_score=0
systems_score=0
game_over=False

def outup():
   print(f"Current score:\n user score: {user_score}  systems score : {systems_score} \n") 


while (not game_over):
   
    os.system('cls')
    outup()
    
    #Take user input
    choice_of_user=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    
    #Check the user input is valid or not.
    if choice_of_user<0 and choice_of_user>2:
        print("Invalid Input")
        break
    
    #Display the user choice and system choice.
    print("Your choice:\n")
    print(game[choice_of_user])
    random_num=random.randint(0,2)
    print("System's choice:\n")
    print(game[random_num])

    #Check who is the winner and display that.
    if(choice_of_user==0 and random_num==2 ):  
        print("YOU WON")
        user_score=user_score+1
    elif(choice_of_user==2 and random_num==0):
        print("System WON")
        systems_score=systems_score+1
    elif(choice_of_user==1 and random_num==2):
        print("System WON")
        systems_score=systems_score+1
    elif(choice_of_user==2 and random_num==1):
        print("YOU WON")
        user_score=user_score+1
    elif(choice_of_user==1 and random_num==0):
        print("YOU WON")
        user_score=user_score+1
    elif(choice_of_user==0 and random_num==1):
        print("System WON")
        systems_score=systems_score+1
    else:
        print("DRAW")
        user_score=user_score+0
        systems_score=systems_score+0
        
    #Ask user to continue or not .
    choice=input("Do you like to continue?(yes/no): ").lower()
    if choice=='no':
        game_over=True
        outup()
    elif choice!='yes' and choice!='no':
        print("Invalid choice")
        break