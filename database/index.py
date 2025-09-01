from read_file import read_file
from pages import mount_pages
from buckets import Bucket
from hash_function import hash_word
from metrics import calculate_rate_bucket_overflows

words = read_file("words.txt")
pages = mount_pages(10, words)
buckets = Bucket.create_buckets(500, 1000)

for page_index, word_indices in enumerate(pages):
    for word_index in word_indices:
        word = words[word_index]
        bucket_index = hash_word(str(word), len(buckets))
        buckets[bucket_index].add_word(str(word), page_index)

for bucket in buckets:
    print(bucket)
    for overflow in bucket.overflows:
        print("  ", overflow)

print(f"Total pages: {len(pages)}")
print(f"Rate of bucket overflows: {calculate_rate_bucket_overflows(buckets):.2%}")
