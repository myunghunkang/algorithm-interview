from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        menu = 2
        if menu == 1:  # with 'index'
            for i in range(len(nums)):
                for j in range(i+1, len(nums)):
                    if nums[i] + nums[j] == target:
                        return [i, j]

        elif menu == 2:  # with 'index' and 'value', return [current one, one to search to forward]
            for i, val in enumerate(nums):
                complement = target - nums[i]
                if complement in nums[i+1:]:
                    return [i, nums[i+1:].index(complement)+(i+1)]


        elif menu == 3:  # with 'index' and 'value', return [one to search in stack, current one]
            map_nums = {}
            for i, val in enumerate(nums):
                complement = target - nums[i]
                if complement in map_nums:
                    return [map_nums[complement], i]
                else:
                    map_nums[complement] = i
