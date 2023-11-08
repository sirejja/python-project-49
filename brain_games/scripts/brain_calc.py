#!/usr/bin/env python3
from brain_games import consts
from brain_games.games import calc


def main():
    calc.ask_question_to_calc(attempts=consts.ATTEMPTS_CNT)


if __name__ == '__main__':
    main()
