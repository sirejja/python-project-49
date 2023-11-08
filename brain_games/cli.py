import typing

import prompt


def welcome_user() -> str:
    print('\nWelcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    return name


def process_game_flow(
        start_phrase: str,
        questions_answers: typing.Iterable[tuple[str, str]],
):
    name = welcome_user()
    print(start_phrase)

    for question, correct_answer in questions_answers:

        print(f'Question: {question}')

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
