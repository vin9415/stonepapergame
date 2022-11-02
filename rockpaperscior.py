import random
user_input=("enter a choice: (rock, paper , scissor)")
possible_action=["rock","paper","scissor"]
computer_actions=random.choice(possible_action)

if user_input==computer_actions:
    print("its a tie")
elif user_input=="rock":
    if computer_actions=="paper":
        print("computer wins")
    else:
        print("user win")    
elif user_input=="paper":
     if computer_actions=="rock":
        print("computer wins")
     else:
            print("user win")     
        
elif user_input=="scissor":
    if computer_actions=="paper":
        print("computer wins")
    else:
         print("user win")  
break