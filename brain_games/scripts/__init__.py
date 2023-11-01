import time

import prompt

from brain_games.cli import welcome_user


def process_game_flow(
        questions: list[str | int],
        correct_answers: list[str],
        start_phrase: str
):
    name = welcome_user()
    print(start_phrase)

    for question, correct_answer in zip(questions, correct_answers):

        print(f'Question: {question}')

        # hack for early prompt
        time.sleep(0.5)

        guess_input = prompt.string('Your answer: ')

        if guess_input == correct_answer:
            print('Correct!')
        else:
            print(
                f"'{guess_input}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'.\n"
                f"Let's try again, {name}!"
            )
            return
    print(f'Congratulations, {name}!')
