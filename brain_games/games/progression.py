#!/usr/bin/env python3
import random

from brain_games.scripts import process_game_flow


def find_gcd(a: int, b: int):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b


def ask_question_progression(n: int = 3):
    questions = []
    results = []
    for _ in range(n):
        progression_numbers = []

        step = random.randint(1, 1000)
        number = random.randint(1, 1000)
        progression_numbers.append(str(number))

        for _ in range(10):
            number += step
            progression_numbers.append(str(number))

        hidden_number_idx = random.randint(0, len(progression_numbers) - 1)
        results.append(str(progression_numbers[hidden_number_idx]))
        progression_numbers[hidden_number_idx] = '..'

        questions.append(' '.join(progression_numbers))

    process_game_flow(
        questions=questions,
        correct_answers=results,
        start_phrase='What number is missing in the progression?'
    )

