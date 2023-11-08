#!/usr/bin/env python3
from brain_games import consts
from brain_games.games import progression


def main():
    progression.ask_question_progression(attempts=consts.ATTEMPTS_CNT)


if __name__ == '__main__':
    main()
