def mount_pages(page_size: int, words_list: list[str]) -> list[list[str]]:
    """Mount pages from a list of words.

    Args:
        page_size (int): Number of words per page.
        words_list (list[str]): List of words to be paginated.

    Returns:
        list[list[int]]: List of pages, each containing words.
    """
    pages = []
    current_page = []

    for word in words_list:
        current_page.append(word)

        if len(current_page) == page_size:
            pages.append(current_page)
            current_page = []

    if current_page:
        pages.append(current_page)

    return pages
