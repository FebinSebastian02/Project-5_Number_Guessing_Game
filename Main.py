#imports are done
import random
def main():
    print("\n!!!Welcome to the GuessMaster!!!")
    while True:
        choice = int(input("\nDo you wish to play the game 1) Yes 2)No..."))
        if choice == 2:
            print("Quitting the game...")
            quit()
        elif choice == 1:
            numList = []
            for i in range(1, 51):
                numList.append(i)   #Used to append numbers 1-50 to the list
            comTurn = random.choice(numList)
            print(comTurn)  #Here, the print is used only for demo purpose.Comment this line while playing the game.
            k = 2
            while True:
                userTurn = int(input("\nEnter a number between 1 and 50..."))
                print(userTurn)
                if userTurn < 1 or userTurn > 50:
                    print("Invalid number entered. Please enter a valid number between 1 and 50...")
                else:
                    if userTurn == comTurn:
                        print("\nYour guess is correct")
                        print("!!!Congratulations, you have been won!!!")
                        break
                    elif userTurn != comTurn:
                        if k == 0:
                            print("\n!!!You lost the game!!!")
                            break
                        print("\nYou have {} more chance left".format(k))
                        k -= 1
        else:
            print("\nInvalid choice entered. Enter a valid choice")

main()