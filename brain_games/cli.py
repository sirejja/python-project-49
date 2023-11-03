import time

import prompt


def welcome_user() -> str:
    print('Welcome to the Brain Games!')
    # hack for early prompt
    time.sleep(0.5)
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    return name


def process_game_flow(
        start_phrase: str | None = None,
        questions: list[str | int] | None = None,
        correct_answers: list[str] | None = None,
):
    name = welcome_user()
    if not any((start_phrase, questions, correct_answers)):
        return

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
