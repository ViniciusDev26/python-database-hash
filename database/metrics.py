from database.buckets import Bucket


def calculate_rate_bucket_overflows(buckets: list[Bucket]) -> float:
    """Calculate the rate of bucket overflows."""
    total_buckets = len(buckets)
    if total_buckets == 0:
        return 0.0

    overflow_count = sum(len(bucket.overflows) for bucket in buckets)
    return (overflow_count / total_buckets) * 100


def calculate_page_quantity(pages: list) -> int:
    """Calculate the total number of pages."""
    return len(pages)


def calculate_percentage_collisions(collisions: int, total_words: int) -> float:
    """Calculate the percentage of collisions."""
    if total_words == 0:
        return 0.0
    return (collisions / total_words) * 100


def show_parameters(words, num_pages, buckets) -> None:
    """Display parameters in a readable format."""

    overflow_count = sum(len(bucket.overflows) for bucket in buckets)
    collisions = sum(bucket.get_total_collisions() for bucket in buckets)

    metrics = {
        "Total pages": num_pages,
        "Total words": len(words),
        "Total collisions": collisions,
        "Total Buckets": len(buckets),
        "Total bucket overflows": overflow_count,
        "Percentage of collisions": calculate_percentage_collisions(
            collisions, len(words)
        ),
        "Percentage of bucket overflows": calculate_rate_bucket_overflows(buckets),
    }

    return metrics
