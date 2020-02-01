from random import randint
from itertools import combinations

def time_gen():
    t1 = randint(5,20)
    t2 = randint(5,20)
    t3 = randint(5,20)
    while abs(t2 - t1) <= 3:
        t2 = randint(4,20)
    while abs(t3 - t2) <= 3 and abs(t3 - t1) <= 3:
        t3 = randint(4,20)
    return [t1,t2,t3]

# time_gen()

def get_times():
    lst = list(range(21))
    for i in range(5):
        lst.remove(i)
    comb = combinations(lst, 3)
    times = list()
    for i in list(comb):
        if (abs(i[2]-i[1]) > 3 and abs(i[1]-i[0]) > 3 and abs(i[0]-i[2]) > 3):
            times.append(i)
    return times

times = get_times()

def Cost_Calculation(times):

    t = 0
    crews = 1
    Cost = 54000

    Trains_loaded = 0
    Train_progress = 0
    Train_present = False
    train1 = False
    train2 = False
    train3 = False
    Stalling = False
    Tipple_loading = False

    Tipple = 1.5

    while Trains_loaded != 3:
        #print("time",t)
        #print("Trains loaded",Trains_loaded)
        #print("Tipple",Tipple)
        if Tipple_loading:
            Tipple += 0.25*crews
            if crews == 1:
                Cost += 9000
            elif crews == 2:
                Cost += 21000
        if Stalling:
            Cost += 15000
        if t in times:
            if (Trains_loaded == 0):
              train1 = True
            if (Trains_loaded == 1):
              train2 = True
              train1 = False
            if (Trains_loaded == 2):
              train3 = True
              train2 = False
        if train1:
            if Tipple >= 1: # Since there is nothing to change about Tipple loading, so time is advanced
                Stalling = False
                Tipple -= 1
                Trains_loaded += 1
                train1 = False
                t += 2
                crews = 1
            else:
                Stalling = True
                crews = 2
        if train2:
            if Tipple >= 1: # Since there is nothing to change about Tipple loading, so time is advanced
                Stalling = False
                Tipple -= 1
                Trains_loaded += 1
                train2 = False
                t += 2
                crews = 1
            else:
                Stalling = True
                crews = 2
        if train3:
            if Tipple >= 1: # Since there is nothing to change about Tipple loading, so time is advanced
                Stalling = False
                Tipple -= 1
                Trains_loaded += 1
                train3 = False
                t += 2
                crews = 1
            else:
                Stalling = True
                crews = 2
        elif Tipple < 1.5:
            Tipple_loading = True
        elif Tipple == 1.5:
            Tipple_loading = False
        t += 1
    return Cost

costs = list()
for i in times:
    print(i)
    costs.append(Cost_Calculation(i))
print(min(costs))

#print(Cost_Calculation(times))
#print(times)
