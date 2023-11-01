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


def ask_question_gcd(n: int = 3):
    questions = []
    results = []
    for _ in range(n):
        a, b = random.randint(1, 100), random.randint(1, 100)
        results.append(str(find_gcd(a, b)))
        questions.append(f'{a} {b}')

    process_game_flow(
        questions=questions,
        correct_answers=results,
        start_phrase='Find the greatest common divisor of given numbers.'
    )
