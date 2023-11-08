import random

from brain_games import consts
from brain_games.cli import process_game_flow


def is_prime(number: int) -> bool:
    for i in range(2, (number // 2) + 1):
        if number % i == 0:
            return False
    return True


def ask_question_prime(attempts: int) -> None:
    questions = []
    correct_answers = []
    for _ in range(attempts):

        number = random.randint(1, 1000)
        if is_prime(number=number):
            correct_answer = consts.YES_ANSWER
        else:
            correct_answer = consts.NO_ANSWER

        correct_answers.append(correct_answer)
        questions.append(str(number))

    process_game_flow(
        questions_answers=zip(questions, correct_answers),
        start_phrase='Answer "yes" if given number is prime. '
                     'Otherwise answer "no".'
    )
