#!/usr/bin/env python3
from brain_games import consts
from brain_games.games import even


def main():
    even.ask_question_even(attempts=consts.ATTEMPTS_CNT)


if __name__ == '__main__':
    main()
