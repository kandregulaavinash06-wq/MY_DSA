# LeetCode 3
# Longest Substring Without Repeating Characters

# -------------------------
# Brute Force
# Time: O(n²)
# Space: O(n)
# -------------------------

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            seen = set()

            for j in range(i, len(s)):
                if s[j] in seen:
                    break

                seen.add(s[j])
                res = max(res, j - i + 1)

        return res


# -------------------------
# Optimized - Sliding Window
# Time: O(n)
# Space: O(n)
# -------------------------

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        d = {}
        res = 0

        for r in range(len(s)):
            if s[r] in d:
                l = max(l, d[s[r]] + 1)

            d[s[r]] = r
            res = max(res, r - l + 1)

        return res