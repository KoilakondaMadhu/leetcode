class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counters = sorted([(word, count) for word, count in Counter(words).items()],
                          key=lambda x: (-x[1], x[0]))
        return [word for word, _ in counters[:k]]
