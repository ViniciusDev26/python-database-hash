def calculate_rate_bucket_overflows(buckets: list) -> float:
    """Calculate the rate of bucket overflows."""
    total_buckets = len(buckets)
    if total_buckets == 0:
        return 0.0

    overflow_count = sum(len(bucket.overflows) for bucket in buckets)
    return overflow_count / total_buckets


def calculate_page_quantity(pages: list) -> int:
    """Calculate the total number of pages."""
    return len(pages)


def show_parameters(num_pages, buckets, collisions) -> None:
    """Display parameters in a readable format."""
    print(f"Total pages: {num_pages}")
    print(f"Total collisions: {collisions}")
    print(f"Rate of bucket overflows: {calculate_rate_bucket_overflows(buckets):.2%}")
