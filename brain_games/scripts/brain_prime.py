#!/usr/bin/env python3
from brain_games import consts
from brain_games.games import prime


def main():
    prime.ask_question_prime(attempts=consts.ATTEMPTS_CNT)


if __name__ == '__main__':
    main()
