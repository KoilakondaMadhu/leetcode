class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9 + 7
        from collections import Counter

        # Count initial characters
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1

        for _ in range(t):
            new_count = [0] * 26
            for i in range(26):
                if i == 25:  # 'z'
                    new_count[0] = (new_count[0] + count[25]) % MOD  # 'a'
                    new_count[1] = (new_count[1] + count[25]) % MOD  # 'b'
                else:
                    new_count[i+1] = (new_count[i+1] + count[i]) % MOD
            count = new_count

        return sum(count) % MOD
