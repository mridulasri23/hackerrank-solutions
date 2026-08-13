# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/stat-warmup/problem?isFullScreen=true
# Problem     Basic Statistics Warmup
# Difficulty  Easy
# Subdomain   Statistics and Machine Learning
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-13, 10:30 a.m.
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
