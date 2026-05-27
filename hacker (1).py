#bianca
#panda

import pandas as pd

data = pd.read_csv('hacker.csv')

ID = data['Log_ID'].tolist()
IP = data['IP_Address'].tolist()
protocol = data['Protocol'].tolist()
KB = data['Data_KB'].tolist()
time = data['Time'].tolist()
info = data['Description'].tolist()
empty = []

#main

#AccountCompromised: Repeated failed login attempts signal that a hacker may be trying to break through your network. The hacker successfully logged in shortly after. Find out which account the user used to login.


i = 0
def findhacker():
    for i in range(len(info)):
        if "Failed" in info[i] and "Login" in info[i+1]:
            empty.append(info[i+1])
        i=i+1
    print("hacker found: ", empty)
    empty.clear()

findhacker()


#DataStolen: A large amount of data was stolen by the hacker. Find the moment the hacker stole the data and print the amount along with the name of the file that was stolen.
i = 0
def datastolen():
    for i in range(len(info)):
        if "Transfer" in info[i]:
            print(data.loc[i])
        i=i+1
datastolen()

#Print the amount of users that were forced to reset their passwords after the breach.

i=0
def forcedreset():
    for i in range(len(info)):
        if "Force" in info[i]:
            empty.append(ID[i])
    print(len(empty))
    empty.clear()
    
forcedreset()
