" Longest Substring Without Repeating Characters "

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        i, j, maxlen, curlen = 0, 0, 0, 0
        while j < len(s):
            char = s[j]
            if char in chars:
                chars.remove(s[i])
                i += 1
            else:
                chars.add(char)
                j += 1
            curlen = j - i
            maxlen = max(maxlen, curlen)

        return maxlen
