#bianca and maya
#CREATE Program
#program for bird watchers that helps them identify what bird they saw


#credits
#bird data set
#website name: Cornell Lab of Ornithology
#dataset source:"https://www.birds.cornell.edu/home/"


#inititalize
import pandas as pd
import webbrowser
data = pd.read_csv('birddata.csv') #uploading the data from our csv file




number = data['id'].tolist()
name = data['Name'].tolist()
scientific = data['Scientific Name'].tolist()
status = data['Conservation Status'].tolist()
color = data['Primary Color'].tolist()
diet = data['Diet'].tolist()
areaphoto = data['Image of Range'].tolist()
birdphoto = data['Image of Bird'].tolist()


birdfound = []
birdfound2 =[]
birdfound3 =[]
finalbird = []
finalbird2 = []


#functions
def BirdColor(primary_color): #searches for a bird based off of its main color
    i = 0
    for item in color:
        if primary_color in color[i].lower():
            birdfound.append(name[i])
        i = i + 1
    print("the bird you saw may have been: ")
    for item in birdfound:
        print(item)


def BirdFood(food): #searches for a bird based off of what it was seen eating
    i = 0
    for item in diet:
        if food in diet[i]:
            birdfound.append(name[i])
        i = i + 1
    print("you may have seen a")
    for item in birdfound:
        print(item)


def BirdFood2(food2): #used after user either says a color or says a first food, refines list down to more specific bird
    i = 0
    for item in diet:
        if food2 in diet[i]:
            birdfound2.append(name[i])
        i = i + 1
    i = 0
    for item in birdfound:
        if item in birdfound2:
            finalbird.append(birdfound[i])
        i = i + 1
    print("you may have seen a")
    for item in finalbird:
        print(item)


def BirdFood3(food3): #used after user already input a color and food, refines set down to third food
    i = 0
    for item in diet:
        if food3 in diet[i]:
            birdfound3.append(name[i])
        i = i + 1
    i = 0
    for item in finalbird:
        if item in birdfound3:
            finalbird2.append(finalbird[i])
        i = i + 1
    print("you may have seen a")
    for item in finalbird2:
        print(item)


def MainMenu(): #main menu of program, here the user may choose to identify the bird they saw with what food they were eating, and what color they were
    print("Hi, welcome!")
    print("We are here to help you identify the bird you saw!")
    choice = input("Would you like to search based on the bird's color or the food it was eating? ")
    if choice.lower() == "food":
        food = input("What did you see it eating? ")
        BirdFood(food)
        more = input("Did you see it eating anything else? (Y/N) ")
        if more.upper() == "Y":
            food2 = input("What other food was it eating? ")
            BirdFood2(food2)
            choice2 = input("Would you now like to search by its primary color? (Y/N) ")
            if choice2.upper() == "Y":
                color = input("What was its main color? ")
                BirdColor(color)
        elif more.upper() == "N":
            choice2 = input("Would you like to also search by color? (Y/N) ")
            if choice2.upper() == "Y":
                color = input("What was its main/primary color? ")
                BirdColor(color)
            if choice2.upper() == "N":
                print("It was probably...")
                for item in birdfound:
                    print(item)
    if choice.lower() == "color":
        color = input("What was its main/primary color? ")
        BirdColor(color)
        more = input("Would you like to search by what it was eating now? (Y/N) ")
        if more.upper() == "Y":
            food = input("What did you see it eating? ")
            BirdFood2(food)
            more2 = input("Did you see it eating anything else? (Y/N) ")
            if more2.upper() == "Y":
                food3 = input("What other food was it eating? ")
                BirdFood3(food3)
            else:
                print("Then you probably saw a...")
                for item in finalbird:
                    print(item)
        else:
            print("It was probably...")
            for item in birdfound:
                print(item)






#main
BirdColor("blue")
