class Bucket:
    """Class representing a bucket with a name and a list of words."""

    def __init__(self, name: str, bucket_size: int, words: dict[str, str]) -> None:
        self.name = name
        self.bucket_size = bucket_size
        self.words = words
        self.overflows = []

    def __repr__(self) -> str:
        return f"Bucket(name={self.name}, words={self.words})"

    def add_bucket_overflow(self) -> None:
        """Add a bucket overflow indicator."""
        overflow_bucket = Bucket(
            name=f"{self.name} - OVERFLOW", bucket_size=self.bucket_size, words={}
        )
        self.overflows.append(overflow_bucket)

    def get_last_bucket_overflow(self) -> "Bucket | None":
        """Get the last bucket overflow if it exists."""
        if self.overflows:
            return self.overflows[-1]
        return None

    def is_full(self) -> bool:
        """Check if the bucket is full."""
        return len(self.words) >= self.bucket_size

    def add_word(self, word: str, page: str) -> None:
        """Add a word to the bucket."""
        if self.is_full():
            last_overflow = self.get_last_bucket_overflow()
            if last_overflow is None:
                self.add_bucket_overflow()
                last_overflow = self.get_last_bucket_overflow()

            if last_overflow.is_full():
                last_overflow.add_bucket_overflow()
                last_overflow = self.get_last_bucket_overflow()

            last_overflow.add_word(word, page)
        else:
            self.words[word] = page

    @staticmethod
    def create_buckets(quantity, bucket_size):
        """Create a list of buckets with specified quantity."""
        return [
            Bucket(name=f"Bucket {i+1}", bucket_size=bucket_size, words={})
            for i in range(quantity)
        ]
