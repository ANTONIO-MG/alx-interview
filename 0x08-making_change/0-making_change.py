#!/usr/bin/python3
"""
Change comes from within
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    :param coins: List of the values of the coins in your possession
    :param total: The total amount to meet with the fewest number of coins
    :return: The fewest number of coins needed to meet total, or -1 if not possible
    """
    if total <= 0:
        return 0

    # Initialize a list to store the minimum coins needed for each amount up to total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Compute the minimum coins needed for each amount
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still float('inf'), it means it's not possible to form total with given coins
    return dp[total] if dp[total] != float('inf') else -1


if __name__ == "__main__":
    # Example test cases
    print(makeChange([1, 2, 25], 37))  # Expected output: 7
    print(makeChange([1256, 54, 48, 16, 102], 1453))  # Expected output: -1
