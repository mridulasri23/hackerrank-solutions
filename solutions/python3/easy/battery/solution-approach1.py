# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/battery/problem?isFullScreen=true
# Problem     Laptop Battery Life
# Difficulty  Easy
# Subdomain   Statistics and Machine Learning
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-13, 10:15 a.m.
# Technique   linear-regression-threshold-clipping
# Time        O(1)
# Space       O(1)
# Insight     The model assumes a linear relationship between charging time and battery life up to a saturation point of four hours, after which the battery life remains constant at eight hours.
# Interview   Before: "How would you model this battery data?" After: "I observed the training data shows a linear trend y=2x that plateaus at 8.00 hours. By applying a conditional threshold at 4.00 hours, I achieve O(1) time complexity while respecting the saturation limit observed in the dataset."
# Pitfalls    (1) Failing to account for the saturation point at 4.00 hours leads to overestimating battery life for long charge durations.  (2) Assuming a strictly linear model without the 8.00-hour cap violates the observed behavior in the training data.
# ──────────────────────────────────────────────────

timeCharged = float(input().strip())

if timeCharged >= 4.0:
    print("8.00")
else:
    print(f"{2 * timeCharged:.2f}")
