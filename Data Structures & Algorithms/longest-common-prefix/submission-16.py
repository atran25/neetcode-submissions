class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        max_len = min(len(i) for i in strs)
        for i in range(max_len):
            cur_char = strs[0][i]
            for str in strs:
                if cur_char != str[i]:
                    return str[:i]
        return strs[0][:max_len]

            
