mask1 (10000000): Used to check the most significant bit (MSB).
mask2 (01000000): Used to check the second MSB.
Iteration through data:

For each integer in data, check if it is part of a UTF-8 character.
If num_bytes is zero, determine how many bytes the UTF-8 character has.
If num_bytes is not zero, check if the integer follows the format for the continuation bytes (10xxxxxx).
Validation:

The first byte determines the length of the UTF-8 character.
If num_bytes is greater than 1, each following byte must start with 10.
Return True if all bytes are valid UTF-8, otherwise False.