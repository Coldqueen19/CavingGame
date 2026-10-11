import json
import time
import os

#data = open("congrats.pdf", "rb").read()

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
global injuries
global answer
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
    injuries = loaded_data.get("injuries", 0)



def save():
    data = { "completed_starter": completed_starter, "area": cave, "money": money, "caves": caves, "cave_names": cave_names, "cave_functions": cave_functions_str, "starttext": starttext, "inventory": inventory, "cave_answers": cave_answers, "injuries": injuries}
    with open('savefile.json', 'w') as file:
        json.dump(data, file)


def boss():
    print("So, you've finally the nerve to find me eh? Well I can tell you this won't be easy for you! \nI'll give you one chance to surrender and i'll give you 404 and 2 injuries")
    answer = input("Surrender? [Y/n] % ")
    if answer.lower() == "y":
        print("You have some nerve, challenging the developer. Ok, I gave you your chance so here's how it works: \nThere are 3 stages to this  boss fight: \n1. 10 questions \n2. Typing out a passage of text without any mistakes. \n3. A final multiple choice question with 10 possible answers. \nFail any of them and you lose all your money and gain 10 injuries. \nBeat all of them and get 300$. Have fun!")
        answer = input("What is the first cave in this game?")
        if answer.lower() == "goatchurch cavern":
            answer = input("What was the incorrect answer for the question in training?")
            if answer.lower() == "head first":
                answer = input("What os was this game originally designed for?")
                if answer.lower() == "mac" or answer.lower() == "macintosh" or answer.lower() == "macos" or answer.lower() == "macintosh os":
                    answer = input("How many caves have you unlocked?")
                    if int(answer) == len(cave_names):
                        answer = input("What is the second cave in this game?")
                        if answer.lower() == "swildon's hole":
                            answer = input("What is the of this game?")
                            if answer.lower() == "cave crawler":
                                answer = input("Do you have rope in your inventory?")
                                if (answer.lower() == "yes" and "rope" in inventory) or (answer.lower() == "no" and "rope" not in inventory):
                                    answer = input("What is the fourth option in the main menu?")
                                    if answer.lower() == "retire":
                                        answer = input("What is the first option in the main menu?")
                                        if answer.lower() == "go caving":
                                            answer = input("Where, in real life is the first cave?")
                                            if answer.lower() == "the mendips" or answer.lower() == "mendips":
                                                print("Wow! You mananged to beat the first round! but here's the second.")
                                                para = "fgdhjgfbsajhfgbdsjgfewshfgsdhjfgshjnfshjfvdshfgdhjkgfhsjagfhajdsfghdjkfghdsjfgdsjhkgfahjkgfdjhkgfdshjakfgdhjkgashjkgahjskgdaskjhadshjkfdghjsdfahjkfdgfhdjkgfhjkdfgjfkdhagfhjdkfghjdskfgdjhsafgjdhfgjkhfsafhgjdkasfghdjaksfdhsgjakfsajghkdasjkhfsdagjksagjksajkajkgshfgjhafkfeggewyjhbzufhvsauyfvstghadtshgdftysahdfytahfdaythfaytjhfasghdfvsahgdfasghjdvasydgxcagshdcsghcxasghftywsctysahvxsatyadfasgfxsatydvstyaxfvaytvxytsavxysahvxysghaxvsghxvsghacxvhsgadxvghsaxvhgsx"
                                                print(f"Copy this text with nomore than 3 errors: {para} %")
                                                start = time.time()
                                                answer = input("% ")
                                                elapsed = time.time() - start
                                                if len(answer) > 50 and elapsed < 20:
                                                    print("NO copy and paste. That's a fail.")
                                                    injuries += 10
                                                    increaseMoney(-money)
                                                else:
                                                    mistakes = 0
                                                    for trgt, usr in zip(para, answer):
                                                        if trgt != usr:
                                                            mistakes += 1
                                                    if mistakes >= 3:
                                                        print("3+ Mistakes. Dissapointing.")
                                                        injuries += 10
                                                        increaseMoney(-money)
                                                    else:
                                                        print("Ok, I see something in you but can you answer this question?")
                                                        answer = input("What is Schildkröte in English?")
                                                        if answer.lower() == "tortoise":
                                                            download_dir = os.path.expanduser(os.path.join("~","Downloads"))
                                                            os.chdir(download_dir)
                                                            #open("CONGRATULATIONS.pdf", "wb").write(data)
                                                            os.chdir(target_dir)

                                            else:
                                                print("I warned you!")
                                                injuries += 10
                                                increaseMoney(-money)
                                        else:
                                            print("I warned you!")
                                            injuries += 10
                                            increaseMoney(-money)
                                    else:
                                        print("I warned you!")
                                        injuries += 10
                                        increaseMoney(-money)
                                else:
                                    print("I warned you!")
                                    injuries += 10
                                    increaseMoney(-money)
                            else:
                                print("I warned you!")
                                injuries += 10
                                increaseMoney(-money)
                        else:
                            print("I warned you!")
                            injuries += 10
                            increaseMoney(-money)
                    else:
                        print("I warned you!")
                        injuries += 10
                        increaseMoney(-money)
                else:
                    print("I warned you!")
                    injuries += 10
                    increaseMoney(-money)
            else:
                print("I warned you!")
                injuries += 10
                increaseMoney(-money)
        else:
            print("I warned you!")
            injuries += 10
            increaseMoney(-money)
    else:
        injuries += 2
        increaseMoney(50)


