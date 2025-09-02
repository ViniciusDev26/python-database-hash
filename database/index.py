from read_file import read_file
from pages import mount_pages
from buckets import Bucket
from hash_function import hash_word
from metrics import show_parameters

words = read_file("words.txt")
pages = mount_pages(10, words)
buckets = Bucket.create_buckets(500, 1000)
collisions = 0

for page_index, word_indices in enumerate(pages):
    for word_index in word_indices:
        word = words[word_index]
        bucket_index = hash_word(str(word), len(buckets))
        has_collision = buckets[bucket_index].add_word(str(word), page_index)
        if has_collision:
            collisions += 1

show_parameters(num_pages=len(pages), buckets=buckets, collisions=collisions)
