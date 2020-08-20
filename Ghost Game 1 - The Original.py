#GhostGame
import random

#Variables
nullInput = 0
muchInput = 4
restart = 5
score = 0
#Runs the main code
while restart == 5:
    print("Three doors ahead.\n Ghost behind one. Choose one...")
    userInput = int(input("1, 2, 3"))
    #Checks to see if the user actually input the correct information parameters
    while nullInput >= userInput or muchInput<userInput:
       print("Please type in a valid answer...")
       userInput = int(input("1, 2, 3"))
    #Randomizes ghosts position
    ghostDoor = random.randint(1, 3)
    #used for debuging
    print(ghostDoor)
    #if the user input is the same as the random number stops or restarts the program
    if userInput == ghostDoor:
        print("Ghost!!!\n Run Away!!!")
        print("Your score is: "+str(score))
        print("Do you want to play again?\n Press 5 to restart or 8 to quit")
        restart = int(input("5 or 8"))
        #resets score to 0 after displaying the initial score
        score = 0
        #checks to see if information is in correct parameters
        while restart>8 or restart<5:
            print("Please type something valid")
            restart = int(input("5 or 8"))
    #if the user input is not the same as the random number
    else:
        print("No ghost ahead.\n You move on to the next room")
        score = score + 1
        print("Your score is: "+str(score))
