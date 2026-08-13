# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/stat-warmup/problem?isFullScreen=true
# Problem     Basic Statistics Warmup
# Difficulty  Easy
# Subdomain   Statistics and Machine Learning
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-13, 10:30 a.m.
# Technique   sorting-and-frequency-counting
# Time        O(N log N)
# Space       O(N)
# Insight     The implementation calculates descriptive statistics by sorting the dataset to determine the median and using a frequency map to identify the smallest mode.
# Interview   Before: "How would you compute the mode and confidence interval for a large dataset?" After: "I would use a hash map for O(N) frequency counting and sort the array in O(N log N) to find the median, then apply the standard deviation formula to derive the 95% confidence interval."
# Pitfalls    (1) Failing to sort the array before calculating the median leads to incorrect middle-element selection.  (2) Selecting the wrong mode when multiple elements share the maximum frequency by ignoring the requirement to pick the numerically smallest integer.  (3) Using the sample standard deviation formula (dividing by N-1) instead of the population standard deviation formula (dividing by N) as specified in the problem.
# ──────────────────────────────────────────────────

import math
from collections import Counter

n = int(input())
a = list(map(int, input().split()))

# Mean
mean = sum(a) / n

# Median
a.sort()

if n % 2 == 1:
    median = a[n // 2]
else:
    median = (a[n // 2 - 1] + a[n // 2]) / 2

# Mode
count = Counter(a)
max_freq = max(count.values())
mode = min(x for x in a if count[x] == max_freq)

# Standard Deviation
sd = math.sqrt(sum((x - mean) ** 2 for x in a) / n)

# 95% Confidence Interval
margin = 1.96 * sd / math.sqrt(n)
lower = mean - margin
upper = mean + margin

print(f"{mean:.1f}")
print(f"{median:.1f}")
print(mode)
print(f"{sd:.1f}")
print(f"{lower:.1f} {upper:.1f}")
