## Links
[Leetcode](https://leetcode.com/problems/unique-paths/)

## Expected Output
No of unique paths to reach `finish`

e.g.:
**Input:**
m = 2, n = 3

**Output:**
3

## Recursive Approach
```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dfs(r, c):
            if r == m or c == n:
                return 0
            if r == m-1 or c == n-1:
                return 1
            return dfs(r+1, c)
        return dfs(0, 0)
```

## Memoization - Top Down
```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [ [-1]*n for i in range(m)]
        def dfs(r, c):
            if r == m or c == n:
                return 0
            if r == m-1 or c == n-1:
                return 1
            dp[r][c] = dfs(r+1, c)
            return dp[r][c]
        return dfs(0, 0)
```

## Tabulation - Bottom Up - 2DP
```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [ [1] * n for _ in range(m) ]
        for r in range(1, m):
            for c in range(1, n):
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
        return dp[m - 1][n - 1]
```

## Tabulation - Bottom Up - 2DP
```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for _ in range(1, m):
            for c in range(1, n):
                dp[c] = dp[c] + dp[c-1]
        return dp[n-1]
```

# Time & Space complexity

Max number of branches per node ? 
2

Max depth of the recursion tree?
- reaching from (0,0) to (m-1, n-1) - how may moves?
m-1 + n-1 = m+n-1


time complexity formula = (no of branches)^(max depth of recursion)


**Recursive Approach**
T = O(2^(m+n))
S = O(m+n) 
    - maximum size of recursion stack

**Memoization approach**
T = O(m*n)
    - each state is computed once and used from cache
S = O(m*n) + recursion stack
    - cache-states + recursion-stack

**2DP Tabulation approach**
T = O(m*n)
    - each cell is visited once
S = O(m*n)
    - grid size

**1DP Tabulation approach**
T = O(m*n)
    - each cell is visited once
S = O(n)
    - size of 1D array

