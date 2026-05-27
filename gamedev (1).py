#bianca
#panda

import pandas as pd

data = pd.read_csv('gamedev.csv')

levels = data['Level'].tolist()
time = data['Time'].tolist()
rating = data['Rating'].tolist()
summary = data['Summary'].tolist()
feedback = data['Feedback'].tolist()
problematic = []

def redflags(keyword):
    i = 0
    for item in feedback:
        if keyword.upper() in item:
            problematic.append(levels[i])
            problematic.append(feedback[i])
        i=i+1

def longtime():
    i= 0
    n = 0
    level = levels[i]
    for i in range(len(levels)):
        if rating[i] <= 4:
            i=i+1
        if time[n]>=time[i]:
            level = levels[n]
            i=i+1
        elif time[n] < time[i]:
            n= i
            level = levels[n]
            i = i+1
    print(level)
    print(data.loc[n])

def findsecret():
    i=0
    for item in feedback:
        if "secret" in item:
            print(data.loc[i])
        else:
            i = i+1

#main
redflags("error")
redflags("issue")
redflags("bug")
print(problematic)
longtime()
findsecret()
