#bianca
#slot machine challenge

#initialize
import random

symbols = [7,"♥","♥","♥","♠","♠","♠","♠","♠","♠","♠","♣","♣","♣","♣","♣","♣","♣","♣","♣",]
balance = 0
cashout = "no"
result = "loss"
totalwon = 0
spent = 0
playername = "player"

leaderboard = []
list = []

#functions
def startscreen():
    print(leaderboard)

def menu():
    global cashout
    global playername
    startscreen()
    playername = input("enter your name: ")
    checking()
    while cashout == "no":
        deposit()
        if balance >= 10:
            spin()
            payout()
            info()
            end()
        else:
            print("not enough credits!")

def checking():
    global playername
    x = "no"
    with open("savedata.txt", "r") as file:
        for line in file:
            if playername in line:
                    x = "yes"
    if x == "yes":
        load_save()

def load_save():
    global balance
    with open("savedata.txt", "r") as save_info:
        list.append(save_info.readline().strip())
        balance = int(save_info.readline().strip())
        list.append(balance)
        list.append(save_info.readline().strip())
        print(list)


def simulate():
    global spent
    global totalwon
    i=0
    for i in range (1001):
        spin()
        payout()
        i = i +1
    print("net profit: ", spent - totalwon)

def end():
    global cashout
    global playername
    global balance
    cashout = input("do you want to cashout?")
    if cashout == "yes":
         with open("savedata.txt","w") as save_info:
            save_info.write(str(playername) + "\n")
            save_info.write(str(balance)+ "\n")
            save_info.write(str(totalwon)+ "\n")
         with open("savedata.txt", "r") as save_info:
            list.append(save_info.readline().strip())
            list.append(int(save_info.readline().strip()))
            list.append(int(save_info.readline().strip()))
    leaderboard.append(list)
    print(leaderboard)
    leaderboard.sort()


def info():
    global balance
    global totalwon
    print("you have", balance, " credits")
    print("you have", totalwon , "dollars won")

def spin():
    global result
    global balance
    global spent
    slot1 = random.choice(symbols)
    slot2 = random.choice(symbols)
    slot3 = random.choice(symbols)
    print(slot1,slot2,slot3)
    if slot1 == slot2:
        if slot1 != 7:
            if slot2 == slot3:
                print("WIN!!")
                result = "win"
        elif slot2 == slot3:
            result = "jackpot"
            print("JACKPOT!!!")
    else:
        print("sorry")
        result = "loss"
    spent = spent + 10
    balance = balance - 10

def payout():
    global result
    global balance
    global totalwon
    if result == "jackpot":
        totalwon = totalwon + 200
    if result == "win":
        totalwon = totalwon + 50

def deposit():
    global balance
    global spent
    add = input("deposit 0, 20, 50, or 100 credits? ")
    if add == "20":
        balance = balance + 20
        spent = spent + 20
    if add == "50":
        balance = balance + 50
        spent = spent + 50
    if add == "100":
        balance = balance + 100
        spent = spent + 100


#main
menu()
