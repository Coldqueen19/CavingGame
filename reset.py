import pickle
completed_starter = False
cave = "training"
money = 0
caves = []
starttext = "MANDATORY ORIGINAL TRAINING"
with open('savefile.pkl', 'wb') as file:
    pickle.dump([completed_starter, cave, money, caves, starttext], file)