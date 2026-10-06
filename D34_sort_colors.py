# Day 34 - LeetCode #75: Sort Colors
# https://leetcode.com/problems/sort-colors/
#
# Given an array containing only 0, 1, and 2,
# sort it in-place without using the built-in sort() function.
#
# I tried three approaches:
# 1. Optimized Bubble Sort
# 2. Dutch National Flag Algorithm
# 3. Counting approach


class Solution:

    # Approach 1: Optimized Bubble Sort
    #
    # Compare adjacent elements and swap them when they
    # are in the wrong order.
    #
    # The flag checks whether any swap happened during
    # a complete pass. If no swap happens, the array
    # is already sorted, so we can stop early.
    #
    # Time Complexity:
    # Best: O(n)
    # Average/Worst: O(n^2)
    #
    # Space Complexity: O(1)

    def sortColors_bubble(self, nums: list[int]) -> None:
        for i in range(len(nums)):

            flag = False

            for j in range(len(nums) - i - 1):

                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    flag = True

            if not flag:
                break


    # Approach 2: Dutch National Flag Algorithm
    #
    # Use three pointers:
    # low  -> position where the next 0 should go
    # mid  -> current element being checked
    # high -> position where the next 2 should go
    #
    # 0 -> swap with low and move both low and mid
    # 1 -> already in the correct middle section
    # 2 -> swap with high and move only high
    #
    # Time Complexity: O(n)
    # Space Complexity: O(1)

    def sortColors_dutch_flag(self, nums: list[int]) -> None:
        low, mid, high = 0, 0, len(nums) - 1

        while mid <= high:

            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            elif nums[mid] == 1:
                mid += 1

            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1


    # Approach 3: Counting Approach
    #
    # Count how many 0s, 1s, and 2s are present.
    # Then overwrite the original array using those counts.
    #
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    #
    # Only three counters are used, so the extra space
    # remains constant.

    def sortColors_counting(self, nums: list[int]) -> None:
        z, o, t = 0, 0, 0

        # Count the number of 0s, 1s, and 2s.
        for i in nums:
            if i == 0:
                z += 1
            elif i == 1:
                o += 1
            else:
                t += 1

        i = 0

        # Rewrite the array in sorted order.
        while i < len(nums):

            if z > 0:
                nums[i] = 0
                z -= 1

            elif o > 0:
                nums[i] = 1
                o -= 1

            else:
                nums[i] = 2
                t -= 1

            i += 1