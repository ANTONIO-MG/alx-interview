#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    Validate if a given dataset represents a valid UTF-8 encoding.

    :param data: List of integers
    :return: True if data is a valid UTF-8 encoding, else False
    """
    num_bytes = 0

    # Masks for checking the most significant bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for num in data:
        mask = 1 << 7
        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            while mask & num:
                num_bytes += 1
                mask = mask >> 1

            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Check that the next num_bytes - 1 integers follow 10xxxxxx format
            if not (num & mask1 and not (num & mask2)):
                return False

        num_bytes -= 1

    return num_bytes == 0


if __name__ == "__main__":
    # Example test cases
    data = [65]
    print(validUTF8(data))  # True

    data = [80, 121, 116, 104, 111, 110, 32,
            105, 115, 32, 99, 111, 111, 108, 33]
    print(validUTF8(data))  # True

    data = [229, 65, 127, 256]
    print(validUTF8(data))  # False
