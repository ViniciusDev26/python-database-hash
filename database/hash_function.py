def hash_word(word, max_number):
    """
    Hash a word to an integer using a better distribution to avoid collisions.

    Args:
        word (str): The word to hash
        max_number (int): Maximum number in the range (exclusive)

    Returns:
        int: Integer in range [0, max_number)
    """
    if max_number <= 0:
        raise ValueError("max_number must be positive")

    # Use polynomial rolling hash with a prime multiplier to reduce collisions
    hash_value = 0
    prime = 31

    for i, char in enumerate(word):
        hash_value += ord(char) * (prime**i)

    return hash_value % max_number
