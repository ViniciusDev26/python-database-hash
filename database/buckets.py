import math


class Bucket:
    """Class representing a bucket with a name and a list of words."""

    def __init__(self, name: str, bucket_size: int, words: dict[str, str]) -> None:
        self.name = name
        self.bucket_size = bucket_size
        self.words = words
        self.overflows = []
        self.collisions = 0
        self.overflow_count = 0

    def __repr__(self) -> str:
        return f"Bucket(name={self.name}, words={self.words})"

    def add_bucket_overflow(self) -> None:
        """Add a bucket overflow indicator."""
        overflow_bucket = Bucket(
            name=f"{self.name} - OVERFLOW - {len(self.overflows)}",
            bucket_size=self.bucket_size,
            words={},
        )
        self.overflows.append(overflow_bucket)

    def get_last_bucket_overflow(self) -> "Bucket | None":
        """Get the last bucket overflow if it exists."""
        if self.overflows:
            return self.overflows[-1]
        return None

    def get_total_collisions(self) -> int:
        """Get total collisions in this bucket and its overflows."""
        total = self.collisions
        for overflow in self.overflows:
            total += overflow.get_total_collisions()
        return total

    def is_full(self) -> bool:
        """Check if the bucket is full."""
        return len(self.words) >= self.bucket_size

    def add_word(self, word: str, page: str):
        """Add a word to the bucket."""
        if self.is_full():
            # Colisão: bucket cheio, nova palavra precisa ir para overflow
            self.collisions += 1

            last_overflow = self.get_last_bucket_overflow()
            if last_overflow is None or last_overflow.is_full():
                self.add_bucket_overflow()
                last_overflow = self.get_last_bucket_overflow()

            last_overflow.add_word(word, page)
            return

        self.words[word] = page

    @staticmethod
    def create_buckets(quantity_words, bucket_size):
        """Create a list of buckets with specified quantity."""
        quantity = math.ceil((quantity_words * 1.2) / bucket_size)

        buckets = [
            Bucket(name=f"Bucket {i+1}", bucket_size=bucket_size, words={})
            for i in range(quantity)
        ]

        return buckets
