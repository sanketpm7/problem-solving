"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/


Pattern: sliding window


"""

# Brute Force
# T = O(N^2)
# S = O(N)

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         maxlen = 0
#         for i in range(len(s)):
#             res = ""
#             for j in range(i, len(s)):
#                 if s[j] in res:
#                     break
#                 maxlen = max(maxlen, len(res))
#         return maxlen
#

# Optimized
# T = O(N)
# S = O(N)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        uniq = set()
        max_len = 0

        while r < len(s):
            if s[r] in uniq:
                uniq.remove(s[l])
                l += 1
            else:
                uniq.add(s[r])
                max_len = max(max_len, len(uniq))
                r += 1
        return max_len


def test_lengthOfLongestSubstring():
    input_result = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
    ]
    for i, (input, result) in enumerate(input_result):
        assert Solution().lengthOfLongestSubstring(input) == result, f"Test:[{i}] - FAILED"

