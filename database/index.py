from read_file import read_file
from pages import mount_pages
from buckets import Bucket
import hash_function
from metrics import show_parameters


def run(lines_per_page: int, bucket_size) -> dict:
    words = read_file("words.txt")
    pages = mount_pages(lines_per_page, words)

    buckets = Bucket.create_buckets(len(words), bucket_size)
    collisions = 0

    for page_index, word_indices in enumerate(pages):
        for word in word_indices:
            bucket_index = hash_function.hash_fnv1a(str(word), len(buckets))
            has_collision = buckets[bucket_index].add_word(str(word), page_index)
            if has_collision:
                collisions += 1

    for bucket in buckets:
        if len(bucket.overflows) > 2:
            print(f"{bucket.name}: {len(bucket.overflows)}")

    return show_parameters(
        words=words, num_pages=len(pages), buckets=buckets, collisions=collisions
    )


run(lines_per_page=100, bucket_size=1)
