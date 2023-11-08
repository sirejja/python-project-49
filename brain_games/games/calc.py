import random

from brain_games.cli import process_game_flow


def eval_calc_question(
        sign: str,
        a_number: int,
        b_number: int,
) -> int:
    match sign:
        case '-':
            return a_number - b_number
        case '+':
            return a_number + b_number
        case '*':
            return a_number * b_number
        case _:
            raise ValueError


def ask_question_to_calc(attempts: int) -> None:
    signs = ('-', '+', '*')
    questions = []
    correct_answers = []

    for _ in range(attempts):
        sign = random.choice(signs)
        a_number = random.randint(1, 100)
        b_number = random.randint(1, 100)

        correct_answers.append(
            str(
                eval_calc_question(
                    sign=sign,
                    a_number=a_number,
                    b_number=b_number,
                )
            )
        )
        questions.append(f'{a_number} {sign} {b_number}')

    process_game_flow(
        questions_answers=zip(questions, correct_answers),
        start_phrase='What is the result of the expression?'
    )
