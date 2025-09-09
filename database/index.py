from read_file import read_file
from pages import mount_pages
from buckets import Bucket
import hash_function
from metrics import show_parameters
from loguru import logger


def run(lines_per_page: int, bucket_size) -> dict:
    logger.info(
        f"Starting database hash run with {lines_per_page} lines per page and bucket size {bucket_size}"
    )

    words = read_file("words.txt")
    logger.success(f"Read {len(words)} words from file")

    pages = mount_pages(lines_per_page, words)
    logger.success(f"Created {len(pages)} pages")

    buckets = Bucket.create_buckets(len(words), bucket_size)

    logger.info("Starting word insertion process")
    for page_index, word_indices in enumerate(pages):
        for word in word_indices:
            bucket_index = hash_function.hash_fnv1a(str(word), len(buckets))
            buckets[bucket_index].add_word(str(word), page_index)

    logger.info("Finished word insertion process")

    # Get metrics
    metrics = show_parameters(words=words, num_pages=len(pages), buckets=buckets)

    # Log all metrics in success message with line breaks
    metrics_str = "\n".join([f"  {key}: {value}" for key, value in metrics.items()])
    logger.success(f"Process completed:\n{metrics_str}")

    return metrics


run(lines_per_page=100, bucket_size=300)
