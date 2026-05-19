class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_count = defaultdict(int)
        for char in s:
            letter_count[char] += 1

        for char in t:
            letter_count[char] -= 1

        for count in letter_count.values():
            if count != 0:
                return False
        return True