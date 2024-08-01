#!/usr/bin/python3
"""
Change comes from within
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    :param coins: List of the values of the coins in your possession
    :param total: The total amount to meet with the fewest number of coins
    :return: The fewest number of coins needed to meet total,
    or -1 if not possible
    """
    if total <= 0:
        return 0

    # Initialize a list to store the minimum coins needed
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Compute the minimum coins needed for each amount
    for i in range(1, total + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still float('inf')
    return dp[total] if dp[total] != float('inf') else -1


if __name__ == "__main__":
    import time

    makeChange = __import__('0-making_change').makeChange

    start = time.time()

    for i in range(10):
        makeChange([2, 4, 6, 10], 1278653)

    end = time.time()

    avg = (end - start) / 10

    if avg > 3:
        print("Runtime too long")
    else:
        print("OK")
