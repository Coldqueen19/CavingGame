import pickle
import json
import time

global cave
global completed_starter
global money
global caves
global starttext
global gain
global cave_functions
global cave_functions_str
global cave_names
with open("savefile.json", 'r') as file:
    loaded_data = json.load(file)
completed_starter = loaded_data.get("completed_starter", False)
cave = loaded_data.get("area", "training")
money = loaded_data.get("money", 100)
caves = loaded_data.get("caves", [])
cave_names = loaded_data.get("cave_names", [])
cave_functions_str = loaded_data.get("cave_functions", [])
starttext = loaded_data.get("starttext", "MANDATORY ORIGINAL TRAINING")
for string in cave_functions_str:
    if string in globals():
        func = globals()[string]
        cave_functions.append(func)
def save():
    data = { "completed_starter": completed_starter, "area": cave, "money": money, "caves": caves, "cave_names": cave_names, "cave_functions": cave_functions_str, "starttext": starttext}
    with open('savefile.json', 'w') as file:
        json.dump(data, file)

def goatchurch():
    global cave
    global completed_starter
    global money
    global caves
    global starttext
    global gain
    global cave_functions
    global cave_functions_str
    global cave_names
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
        print("Turn headtorch on. Here are some commands. Order them.")
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
                            print(
                                "You make it down safely, but must now figure out how to continue through the small hole to advance through the cave.")
                            answer = input("Commando crawl or normal crawl? ")
                            if answer.lower() == "commando" or answer.lower() == "commando crawl":
                                print(
                                    "You have made it through the hole. The next choice will not be until much later.")
                                print(
                                    "You travel through the cave to get to the drainpipe and enter it. However, there is someone in it!")
                                answer = input("Do you go backwards or force the other person backwards?")
                                if answer.lower() == "backwards":
                                    print("It is always good to be courteous. As a thank you for your trouble, the other caver gives you some money.")
                                    gain = 50
                                    increaseMoney(gain)
                                    print("You decide to return up the coffin lid.")
                                    answer = input("Try and climb up it or try to shuffle?")
                                    if answer.lower() == "climb":
                                        print("There is no rope, so you must shuffle!")
                                        print(
                                            "You take a while to shuffle up, and decide that next time you will place a rope there to make it easier")
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
                                            save()
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
                                            save()
                                            bigMenu()
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
                                            save()
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
                                            save()
                                else:
                                    print(
                                        "The man is very angry at having to force his group to back up and demands compensation.")
                                    gain = -10
                                    increaseMoney(gain)
                                    print("You decide to return up the coffin lid.")
                                    answer = input("Try and climb up it or try to shuffle?")
                                    if answer.lower() == "climb":
                                        print("There is no rope, so you must shuffle!")
                                        print(
                                            "You take a while to shuffle up, and decide that next time you will place a rope there to make it easier")
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
                                            save()
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
                                            save()
                                            bigMenu()
                                    else:
                                        print(
                                            "You take a few minutes to shuffle up, but it is far quicker than climbing!")
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
                                            save()
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
                                            save()
                                            bigMenu()


                            else:
                                print("You get stuck but are eventually rescued.")
                                bigMenu()
                        else:
                            print(
                                "This rash decision marks the end of your caving career. You are eventually rescued but must go through re-training before going near another cave.")
                            print()
                            answer = input("Go for retraining now?")
                            starttext = "MANDATORY RETRAINING: BAD DESCISION MAKAING"
                            cave = "training"
                            if answer.lower() == "yes":
                                print()
                                print()
                                print("MANDATORY RETRAINING: BAD DESCISION MAKAING")
                                print()
                                print()
                                training()
                            else:
                                save()

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
        save()


def swildons():
    global cave
    global completed_starter
    global money
    global caves
    global starttext
    global gain
    global cave_functions
    global cave_functions_str
    global cave_names
    print("Welcome to Swildons hole!")
    print("This cave is considerably harder to complete than Goatchurch Cavern due to the ever changing nature of a wet cave.")
    print("Additionally there is only one entrance and there is an entry fee of 1$")
    answer = input("Continue?")
    if answer.lower() == "yes":
        increaseMoney(-1)
    else:
        print("Your game will save here")
    save()


def menu1():
    print()
    print("Here are the list of caves you can enter:")
    print("Goatchurch Cavern")
    ans = input("Where would you like to go?")
    if ans.lower() == "goatchurch" or ans.lower() == "goatchurch cavern":
        goatchurch()
    else:
        print()
        print("I'm sorry, but that cave is either locked or under development.")
        save()


def menu2():
    global cave
    global completed_starter
    global money
    global caves
    global starttext
    global gain
    global cave_functions
    global cave_functions_str
    global cave_names
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
        print("I'm sorry, but that cave is either locked or under development.")
        save()


