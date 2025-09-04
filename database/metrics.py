from buckets import Bucket


def calculate_rate_bucket_overflows(buckets: list[Bucket]) -> float:
    """Calculate the rate of bucket overflows."""
    total_buckets = len(buckets)
    if total_buckets == 0:
        return 0.0

    overflow_count = sum(len(bucket.overflows) for bucket in buckets)
    return overflow_count / total_buckets


def calculate_page_quantity(pages: list) -> int:
    """Calculate the total number of pages."""
    return len(pages)


def calculate_percentage_collisions(collisions: int, total_words: int) -> float:
    """Calculate the percentage of collisions."""
    if total_words == 0:
        return 0.0
    return (collisions / total_words) * 100


def show_parameters(words, num_pages, buckets, collisions) -> None:
    """Display parameters in a readable format."""

    metrics = {
        "Total pages": num_pages,
        "Total collisions": collisions,
        "Percentage of collisions": calculate_percentage_collisions(
            collisions, len(words)
        ),
        "Rate of bucket overflows": calculate_rate_bucket_overflows(buckets),
    }

    for key, value in metrics.items():
        print(f"{key}: {value}")

    return metrics
