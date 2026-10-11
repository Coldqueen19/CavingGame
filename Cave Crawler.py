import json
import time
import os

target_dir = os.path.expanduser(os.path.join("~", "Library", "Application Support", "CaveCrawler"))
os.makedirs(target_dir, exist_ok=True)
os.chdir(target_dir)

print("\033[2J\033[3J\033[H\033[0m\n\033[?25l")

global cave
global completed_starter
global money
global caves
global starttext
global gain
global cave_functions
global cave_functions_str
global cave_names
global cave_answers
global inventory
global loaded_data
global shop
global prices
global shop_ref
open("savefile.json", "a").close()
shop_stock = ["Rope"]
prices = [20]
shop_ref = ["rope"]
loaded_data = {}
cave_functions = []
with open("savefile.json", 'r+') as file:
    try:
        loaded_data = json.load(file)
    except json.JSONDecodeError:
        file.write("{}")
    completed_starter = loaded_data.get("completed_starter", False)
    cave = loaded_data.get("area", "training")
    money = loaded_data.get("money", 100)
    caves = loaded_data.get("caves", [])
    cave_names = loaded_data.get("cave_names", [])
    cave_functions_str = loaded_data.get("cave_functions", [])
    cave_answers = loaded_data.get("cave_answers", [])
    inventory = loaded_data.get("inventory", [])
    starttext = loaded_data.get("starttext", "MANDATORY ORIGINAL TRAINING")
for string in cave_functions_str:
    if string in globals():
        func = globals()[string]
        cave_functions.append(func)


