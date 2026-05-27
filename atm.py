#atm
#bianca
#shows deposit, withdrawal, and balance

#main
balance = 0

def deposit(amount):
    global balance
    balance = balance + amount
    print("deposit:",amount)

def withdrawl(amount):
    global balance
    balance = balance - amount
    print("withdrawl:",amount)


def total():
    global balance
    print("total: ",balance)

def atm(amount1, amount2):
    deposit(amount1)
    withdrawl(amount2)
    total()

atm(5000,47)