def bigMenu():
    global cave
    global completed_starter
    global money
    global caves
    global starttext
    global gain
    global cave_functions
    global cave_functions_str
    global cave_names
    print()
    print()
    print("You can do 4 actions currently:")
    print("Go caving")
    print("!UNDER DEVELOPMENT! Get better gear(Shop)")
    print("Save and Quit")
    print("Restart")
    global response
    response = input("What do you want to do?")
    if response.lower() == "getbettergear" or response.lower() == "get better gear" or response.lower() == "shop":
        print("I'm sorry, but that feature is under development.")
    elif response.lower() == "gocaving" or response.lower() == "go caving":
        if cave == "goatchurch":
            menu1()
        elif cave == "swildons":
            menu2()
    elif response.lower() == "save" or response.lower() == "save and quit":
        with open('savefile.pkl', 'wb') as file:
            pickle.dump([completed_starter, cave, money, caves, starttext], file)
    elif response.lower() == "restart":
        response == input("Are you sure? You will definitely lose all of your progress! This action physically overrides the save file and if a copy is not made you will be unable to recoer your previous game/s")
        if response.lower() == "yes":
            reset()
        else:
            save()
    else:
        print("That feature does not exist. Please request it if you wish.")
        with open('savefile.pkl', 'wb') as file:
            pickle.dump([completed_starter, cave, money, caves, starttext], file)


def training():
    global cave
    global completed_starter
    global money
    global caves
    global starttext
    global gain
    global cave_functions
    global cave_functions_str
    global cave_names
    print("Welcome to training!")
    time.sleep(2)
    print("This will guide you through the best choices to use whilst playing the game to ensure that you have the best playing experience!")
    time.sleep(2)
    print("Many topics will be covered.")
    time.sleep(1)
    print()
    time.sleep(1)
    print("1. Choices")
    time.sleep(1)
    print()
    time.sleep(1)
    print("This game is mostly based on choices.")
    time.sleep(2)
    print("Sometimes your choices won't matter and there is a similar path for both choices...")
    time.sleep(2)
    print("...and sometimes making the wrong choice will cost you.")
    time.sleep(1)
    print("Try it now!")
    time.sleep(1)
    answer = input("Go headfirst or legs first down the slope?")
    time.sleep(5)
    if answer.lower() == "legs first" or answer.lower() == "legsfirst" or answer.lower() == " legsfirst" or answer.lower() == " legs first":
        print("You would have safely go down the slope.")
    elif answer.lower() == "head first" or answer.lower() == "headfirst" or answer.lower() == " headfirst" or answer.lower() == " head first":
        print("What a disaster! You would have cracked your skull open! Please do not do this in future!")
    time.sleep(1)
    print("Now that you have tried decision making it is time to move on to money.")
    time.sleep(1)
    print()
    print("2. Money")
    time.sleep(1)
    print("Money is an important piece of the game. It can be used to purchase items in the shop, which have varios purposes.")
    time.sleep(1)
    print("Take a look at this money log.")
    time.sleep(1)
    money = 0
    increaseMoney(50)
    time.sleep(3)
    print()
    print("Here you can see that you have gained 50$ and that your new balance is 50$.")
    time.sleep(1)
    print("Sadly this money will not be added to your account but a not too shabby sum of 100$ is given at the start for free!")
    money = 100
    time.sleep(1)
    print()
    print("END OF SESSION")
    starttext = ""
    cave = "goatchurch"
    caves.append("goatchurch")
    caves.append("goatchurch cavern")
    cave_names.append("Goatchurch Cavern")
    cave_functions_str.append("goatchurch")
    cave_functions_str.append("goatchurch")
    save()
    answer = input("Continue to first cave? Typing 'yes' will continue, typing anything else will save and quit however you will be able to compleye the first cave as soon as you open game again.")
    if answer.lower() == "yes":
        goatchurch()
    else:
        save()


def increaseMoney(gain):
    global money
    global money2
    money2 = money
    money += gain
    print("Your balance has changed by " + str(money - money2) + "$")
    print("Your new balance is " + str(money) + "$")

def reset():
    global cave
    global completed_starter
    global money
    global caves
    global starttext
    completed_starter = False
    cave = "training"
    money = 0
    caves = []
    starttext = "MANDATORY ORIGINAL TRAINING"
    save()

print("Please remember that this game does not autosave, except at the end of each cave. If you quit before then, your progress WILL NOT be saved.")
print("The only other time it saves is when you are forced to quit the game with your actions.")
time.sleep(1)
if starttext != "":
    print()
    print()
    print(starttext)
    print()
    print()
    time.sleep(1)
if cave == "goatchurch":
    menu1()
elif cave == "swildons":
    menu2()
elif cave == "training":
    training()