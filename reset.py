import pickle
def reset():
    completed_starter = False
    cave = "goatchurch"
    money = 100
    caves = []
    with open('savefile.pkl', 'wb') as file:
        pickle.dump([completed_starter, cave, money, caves], file)