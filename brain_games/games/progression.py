import random

from brain_games.cli import process_game_flow


def find_gcd(a: int, b: int):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b


def ask_question_progression(attempts: int) -> None:
    questions = []
    correct_answers = []
    for _ in range(attempts):
        progression_numbers = []

        step = random.randint(1, 100)
        number = random.randint(1, 1000)
        progression_numbers.append(str(number))

        for _ in range(10):
            number += step
            progression_numbers.append(str(number))

        hidden_number_idx = random.randint(0, len(progression_numbers) - 1)
        correct_answers.append(str(progression_numbers[hidden_number_idx]))
        progression_numbers[hidden_number_idx] = '..'

        questions.append(' '.join(progression_numbers))

    process_game_flow(
        questions_answers=zip(questions, correct_answers),
        start_phrase='What number is missing in the progression?'
    )
