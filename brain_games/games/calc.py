#!/usr/bin/env python3
import random

from brain_games.scripts import process_game_flow


def ask_question_to_calc(n: int = 3):
    signs = ('-', '+', '*')
    questions = [
        f'{random.randint(1, 1000)} {random.choice(signs)} {random.randint(1, 1000)}'
        for _ in range(n)
    ]
    correct_answers = [str(eval(question)) for question in questions]

    process_game_flow(
        questions=questions,
        correct_answers=correct_answers,
        start_phrase='What is the result of the expression?'
    )
