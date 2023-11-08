import random

from brain_games import consts
from brain_games.cli import process_game_flow


def is_even(number: int) -> bool:
    if number % 2 == 0:
        return True
    return False


def ask_question_even(attempts: int):
    questions = []
    correct_answers = []

    for _ in range(attempts):
        number = random.randint(1, 1000)

        if is_even(number=number):
            correct_answer = consts.YES_ANSWER
        else:
            correct_answer = consts.NO_ANSWER

        questions.append(number)
        correct_answers.append(str(correct_answer))

    process_game_flow(
        questions_answers=list(zip(questions, correct_answers)),
        start_phrase='Answer "yes" if the number is even'
                     ', otherwise answer "no".'
    )
