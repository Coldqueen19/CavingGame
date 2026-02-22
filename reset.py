import pickle

completed_starter = False
cave = "goatchurch"
money = 100

with open('savefile.pkl', 'wb') as file:
    pickle.dump([completed_starter, cave, money], file)