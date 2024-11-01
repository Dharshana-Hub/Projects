import random
Choices = ["Rock", "Paper", "Scissors", "Quit"]
while True:
    User_Choice = str(input('Enter your move ("Rock", "Paper", "Scissors", "Quit"): '))
    Computer_Choice = random.choice(Choices[:3])
    if User_Choice == Choices[3]:
        print("Thank You!!")
        break
    elif User_Choice == "Rock":
        if Computer_Choice == "Rock":
            print("Both the players have selected the same choice ... It's a tie!!")
        elif Computer_Choice == "Paper":
            print("Paper covers Rock ... You Lose!")
        elif Computer_Choice == "Scissors":
            print("Rock smashes Scissors ... You Win!!!")

    elif User_Choice == "Scissors":
        if Computer_Choice == "Scissors":
            print("Both the players have selected the same choice ... It's a tie!!")
        elif Computer_Choice == "Paper":
            print("Scissors cuts the paper ... You Win!!!")
        elif Computer_Choice == "Rock":
            print("Rock smashes the Scissors ... You Lose!")
    
    elif User_Choice == "Paper":
        if Computer_Choice == "Paper":
            print("Both the players have selected the same choice ... It's a tie!!")
        elif Computer_Choice == "Scissors":
            print("Scissors cuts the paper ... You Lose!")
        elif Computer_Choice == "Rock":
            print("Paper covers the Rock ... You Win!!!")
    else:
        print("Please select a proper Choice!")
        