def doctor():
    global injuries
    print(f"You have {injuries} injuries.")
    if money >= 20:
        increaseMoney(-20)
        injuries -= 1
    elif money <= 20 and injuries < 5:
        print("You do not have enough money to afford treatment.")
    else:
        print("You condition is so critical that you must retire.")
        retire()
    print(f"You now have {injuries} injuries.")


def retire():
    print("Well done noble adventurer. I hope you enjoyed your adventure. THe game will now reset.")
    time.sleep(2)
    reset()


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
    global injuries
    if injuries >= 5:
        answer = input("You have more than 5 injuries. Visit the doctor for 20$ or retire? Retiring resets the game.")
        while answer.lower() != "doctor" and answer.lower() != " visit doctor" and answer.lower() != "the doctor" and answer.lower() != "visit the doctor" and answer.lower() != "retire":
            answer = input("Answer not recognised. Please ensure everything is correctly spelt and that there are no leading or trailing spaces: ")
        if answer.lower() == "doctor" or answer.lower() == " visit doctor" or answer.lower() == "the doctor" or answer.lower() == "visit the doctor":
            doctor()
        else:
            retire()
    while injuries >= 5:
        answer = input("You still have more than 5 injuries. Visit the doctor again for 20$ or retire? Retiring resets the game.")
        while answer.lower() != "doctor" and answer.lower() != " visit doctor" and answer.lower() != "the doctor" and answer.lower() != "visit the doctor" and answer.lower() != "retire":
            answer = input("Answer not recognised. Please ensure everything is correctly spelt and that there are no leading or trailing spaces: ")
        if answer.lower() == "doctor" or answer.lower() == " visit doctor" or answer.lower() == "the doctor" or answer.lower() == "visit the doctor":
            doctor()
        else:
            retire()
    print("\033[2J\033[3J\033[H\033[0m")
    print("Goatchurch it is!")
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
                print("It hurts like hell. You have to be rushed out! You gained 2 injuries.")
                injuries += 2
                answer = input("Spend 20$ to visit the doctor and heal one injury [Y/n]?")
                if answer.lower() == "n":
                    print(f"You have {injuries} injuries. If you gain more than 5 injuries you will either have to visit the doctor or retire.")
                else:
                    doctor()
                time.sleep(2)
                save()
                bigMenu()
            else:
                print("You encounter a slide like structure.")
                answer = input("Slide down on your front or on your back? ")
                while answer.lower() != "front" and answer.lower() != "back":
                    answer = input("I can't seem to recognise that answer. Please check for typos and leading or trailing spaces.")
                if answer.lower() == "front":
                    print("It is a little painful but you should be ok?")
                    injuries += 1
                    answer = input("Spend 20$ to visit the doctor [Y/n]?")
                    if answer.lower() == "n":
                        print(f"You have {injuries} injuries. If you gain more than 5 injuries you will either have to visit the doctor or retire.")
                    else:
                        doctor()
                else:
                    print("You make it down with no injury.")
                bigMenu()
                
        else:
            print("It is too dangerous without a rope. You have to return.")
            time.sleep(4)
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
    print("Retire")
    global response
    response = input("What do you want to do?")
    while response.lower() != "getbettergear" and response.lower() != "get better gear" and response.lower() != "shop" and response.lower() != "gocaving" and response.lower() != "go caving" and response.lower() != "save" and response.lower() != "save and quit" and response.lower() != "quit" and response.lower() != "retire":
        response = input("Answer not recognised. Please try again ensuring there are no leading and trailing spaces and that everyting is pelled correctly: ")
    if response.lower() == "getbettergear" or response.lower() == "get better gear" or response.lower() == "shop":
        shop()
    elif response.lower() == "gocaving" or response.lower() == "go caving":
        caving()
    elif response.lower() == "save" or response.lower() == "save and quit" or response.lower() == "quit":
        save()
    elif response.lower() == "retire":
        retire()


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
    global injuries
    completed_starter = False
    cave = "training"
    money = 0
    caves = []
    starttext = "MANDATORY ORIGINAL TRAINING"
    inventory = []
    cave_names = []
    cave_functions_str = []
    injuries = 0
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


for string in cave_functions_str:
    if string in globals():
        func = globals()[string]
        cave_functions.append(func)

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