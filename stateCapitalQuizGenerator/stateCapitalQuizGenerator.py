#! /usr/bin/python3

import random
import os
import statedata
import pkgutil
import sys

all_states_info = statedata.us_states
capitals = {}


states_and_capitals = all_states_info.values()

for i in states_and_capitals:
    capitals[i['name']] = i['capital']
# print(capitals)

# Make a new directory on computer
if not os.path.exists('/home/tj/Documents/automateTheBoring/capitalQuizzes'):
    os.makedirs('/home/tj/Documents/automateTheBoring/capitalQuizzes')

for quiz_num in range(3):
    # TODO: Create quiz and answer key
    quiz = open(f'/home/tj/Documents/automateTheBoring/capitalQuizzes/quiz_{quiz_num}', 'w')
    answer_key = open(f'/home/tj/Documents/automateTheBoring/capitalQuizzes/answer_key_{quiz_num}', 'w')

    quiz.write(f'Capital Quiz version: {quiz_num}')
    answer_key.write(f'Answer Key to Capital Quiz version: {quiz_num}')

    states = list(capitals.keys())
    random.shuffle(states)
    print(states)

    # TODO: Create Header for the Quiz
    # TODO: Shuffle the order of capitals
    # TODO: Create test code to ask 'What is the capital of <state>?' for all 50 states
    # for state in capitals:
    #     # print(state)
    #     capital = capitals[state]
    #     choices = []
    #     print(f'What is the capital of {state}?')
    #     choices.append(capital)
    #     for wrong_choices in range(1, 4):
    #         choices.append(random.capitals.values())

    # TODO: Create code for 4 multiple choice answers a-d 1 being right and 4 wrong

    # TODO: Write the results to a txt document
    quiz.close()
    answer_key.close()