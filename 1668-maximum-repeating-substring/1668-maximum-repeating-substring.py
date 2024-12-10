class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        count = 0
        current_sequence = word

        while current_sequence in sequence:
            count += 1
            current_sequence += word

        return count