#bianca
#panda

#initialize

import pandas as pd

data = pd.read_csv('influencer.csv')

month = data['Month'].tolist()
views = data['Views'].tolist()
dislikes = data['Dislikes'].tolist()
subscribers = data['Subscriber(+-)'].tolist()
revenue = data['Revenue'].tolist()
humblebeginnings = []
goodmonths = []
scandals = []

# Humble Beginnings: print all of the months/data where the influencer had 2000 or fewer views
def viewnumber(max):
    i = 0
    for i in range(len(month)):
        if views[i] <= max:
            humblebeginnings.append(month[i])
        i=i+1
    print("starting months", humblebeginnings)

viewnumber(2000)

# The Golden Age: Print all months where the subscriber growth was over 50000 a month
def growth(min):
    i = 0
    for i in range(len(month)):
        if subscribers[i] >= min:
            goodmonths.append(month[i])
        i=i+1
    print("large growth in", goodmonths)

growth(50000)

# Scandal: Print the two months where the influencer had a scandal that caused them to have no revenue leading to their downfall
def scandal():
    i = 0
    for i in range(len(month)):
        if revenue[i] == 0:
            scandals.append(month[i])
        i=i+1
    print("scandals were in", scandals)

scandal()
