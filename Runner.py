import pickle

global cave
global completed_starter
global money
global caves
with open('savefile.pkl', 'rb') as file:
    loaded_data = pickle.load(file)
completed_starter, cave, money, caves = loaded_data
global gain


def goatchurch():
    print("Goatchurch it is!")
    global answer
    if input("Would you like to go in the old or new entrance?").lower() == "old":
        print("Follow me!")
        print("""
        ________________________________________________________
        |               /                   |                  |
        |              /                    |                  |
        |             /                     |                  |
        |            /                      |                  |
        |           /                       |                  |
        |          /                        |                  |
        |          |                        |                  |
        |          |                        |                  |
        |          |                        |                  |
        |__________|________________________|__________________|
        
        """)
        print("That was the entrance.")
        print("You are now in the showcave.")
        print("In every area of the cave you visit there will be a short minigame.")
        print()
        print("Turn headtorch on. Here are commands. Order them.")
        print()
        print("1. Adjust tilt")
        print("2. Turn knob until light turns on")
        print("3. Place torch on helmet")
        print("4. Test headtorch batteries")
        print("Give the number.")
        answer = input("First is?")
        if answer.lower() == "3" or answer.lower() == "4":
            answer = input("Next is?")
            if answer.lower() == "3" or answer.lower() == "4":
                answer = input("Next is?")
                if answer.lower() == "2":
                    answer = input("Next is?")
                    if answer.lower() == "1":
                        print("You can now continue on.")
                        print("You turn down towards a slope and you must work out how to slide down.")
                        answer = input("Go down feet first or head first?")
                        if answer.lower() == "feet first":
                            print("You make it down safely, but must now figure out how to continue through the small hole to advance through the cave.")
                            answer = input("Commando crawl or normal crawl? ")
                            if answer.lower() == "commando" or answer.lower() == "commando crawl":
                                print("You have made it through the hole. The next choice will not be until much later.")
                                print("You travel through the cave to get to the drainpipe and enter it. However, there is someone in it!")
                                answer = input("Do you go backwards or force the other person backwards?")
                                if answer.lower() == "backwards":
                                    print("It is always good to be courteous. As a thank you for your trouble, the other caver gives you some money.")
                                    gain = 50
                                    increaseMoney(gain)
                                else:
                                    print("The man is very angry at having to force his group to back up and demands compensation.")
                                    gain = -10
                                    increaseMoney(gain)
                                    print("You decide to return up the coffin lid.")
                                    answer = input("Try and climb up it or try to shuffle?")
                                    if answer.lower() == "climb":
                                        print("There is no rope, so you must shuffle!")
                                        print("You take a while to shuffle up, and decide that next time you will place a rope there to make it easier")
                                        print("You make your way out of the cave.")
                                        answer = input("continue to next cave?")
                                        if answer.lower() == "yes":
                                            if "goatchurch" in caves:
                                                gain = 100
                                            else:
                                                print("You are paid for each cave that is a success!")
                                                gain = 200
                                                caves.append("goatchurch")
                                            increaseMoney(gain)
                                            completed_starter = False
                                            cave = "swildons"
                                            with open('savefile.pkl', 'wb') as file:
                                                pickle.dump([completed_starter, cave, money, caves], file)
                                            swildons()
                                        else:
                                            if "goatchurch" in caves:
                                                gain = 100
                                            else:
                                                print("You are paid for each cave that is a success!")
                                                gain = 200
                                                caves.append("goatchurch")
                                            increaseMoney(gain)
                                            completed_starter = False
                                            cave = "swildons"
                                            with open('savefile.pkl', 'wb') as file:
                                                pickle.dump([completed_starter, cave, money, caves], file)
                                    else:
                                        print("You take a few minutes to shuffle up, but it is far quicker than climbing!")
                                        print("You make your way out of the cave.")
                                        answer = input("continue to next cave?")
                                        if answer.lower() == "yes":
                                            if "goatchurch" in caves:
                                                gain = 100
                                            else:
                                                print("You are paid for each cave that is a success!")
                                                gain = 200
                                                caves.append("goatchurch")
                                            increaseMoney(gain)
                                            completed_starter = False
                                            cave = "swildons"
                                            with open('savefile.pkl', 'wb') as file:
                                                pickle.dump([completed_starter, cave, money, caves], file)
                                            swildons()
                                        else:
                                            if "goatchurch" in caves:
                                                gain = 100
                                            else:
                                                print("You are paid for each cave that is a success!")
                                                gain = 200
                                                caves.append("goatchurch")
                                            increaseMoney(gain)
                                            completed_starter = False
                                            cave = "swildons"
                                            with open('savefile.pkl', 'wb') as file:
                                                pickle.dump([completed_starter, cave, money, caves], file)


                            else:
                                print("You get stuck but are eventually rescued.")
                                bigMenu()
                        else:
                            print("This rash decision marks the end of your caving career. You are eventually rescued but must go through re-training before going near another cave.")
                            print()
                            training()
                    else:
                        print("You are forced to return to the entrance.")
                        bigMenu()
                else:
                    print("You are forced to return to the entrance.")
                    bigMenu()
            else:
                print("You are forced to return to the entrance.")
                bigMenu()
        else:
            print("You are forced to return to the entrance.")
            bigMenu()

    else:
        print("I'm sorry, but that feature is under development.")
        with open('savefile.pkl', 'wb') as file:
            pickle.dump([completed_starter, cave, money, caves], file)

def swildons():
    print("coming soon")

def menu1():

    print()
    print("Here are the list of caves you can enter:")
    print("Goatchurch Cavern")
    ans = input("Where would you like to go?")
    if ans.lower() == "goatchurch" or ans.lower() == "goatchurch cavern":
        goatchurch()
    else:
        print()
        print("I'm sorry, but that feature is under development.")

def menu2():

    print()
    print("Here are the list of caves you can enter:")
    print("Goatchurch Cavern")
    print("Swildons Hole")
    ans = input("Where would you like to go?")
    if ans.lower() == "goatchurch" or ans.lower() == "goatchurch cavern":
        goatchurch()
    if ans.lower() == "swildons" or ans.lower() == "swildons hole":
        swildons()
    else:
        print()
        print("I'm sorry, but that feature is under development.")


def bigMenu():

    print()
    print()
    print("You can do 2 actions currently:")
    print("Go caving")
    print("!UNDER DEVELOPMENT! Get better gear(Shop)")
    global response
    response = input("What do you want to do?")
    if response.lower() == "getbettergear" or response.lower() == "get better gear" or response.lower() == "shop":
        print("I'm sorry, but that feature is under development.")
    elif response.lower() == "gocaving" or response.lower() == "go caving":
        menu()
    else:
        print("That feature does not exist. Please request it if you wish.")
        with open('savefile.pkl', 'wb') as file:
            pickle.dump([completed_starter, cave, money, caves], file)
def training():
    print("This feature requires another programme. Please return later.")
    with open('savefile.pkl', 'wb') as file:
        pickle.dump([completed_starter, cave, money, caves], file)

def increaseMoney(gain):
    global money
    global money2
    money2 = money
    money += gain
    print("Your balance has changed by "+ str(money - money2) + "$")
    print("Your new balance is "+ str(money) + "$")


print("Please remember that this game does not autosave, except at the end of each cave. If you quit before then, your progress WILL NOT be saved.")
print("The only other time it saves is when you are forced to quit the game with your actions.")
if cave == "goatchurch":
    menu1()
elif cave == "swildons":
    menu2()