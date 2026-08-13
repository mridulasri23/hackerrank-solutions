# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/markov-snakes-and-ladders/problem?isFullScreen=true
# Problem     Markov's Snakes And Ladders
# Difficulty  Medium
# Subdomain   Statistics and Machine Learning
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-13, 10:34 a.m.
# Technique   monte-carlo-simulation
# Time        O(T * games * max_rolls)
# Space       O(L + S)
# Insight     The simulation approximates the expected value by averaging the number of rolls across 5000 independent trials, discarding games that exceed the 1000-roll threshold.
# Interview   Before: "How would you calculate the expected number of rolls for this board?" After: "I used a Monte Carlo simulation with 5000 trials to approximate the expected value, which runs in O(T * games * max_rolls) time, ensuring we handle the biased die and board constraints correctly."
# Pitfalls    (1) Failing to handle the rule where rolls resulting in a position greater than 100 are wasted.  (2) Incorrectly counting games that do not reach square 100 within the 1000-roll limit.  (3) Misinterpreting the ladder and snake movement rules as optional rather than mandatory transitions.
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
