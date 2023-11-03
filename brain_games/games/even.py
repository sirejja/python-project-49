#!/usr/bin/env python3
import random

from brain_games.cli import process_game_flow


def check_even(number: int):
    yes_answer = 'yes'
    no_answer = 'no'
    if number % 2 == 0:
        return yes_answer
    return no_answer


def ask_question_even(n: int = 3):
    numbers = [random.randint(1, 1000) for _ in range(n)]
    results = [check_even(number=number) for number in numbers]

    process_game_flow(
        questions=numbers,
        correct_answers=results,
        start_phrase='Answer "yes" if the number is even'
                     ', otherwise answer "no".'
    )
