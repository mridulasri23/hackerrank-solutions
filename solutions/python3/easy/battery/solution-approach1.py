# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/battery/problem?isFullScreen=true
# Problem     Laptop Battery Life
# Difficulty  Easy
# Subdomain   Statistics and Machine Learning
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-13, 10:15 a.m.
# ──────────────────────────────────────────────────

timeCharged = float(input().strip())

if timeCharged >= 4.0:
    print("8.00")
else:
    print(f"{2 * timeCharged:.2f}")
