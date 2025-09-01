def mount_pages(page_size: int, words_list: list[str]) -> list[list[int]]:
    """Mount pages from a list of words.

    Args:
        page_size (int): Number of words per page.
        words_list (list[str]): List of words to be paginated.

    Returns:
        list[list[int]]: List of pages, each containing indices of words.
    """
    pages = []
    for i in range(0, len(words_list), page_size):
        page = list(range(i, min(i + page_size, len(words_list))))
        pages.append(page)
    return pages
