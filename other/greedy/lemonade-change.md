## Links
[Leetcode](https://leetcode.com/problems/lemonade-change/)

### Approach

**code**:
```python
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        FIXED_PRICE = 5
        five, ten = 0, 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                ten += 1

            return_change = bill - FIXED_PRICE # 5 | 15

            if return_change == 5:
                if five > 0:
                    five -= 1
                else:
                    return False
            elif return_change == 15: # (5,5,5) | (5, 10)
                if five > 0 and ten > 0: # (5,10)
                    five, ten = five-1, ten-1
                elif five >= 3: # (5,5,5)
                    five -= 3
                else:
                    return False
        return True
```

**Efficiency**:
- Time: O(N)
- Space: O(1)

