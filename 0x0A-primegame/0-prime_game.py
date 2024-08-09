#!/usr/bin/python3
"""
The prime game algorithm module.
"""

def is_prime(n):
    """
    Check if a number is prime.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False
    # check if prime
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def primes_from_range(n):
    """
    Find all prime numbers in a given range.

    Args:
        n (int): The upper limit of the range (inclusive).

    Returns:
        list: A list of prime numbers up to n.
    """
    primes = []
    # loop through the array and find primes
    for i in range(2, n + 1):
        if is_prime(i):
            # add to teh primes list
            primes.append(i)
    return primes

def round_winner(primes):
    """
    Simulate a round of the prime game.

    Maria and Ben take turns playing. Maria starts first.
    Each player picks a prime number and removes it and its multiples from the list.
    The player who cannot make a move loses.

    Args:
        primes (list): The list of prime numbers.

    Returns:
        str: "Maria" if Maria wins, "Ben" if Ben wins.
    """
    # 0 for Maria, 1 for Ben
    current_player = 0
    while primes:
        # remove the played primes
        prime = primes.pop(0)
        # remove the multiples of the played prime
        primes = [x for x in primes if x % prime != 0]
        # switch the player
        current_player = 1 - current_player
    return "Maria" if current_player == 1 else "Ben"

def isWinner(x, nums):
    """
    Determine the overall winner after x rounds of the prime game.

    Args:
        x (int): The number of rounds.
        nums (list): A list of integers representing the upper limit for each round.

    Returns:
        str: "Maria" if Maria wins more rounds, "Ben" if Ben wins more rounds,
             or None if there is a tie.
    """
    # first check
    if not nums or x < 1:
        return None

    maria_wins = 0
    ben_wins = 0

    # play each round of the game
    for round in range(x):
        primes = primes_from_range(nums[round])
        winner = round_winner(primes)
        # assign points to the winner
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    # return the game results
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
