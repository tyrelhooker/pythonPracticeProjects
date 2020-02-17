#! /usr/bin/python3

import random
import os
import statedata

all_states_info = statedata.us_states
capitals = {}
states_and_capitals = all_states_info.values()

for i in states_and_capitals:
    capitals[i['name']] = i['capital']


# Make a new directory on computer
if not os.path.exists('/home/tj/Documents/capitalQuizzes'):
    os.makedirs('/home/tj/Documents/capitalQuizzes')

for quiz_num in range(20):
    # Opens quiz and answer key on each iteration
    quiz = open(f'/home/tj/Documents/capitalQuizzes/quiz_{quiz_num}', 'w')
    answer_key = open(f'/home/tj/Documents/capitalQuizzes/answer_key_{quiz_num}', 'w')

    # Headers for each txt file
    quiz.write(f'State Capital Quiz v. {quiz_num}')
    answer_key.write(f'Answer Key to Capital Quiz version: {quiz_num}')

    # Shuffles state order for each quiz
    states = list(capitals.keys())
    random.shuffle(states)

    # Builds multiple choice answer choices
    for question_num in range(50):
        correct_answer = capitals[states[question_num]]
        wrong_answers = list(capitals.values())
        del wrong_answers[wrong_answers.index(correct_answer)]
        rand_wrong_answers = random.sample(wrong_answers, 3)
        answer_choices = rand_wrong_answers + [correct_answer]
        random.shuffle(answer_choices)

        # Builds quiz questions and answer choices to write to txt file
        # TODO: Refactor the code building the answer choices to better format
        question = f'\n {question_num + 1}. What is the capital of {states[question_num]}?'
        answer_letters = ['(a): ', '(b): ', '(c): ', '(d): ']
        answers = ''
        for choices in range(len(answer_letters)):
            answers += f'{answer_letters[choices]} {answer_choices[choices]} \n'

        # Write the results to a quiz and key txt document
        quiz.write(
            question + '\n' + answers
        )
        # TODO: Refactor the code to include the letter of the correct answer
        answer_key.write(
            question + '\t\n' + correct_answer
        )

    quiz.close()
    answer_key.close()