def save():
    data = { "completed_starter": completed_starter, "area": cave, "money": money, "caves": caves, "cave_names": cave_names, "cave_functions": cave_functions_str, "starttext": starttext, "inventory": inventory, "cave_answers": cave_answers}
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
    print("\033[2J\033[3J\033[H\033[0m")
    print("Goatchurch it is!")
    global answer
    answer = input("Would you like to go in the old or new entrance?")
    while answer.lower() != "old" and answer.lower() != "new":
        print("Answer not recognised")
        answer = input("Please try again: ")
    if answer.lower() == "old":
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
                        while answer.lower() != "feet first" and answer.lower() != "head first":
                            print("Answer not recognised")
                            answer = input("Please try again: ")
                        if answer.lower() == "feet first":
                            print(
                                "You make it down safely, but must now figure out how to continue through the small hole to advance through the cave.")
                            answer = input("Commando crawl or normal crawl? ")
                            while answer.lower() != "commando" and answer.lower() != "commando crawl" and answer.lower() != "normal" and answer.lower() != "normal crawl":
                                print("Answer not recognised")
                                answer = input("Please try again: ")
                            if answer.lower() == "commando" or answer.lower() == "commando crawl":
                                print(
                                    "You have made it through the hole. The next choice will not be until much later.")
                                print(
                                    "You travel through the cave to get to the drainpipe and enter it. However, there is someone in it!")
                                answer = input("Do you go backwards or do you go forwards and force the other person backwards?")
                                while answer.lower() != "forwards" and answer.lower() != "backwards":
                                    print("Answer not recognised")
                                    answer = input("Please try again: ")
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
        dev = input("I'm sorry, but that feature is under development. Press enter to return to main menu.")
        if dev != "hack club is amazing!":
            save()
            bigMenu()
        print("New entrance it is.")
        print("There is a short drop here.")
        if "rope" in inventory:
            answer = input("Rig a rope?")
            if answer.lower() != "yes":
                print("It is too dangerous. You have to return.")
                time.sleep(2)
                save()
                bigMenu()
            else:
                pass
        else:
            print("It is too dangerous. You have to return.")
            time.sleep(2)
            save()
            bigMenu()




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
    print("\033[2J\033[3J\033[H\033[0m")
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
    print("\033[2J\033[3J\033[H\033[0m")
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
    print("\033[2J\033[3J\033[H\033[0m")
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
    print("\033[2J\033[3J\033[H\033[0m")
    print("MAIN MENU\n")
    print("You can do 4 actions currently:")
    print("Go caving")
    print("Get better gear(Shop)")
    print("Save and Quit")
    print("Restart")
    global response
    response = input("What do you want to do?")
    while response.lower() != "getbettergear" and response.lower() != "get better gear" and response.lower() != "shop" and response.lower() != "gocaving" and response.lower() != "go caving" and response.lower() != "save" and response.lower() != "save and quit" and response.lower() != "quit" and response.lower() != "restart":
        response = input("Answer not recognised. Please try again ensuring there are no leading and trailing spaces and that everyting is pelled correctly: ")
    if response.lower() == "getbettergear" or response.lower() == "get better gear" or response.lower() == "shop":
        shop()
    elif response.lower() == "gocaving" or response.lower() == "go caving":
        caving()
        if cave == "goatchurch":
            menu1()
        elif cave == "swildons":
            menu2()
    elif response.lower() == "save" or response.lower() == "save and quit" or response.lower() == "quit":
        save()
    elif response.lower() == "restart":
        response = input("Are you sure? You will definitely lose all of your progress! This action physically overrides the save file and if a copy is not made you will be unable to recoer your previous game/s [y/N] ~")
        if response.lower() == "y":
            reset()
        else:
            save()


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
    print("\033[2J\033[3J\033[H\033[0m")
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
    print("Checking Answer")
    time.sleep(1)
    print("\r\033[AChecking Answer.")
    time.sleep(1)
    print("\r\033[AChecking Answer..")
    time.sleep(1)
    print("\r\033[AChecking Answer...")
    time.sleep(1)
    print("\r\033[A\033[2KChecking Answer")
    time.sleep(1)
    print("\r\033[AChecking Answer.")
    time.sleep(1)
    print("\r\033[AChecking Answer..")
    time.sleep(1)
    print("\r\033[AChecking Answer...")
    time.sleep(1)
    print("\r\033[A\033[2KChecking Answer")
    time.sleep(1)
    print("\r\033[AChecking Answer.")
    time.sleep(1)
    print("\r\033[AChecking Answer..")
    time.sleep(1)
    print("\r\033[AChecking Answer...")
    time.sleep(1)
    if answer.lower() == "legs first" or answer.lower() == "legsfirst" or answer.lower() == " legsfirst" or answer.lower() == " legs first":
        print("\rYou would have safely go down the slope.")
    elif answer.lower() == "head first" or answer.lower() == "headfirst" or answer.lower() == " headfirst" or answer.lower() == " head first":
        print("\rWhat a disaster! You would have cracked your skull open! Please do not do this in future!")
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
    cave_functions.append(goatchurch)
    cave_functions.append(goatchurch)
    save()
    answer = input("Continue to first cave? Typing 'yes' will continue, typing anything else will save and quit however you will be able to compleye the first cave as soon as you open game again.")
    if answer.lower() == "yes":
        bigMenu()
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
    print("\033[2J\033[3J\033[H\033[0m")
    global cave
    global completed_starter
    global money
    global caves
    global cave_names
    global cave_functions_str
    global starttext
    global inventory
    completed_starter = False
    cave = "training"
    money = 0
    caves = []
    starttext = "MANDATORY ORIGINAL TRAINING"
    inventory = []
    cave_names = []
    cave_functions_str = []
    print("Game Reset")
    time.sleep(3)
    save()

def shop():
    global inventory
    print("\033[2J\033[3J\033[H\033[0m")
    print("SHOP")
    for item in shop_stock:
        print(item)
        print(f"{prices[shop_stock.index(item)]}$")
    answer = input("Would you like to buy something?(y/N)")
    while answer.lower() == "y":
        answer = input("What would you like to buy?")
        while answer.lower() not in shop_ref:
            answer = input("Answer not recognised. please try again: ")
        index = shop_ref.index(answer.lower())
        item = shop_ref[index]
        inventory.append(item)
        increaseMoney(-(prices[index]))
        answer = input("Would you like to buy something else?(y/N)")
    bigMenu()


