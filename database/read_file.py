def read_file(read_path="data.txt") -> list[str]:
    """
    Read a file and return its contents as a list of words.

    Args:
        read_path (str): The path to the file to read. Defaults to "data.txt".

    Returns:
        list[str]: A list of words from the file.
    """
    with open(read_path, "r", encoding="utf-8") as file:
        content = file.read()
        words = content.split()
    return words
