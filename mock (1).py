#mockup
#bianca
#helps user find desired dog breed

#Dog Dataset
#Website Name: Code.org
#URL: https://code.org/en-US
#Dataset Source:https://thedogapi.com/en

# initialize
import pandas as pd
data = pd.read_csv('dogs.csv')

import webbrowser

number = data['id'].tolist()
name = data['Name'].tolist()
breed = data['Breed Group'].tolist()
bredfor = data['BredFor'].tolist()
minlife = data['Minimum Life Span'].tolist()
maxlife = data['Maximum Life Span'].tolist()
minheight = data['Minimum Height'].tolist()
maxheight = data['Maximum Height'].tolist()
minweight = data['Minimum Weight'].tolist()
maxweight = data['Maximum Weight'].tolist()
temperament = data['Temperament'].tolist()
image = data['Image'].tolist()

perfdog = []

# functions
def GetDogSize(size):
    if size == "tiny":
        i = 0
        for item in maxweight:
            if item<=10:
                perfdog.append(name[i])
            i = i+1
    elif size == "small":
        i = 0
        for item in minweight:
            if item >= 11 and maxweight[i] <= 25:
                perfdog.append(name[i])
            i = i+1
    elif size == "medium":
        i = 0
        for item in minweight:
            if item >= 26 and maxweight[i] <= 60:
                perfdog.append(name[i])
            i = i+1
    elif size == "large":
        i = 0
        for item in maxwieght:
            if item >= 61:
                perfdog.append(name[i])
            i = i+1
    print("here are reccommended dog breeds: ", perfdog)
    perfdog.clear()

def LookUp(dog_breed):
    i = 0
    for item in name:
        if dog_breed in item:
            perfdog.append(name[i])
            perfdog.append(temperament[i])
            webbrowser.open(image[i])
        i = i+1
    try:
        if perfdog[0]:
            print(perfdog)
            perfdog.clear
    except IndexError:
        print("not found")

def DogFor(purpose):
    i = 0
    for item in bredfor:
        if purpose in item.lower():
            perfdog.append(name[i])
        i = i+1
    try:
        if perfdog[0]:
            print("reccomended: ",perfdog)
    except IndexError:
        print("no matches")
    perfdog.clear()

def MainMenu():
    print("hi! welcome!")
    print("what would you like to do?")
    choice = "search"
    while choice != "quit":
        choice = input("search for a dog or find a match? ")
        if choice == "search for a dog":
            dog_breed = input("what dog are you looking for? ")
            LookUp(dog_breed)
        if choice == "find a match":
            choice2 = input("search based on weight or purpose?")
            if choice2 == "weight":
                size = input("what is your desired weight?")
                GetDogSize(size)
            if choice2 == "purpose":
                purpose = input("what do you want a dog for?")
                DogFor(purpose)



# main
MainMenu()
