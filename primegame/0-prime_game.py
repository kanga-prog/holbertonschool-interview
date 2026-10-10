#!/usr/bin/python3
"""
Prime Game module.
"""


def isWinner(x, nums):
    """
    Determine the winner of the Prime Game.

    Args:
        x: Number of rounds.
        nums: List containing n for each round.

    Returns:
        The name of the player with the most wins,
        or None if there is no clear winner.
    """
    if x <= 0 or not nums:
        return None

    limit = max(nums[:x])

    if limit < 2:
        return "Ben"

    primes = [True] * (limit + 1)
    primes[0] = False
    primes[1] = False

    p = 2
    while p * p <= limit:
        if primes[p]:
            multiple = p * p
            while multiple <= limit:
                primes[multiple] = False
                multiple += p
        p += 1

    prime_count = [0] * (limit + 1)
    count = 0

    for i in range(limit + 1):
        if primes[i]:
            count += 1
        prime_count[i] = count

    maria = 0
    ben = 0

    for n in nums[:x]:
        if n < 2:
            ben += 1
        elif prime_count[n] % 2 == 1:
            maria += 1
        else:
            ben += 1

    if maria > ben:
        return "Maria"
    if ben > maria:
        return "Ben"

    return None
