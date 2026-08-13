# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/markov-snakes-and-ladders/problem?isFullScreen=true
# Problem     Markov's Snakes And Ladders
# Difficulty  Medium
# Subdomain   Statistics and Machine Learning
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-13, 10:34 a.m.
# ──────────────────────────────────────────────────

import random

T = int(input())

for _ in range(T):
    # Dice probabilities
    prob = list(map(float, input().split(',')))

    # Number of ladders and snakes
    l, s = map(int, input().split(','))

    # Ladders
    ladders = {}
    line = input().strip()
    if line:
        for x in line.split():
            a, b = map(int, x.split(','))
            ladders[a] = b

    # Snakes
    snakes = {}
    line = input().strip()
    if line:
        for x in line.split():
            a, b = map(int, x.split(','))
            snakes[a] = b

    # Create weighted dice
    dice = [1, 2, 3, 4, 5, 6]

    total_rolls = 0
    games = 5000
    completed = 0

    for game in range(games):
        pos = 1
        rolls = 0

        while pos != 100 and rolls < 1000:
            # Roll biased die
            roll = random.choices(dice, weights=prob)[0]
            rolls += 1

            new_pos = pos + roll

            # Move only if <= 100
            if new_pos <= 100:
                pos = new_pos

                # Ladder
                if pos in ladders:
                    pos = ladders[pos]

                # Snake
                elif pos in snakes:
                    pos = snakes[pos]

        # Ignore games that did not finish
        if pos == 100:
            total_rolls += rolls
            completed += 1

    # Average number of rolls
    if completed > 0:
        answer = total_rolls / completed
        print(round(answer))
    else:
        print(0)
