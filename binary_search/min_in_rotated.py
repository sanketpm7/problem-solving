"""
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

Core Logic:
----------
1. L < R -> End Case
2. M = (L + R) // 2 -> Find out M belongs to left sorted array or right sorted array

if nums[M] >= nums[L]:
    search right -> L = M + 1
else:
    search left -> R = M - 1

Dry Run:
[1, 2, 3, 4, 5] | 1
[3, 4, 5, 1, 2] | 1
[5, 1, 2, 3, 4] | 1
"""

class Solution:
    def findMin(self, nums: list[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums)-1
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res

def test_findMin():
    input_result = [
        ([3,4,5,1,2], 1),
        ([4,5,6,7,0,1,2], 0),
        ([11,13,15,17], 11),
        ([5,1,2,3,4], 1)
    ]

    for i, (input, result) in enumerate(input_result):
        assert Solution().findMin(input) == result, f"Test[{i}] - FAILED"

