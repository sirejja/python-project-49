import time

import prompt


def welcome_user() -> str:
    print('Welcome to the Brain Games!')
    # hack for early prompt
    time.sleep(0.5)
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    return name
