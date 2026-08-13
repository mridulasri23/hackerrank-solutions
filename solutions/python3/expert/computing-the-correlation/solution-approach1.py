# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/computing-the-correlation/problem?isFullScreen=true
# Problem     Day 5: Computing the Correlation
# Difficulty  Expert
# Subdomain   Statistics and Machine Learning
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-13, 10:32 a.m.
# ──────────────────────────────────────────────────

import math

n = int(input())

a = []
b = []
c = []

for _ in range(n):
    x, y, z = map(float, input().split())
    a.append(x)
    b.append(y)
    c.append(z)


def correlation(x, y):
    mx = sum(x) / n
    my = sum(y) / n

    numerator = sum((x[i] - mx) * (y[i] - my) for i in range(n))

    den1 = math.sqrt(sum((x[i] - mx) ** 2 for i in range(n)))
    den2 = math.sqrt(sum((y[i] - my) ** 2 for i in range(n)))

    return numerator / (den1 * den2)


print(f"{correlation(a, b):.2f}")
print(f"{correlation(b, c):.2f}")
print(f"{correlation(a, c):.2f}")
