class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(list)
        for word in strs:
            char_counter = [0] * 26
            for char in word:
                char_counter[ord(char) - ord('a')] += 1
            anagram_groups[tuple(char_counter)].append(word)
        return list(anagram_groups.values())