def caving():
    print("Here are the list of caves you can enter:")
    for item in cave_names:
        print(item)
    answer = input("Where would you like to go?")
    while answer.lower() not in caves:
        answer = input("You may have misspelt the name or hae not unlocked that cave yet. Please try again: ")
    if answer.lower() in caves:
        index = caves.index(answer.lower())
        cave_functions[index]()


t = 0
while t < (len(cave_names)+2):
    print("\r\033[A\033[2KLoading Caves")
    time.sleep(0.5)
    print("\r\033[ALoading Caves.")
    time.sleep(0.5)
    print("\r\033[ALoading Caves..")
    time.sleep(0.5)
    print("\r\033[ALoading Caves...")
    time.sleep(0.5)
    t = t + 1
print("\r\033[A\033[2KDone")
time.sleep(1)
t = 0
while t<3:
    print("\r\033[A\033[2KLoading Menus")
    time.sleep(0.5)
    print("\r\033[ALoading Menus.")
    time.sleep(0.5)
    print("\r\033[ALoading Menus..")
    time.sleep(0.5)
    print("\r\033[ALoading Menus...")
    time.sleep(0.5)
    t = t + 1
print("\r\033[A\033[2KDone")
time.sleep(1)
t = 0
while t<5:
    print("\r\033[A\033[2KLoading Main Menu")
    time.sleep(0.5)
    print("\r\033[ALoading Main Menu.")
    time.sleep(0.5)
    print("\r\033[ALoading Main Menu..")
    time.sleep(0.5)
    print("\r\033[ALoading Main Menu...")
    time.sleep(0.5)
    t = t + 1
print("\r\033[A\033[2KDone")
time.sleep(1)
print("\033[2J\033[3J\033[H\033[0m")
print('''    &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&    
  &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&  
 &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&$XxXX$&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&$:        ;&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&+ .x&&&&&&+ .X&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&+ :$&&&&&&&&+ ;&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&: +&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&$:.X&&&&&&&&$+;x+X;;&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&: +&&&&&&&&&X$&$&$$&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&+ :$&&&&&&&&X;+&&&&&&$$&&&&&&&&&&&&&&&&&&&&
&&&&&&; :$&&&&&&x. x&&x.  ..   +$&&&&&&&&&&&&&&&
&&&&&&&x. .:;;:. :$&$. :$&&&&&x. +&&&&&&&&&&&&&&
&&&&&&&&&&X+;;+X&&&$: +&&&&&&&&X::X&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&+ .$&&&&&&&&&&&&&&$&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&+ :&&&&&&&;$X+x++;X;X++&&&&&&
&&&&&&&&&&&&&&&&&&&+ :&&&&&&&X&XX$$$$$$X$$&&&&&&
&&&&&&&&&&&&&&&&&&&X..X&&&&&&&&&XX$&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&+ .X&&&&&&&; :&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&$. .:++;.  +&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&$+;::;;X&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
 &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
  &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&  
    &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&    ''')
time.sleep(3)
print("\n Welcome To Cave Crawler")
time.sleep(5)
print("\033[2J\033[3J\033[H\033[0m")
print("\033[31m\033[5mPlease remember that this game does not autosave, except at the end of each cave. If you quit before then, your progress WILL NOT be saved.")
print("The only other time it saves is when you are forced to quit the game with your actions.")
time.sleep(5)
print("\033[2J\033[3J\033[H\033[0m")
print("\033[31m\033[25mPlease remember that this game does not autosave, except at the end of each cave. If you quit before then, your progress WILL NOT be saved.")
print("The only other time it saves is when you are forced to quit the game with your actions.")
time.sleep(5)
print("\033[2J\033[3J\033[H\033[0m")
if starttext != "":
    print(starttext)
    time.sleep(1)
if cave == "training":
    training()
else:
    bigMenu()

time.sleep(2)
print("\033[?25h\033[2J\033[H\033[0m")