import pickle
<<<<<<< HEAD
completed_starter = False
cave = "training"
money = 0
caves = []
starttext = "MANDATORY ORIGINAL TRAINING"
with open('savefile.pkl', 'wb') as file:
    pickle.dump([completed_starter, cave, money, caves, starttext], file)
=======
def reset():
    completed_starter = False
    cave = "goatchurch"
    money = 100
    caves = []
    with open('savefile.pkl', 'wb') as file:
        pickle.dump([completed_starter, cave, money, caves], file)
>>>>>>> 77e71127b746a776be08b3cc40f68ec013d66036
