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
if not os.path.exists('/home/tj/Documents/capitalQuizzes'):
    os.makedirs('/home/tj/Documents/capitalQuizzes')

for quiz_num in range(3):
    # TODO: Create quiz and answer key
    quiz = open(f'/home/tj/Documents/capitalQuizzes/quiz_{quiz_num}', 'w')
    answer_key = open(f'/home/tj/Documents/capitalQuizzes/answer_key_{quiz_num}', 'w')

    # TODO: Create Header for the Quiz    quiz.write(f'Capital Quiz version: {quiz_num}')
    answer_key.write(f'Answer Key to Capital Quiz version: {quiz_num}')

    # TODO: Shuffle the order of the states
    states = list(capitals.keys())
    random.shuffle(states)
    # print(states)

    # TODO: Loop through all 50 states, and make a question for each
    for question_num in range(50):
        correct_answer = capitals[states[question_num]]
        # print(type(correct_answer))
        wrong_answers = list(capitals.values())
        del wrong_answers[wrong_answers.index(correct_answer)]
        rand_wrong_answers = random.sample(wrong_answers, 3)
        answer_choices = rand_wrong_answers + [correct_answer]
        random.shuffle(answer_choices)


    # TODO: Create test code to ask 'What is the capital of <state>?' for all 50 states
        question = f'\n {question_num + 1}. What is the capital of {states[question_num]}?'
        answer_letters = ['(a): ', '(b): ', '(c): ', '(d): ']
        answers = ''
        for choices in range(len(answer_letters)):
            answers += f'{answer_letters[choices]} {answer_choices[choices]} \n'
            # answer_choice_bank.append(answer_letters[choices] + answer_choices[choices])



    # TODO: Write the results to a txt document
        quiz.write(
            question + '\n' + answers
        )
        answer_key.write(
            question + '\n' + correct_answer
        )

    quiz.close()
    answer_key.close()