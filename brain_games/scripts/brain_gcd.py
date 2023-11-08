#!/usr/bin/env python3
from brain_games import consts
from brain_games.games import gcd


def main():
    gcd.ask_question_gcd(attempts=consts.ATTEMPTS_CNT)


if __name__ == '__main__':
    main()
