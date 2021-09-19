from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:

        left, left_max = 0, 0
        right, right_max = len(height)-1, height[len(height)-1]
        volume = 0

        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            if height[left] <= height[right]:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1

        return volume
