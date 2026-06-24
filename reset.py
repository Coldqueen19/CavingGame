import json
completed_starter = False
cave = "training"
money = 0
caves = []
starttext = "MANDATORY ORIGINAL TRAINING"
data = { "completed_starter": completed_starter, "area": cave, "money": money, "caves": caves, "starttext": starttext}
with open('savefile.json', 'w') as file:
    json.dump(data, file)