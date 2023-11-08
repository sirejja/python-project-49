import random

from brain_games.cli import process_game_flow


def find_gcd(a: int, b: int):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b


def ask_question_gcd(attempts: int) -> None:
    questions = []
    correct_answers = []
    for _ in range(attempts):
        a, b = random.randint(1, 10), random.randint(1, 40)
        correct_answers.append(str(find_gcd(a, b)))
        questions.append(f'{a} {b}')

    process_game_flow(
        questions_answers=zip(questions, correct_answers),
        start_phrase='Find the greatest common divisor of given numbers.'
    )
