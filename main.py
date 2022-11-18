from art import logo, vs
from game_data import data
import os
import random


def clear(): return os.system("cls")


person_1 = random.choice(data)


# print(person_1)
# print(person_2)

correct = True
score = 0
while correct:
    person_2 = random.choice(data)
    # Ensure there are two different people
    while person_1["name"] == person_2["name"]:
        person_2 = random.choice(data)

    higher_count_person = person_1
    if person_2["follower_count"] > person_1["follower_count"]:
        higher_count_person = person_2

    print(logo)

    if score > 0:
        print(f"You're right! Current score: {score}")

    print(
        f"Compare A: {person_1['name']}, a {person_1['description']}, from {person_1['country']}")

    print(vs)

    print(
        f"Compare B: {person_2['name']}, a {person_2['description']}, from {person_2['country']}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    correct_guess = False

    if guess == "a":
        if person_1["follower_count"] == higher_count_person["follower_count"]:
            correct_guess = True
            score += 1
    elif guess == "b":
        if person_2["follower_count"] == higher_count_person["follower_count"]:
            correct_guess = True
            score += 1

    if correct_guess:
        person_1 = higher_count_person
        clear()
    else:
        correct = False
        clear()

print(logo)
print(f"Sorry, that's wrong. Final score: {score}")
