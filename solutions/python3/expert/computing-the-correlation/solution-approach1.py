# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/computing-the-correlation/problem?isFullScreen=true
# Problem     Day 5: Computing the Correlation
# Difficulty  Expert
# Subdomain   Statistics and Machine Learning
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-13, 10:32 a.m.
# Technique   pearson-correlation-coefficient-calculation
# Time        O(N)
# Space       O(N)
# Insight     The Pearson correlation coefficient is computed by calculating the mean of each vector and then evaluating the ratio of the covariance to the product of the standard deviations.
# Interview   Before: "How would you calculate the linear correlation between two large datasets without external libraries?" After: "I compute the Pearson coefficient in O(N) time by iterating through the lists to find means, then calculating the covariance and standard deviations, ensuring the result is rounded to two decimal places as required."
# Pitfalls    (1) Failing to handle the floating-point precision requirements for the final output format.  (2) Assuming the input data is already normalized, which would lead to incorrect correlation results.  (3) Neglecting the O(N) space complexity when processing up to 500,000 records, which could lead to memory exhaustion.
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
