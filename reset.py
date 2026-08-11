<<<<<<< HEAD
import pickle
=======
import json
>>>>>>> 947ce42e9a37b5633e9b2cd30215f3be8d98bb8c
completed_starter = False
cave = "training"
money = 0
caves = []
starttext = "MANDATORY ORIGINAL TRAINING"
<<<<<<< HEAD
with open('savefile.pkl', 'wb') as file:
    pickle.dump([completed_starter, cave, money, caves, starttext], file)
=======
data = { "completed_starter": completed_starter, "area": cave, "money": money, "caves": caves, "starttext": starttext}
with open('savefile.json', 'w') as file:
    json.dump(data, file)
>>>>>>> 947ce42e9a37b5633e9b2cd30215f3be8d98bb8c
