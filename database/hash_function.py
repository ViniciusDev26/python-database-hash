def hash_fnv1a(word, max_number):
    """
    FNV-1a hash function with better collision resistance.

    Args:
        word (str): The word to hash
        max_number (int): Maximum number in the range (exclusive)

    Returns:
        int: Integer in range [0, max_number)
    """
    if max_number <= 0:
        raise ValueError("max_number must be positive")

    # FNV-1a constants
    FNV_OFFSET_BASIS = 2166136261
    FNV_PRIME = 16777619

    hash_value = FNV_OFFSET_BASIS

    for char in word:
        hash_value ^= ord(char)
        hash_value *= FNV_PRIME
        hash_value &= 0xFFFFFFFF  # Keep it 32-bit

    return hash_value % max_number


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


def hash_djb2(word, max_number):
    """
    DJB2 hash function - another alternative with good distribution.

    Args:
        word (str): The word to hash
        max_number (int): Maximum number in the range (exclusive)

    Returns:
        int: Integer in range [0, max_number)
    """
    if max_number <= 0:
        raise ValueError("max_number must be positive")

    hash_value = 5381

    for char in word:
        hash_value = ((hash_value << 5) + hash_value) + ord(char)
        hash_value &= 0xFFFFFFFF  # Keep it 32-bit

    return hash_value % max_number


def find_word_in_buckets(word, buckets):
    """
    Find a word in the list of buckets.

    Args:
        word (str): The word to find
        buckets (list): List of Bucket objects

    Returns:
        str | None: The page where the word is found, or None if not found
    """
    index = hash_word(word, len(buckets))
    print(f"Searching for '{word}' in bucket index {index}")
    bucket = buckets[index]
    result = bucket.words[word]
    if result is None:
        for overflow in bucket.overflows:
            result = overflow.words[word]
            if result is not None:
                return result

    return result
