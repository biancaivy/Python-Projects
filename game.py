#game
#biancaandmaya

import random
import time
import json

def gamestart():
    def load_leaderboard(filename="leaderboard.txt"):
        try:
            with open(filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []
    def save_leaderboard(leaderboard_data, filename="leaderboard.txt"):
        with open(leaderboard.txt, 'w') as f:
            json.dump(leaderboard_data, f, indent=4)

    def add_score(leaderboard_data, name, points):
        leaderboard_data.append({"playerName": name, "score": points})
        leaderboard_data.sort(key=lambda x: x["score"], reverse=True)
        return leaderboard_data
    load_leaderboard("gameleaderboard")
    name = input("please enter your name: ")
    diff = input("please selecteasy/medium/hard: ")
    if diff == "easy":
        number = random.randint(1,50)
        answer = int(input("guess number 1 through 50: "))
        start_time = time.perf_counter()
        i=1
        while i <= 5 and number != answer:
            if answer >= number:
                answer = int(input("TOO HIGH; please guess again: "))
            elif answer <= number:
                answer = int(input("TOO LOW; please guess again: "))
            i = i+1
        end_time = time.perf_counter()
        fulltime = end_time - start_time
        if answer != number:
            print("nope! sorry!")
        if answer == number:
            add_score(leaderboard_data, name, points)
            print("correct, time taken was", fulltime , ".")
            points = fulltime/100
            print("points won: ", points)
            print(leaderboard_data)
    elif diff == "medium":
        number = random.randint(1,100)
        answer = int(input("guess number 1 through 100: "))
        start_time = time.perf_counter()
        i=1
        while i <= 5 and number != answer:
            if answer >= number:
                answer = int(input("TOO HIGH; please guess again: "))
            elif answer <= number:
                answer = int(input("TOO LOW; please guess again: "))
            i = i+1
        end_time = time.perf_counter()
        fulltime = end_time - start_time
        if answer != number:
            print("nope! sorry!")
        if answer == number:
            add_score(leaderboard_data, name, points)
            print("correct, time taken was", fulltime , ".")
            points = fulltime/2
            print("points won: ", points)
            print(leaderboard_data)
    else:
        number = random.randint(1,1000)
        answer = int(input("guess number 1 through 1000: "))
        start_time = time.perf_counter()
        i=1
        while i <= 5 and number != answer:
            if answer >= number:
                answer = int(input("TOO HIGH; please guess again: "))
            elif answer <= number:
                answer = int(input("TOO LOW; please guess again: "))
            i = i+1
        end_time = time.perf_counter()
        fulltime = end_time - start_time
        if answer != number:
            print("nope! sorry!")
        if answer == number:
            add_score(leaderboard_data, name, points)
            print("correct, time taken was", fulltime , ".")
            points = fulltime*10
            print("points won: ", points )
            leaderboard = [
{
    "playerName": name,
    "score": points,
},
{
    "playerName": name ,
    "score": points,
},
{
    "playerName": name ,
    "score": points,
}
]
            print(leaderboard)
gamestart()
