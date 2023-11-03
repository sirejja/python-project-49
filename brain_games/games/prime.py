#!/usr/bin/env python3
import random

from brain_games.cli import process_game_flow


def is_prime(x):
    for i in range(2, (x // 2) + 1):
        if x % i == 0:
            return 'no'
    return 'yes'


def ask_question_prime(n: int = 3):
    questions = []
    results = []
    for _ in range(n):

        number = random.randint(1, 1000)
        results.append(is_prime(number))
        questions.append(str(number))

    process_game_flow(
        questions=questions,
        correct_answers=results,
        start_phrase='Answer "yes" if given number is prime. '
                     'Otherwise answer "no".'
    )
