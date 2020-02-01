from random import randint

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

times = time_gen()

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
        print("time",t)
        print("Trains loaded",Trains_loaded)
        print("Tipple",Tipple)
        if Tipple_loading:
            Tipple += 0.25*crews
            if crews == 1:
                Cost += 9000
            elif crews == 2:
                Cost += 21000
        if Stalling:
            Cost += 15000
        if t in times:
            # Train_present = True
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
            else:
                Stalling = True
        if train2:
            if Tipple >= 1: # Since there is nothing to change about Tipple loading, so time is advanced
                Stalling = False
                Tipple -= 1
                Trains_loaded += 1
                train2 = False
                t += 2
            else:
                Stalling = True
        if train3:
            if Tipple >= 1: # Since there is nothing to change about Tipple loading, so time is advanced
                Stalling = False
                Tipple -= 1
                Trains_loaded += 1
                train3 = False
                t += 2
            else:
                Stalling = True
        elif Tipple < 1.5:
            Tipple_loading = True
        elif Tipple == 1.5:
            Tipple_loading = False
        t += 1
    return Cost

print(Cost_Calculation(times))
print(times)
