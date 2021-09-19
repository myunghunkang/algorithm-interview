def main_c4_non_linear_data_structures():
    menu = 1

    if menu == 1:  # 125 https://leetcode.com/problems/number-of-islands/
        in_str = "abc fef cba"

        from c4_non_linear_data_structures.ch12.c32_1 import Solution
        sol = Solution()
        print(sol.numIslands(in_str))


def main_c3_linear_data_structures():
    menu = 2

    if menu == 1:  # 1 https://leetcode.com/problems/two-sum/
        from c3_linear_data_structures.ch07.c7_1 import Solution
        nums = [9,2,7,11,15]
        target = 9
        sol = Solution()
        print(sol.twoSum(nums,target))

    if menu == 2:  # 15 https://leetcode.com/problems/trapping-rain-water/
        from c3_linear_data_structures.ch07.c8_2 import Solution
        heights = [0,1,0,2,1,0,1,3,2,1,2,1]
        sol = Solution()
        print(sol.trap(heights))


    if menu == 3:  # 15 https://leetcode.com/problems/3sum/
        from c3_linear_data_structures.ch07.c9_1 import Solution
        nums = [-1,0,1,2,-1,-4]
        sol = Solution()
        print(sol.threeSum(nums))

def main_c2_python():
    menu = 8

    if menu == 1:  # 125 https://leetcode.com/problems/valid-palindrome/
        in_str = "abc fef cba"

        from c2_python.ch06.c1_1 import Solution
        sol = Solution()
        print(sol.isPalindrome(in_str))

        from c2_python.ch06.c1_2 import Solution
        sol = Solution()
        print(sol.isPalindrome(in_str))

        from c2_python.ch06.c1_3 import Solution
        sol = Solution()
        print(sol.isPalindrome(in_str))

    if menu == 2:  # 344 https://leetcode.com/problems/reverse-string/
        in_list = ["abc", "fef", "cba"]

        from c2_python.ch06.c2_1 import Solution
        sol = Solution()
        print(sol.reverseString(in_list))

        from c2_python.ch06.c2_2 import Solution
        sol = Solution()
        print(sol.reverseString(in_list))

    if menu == 3:  # 937 https://leetcode.com/problems/reorder-data-in-log-files/
        logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]

        from c2_python.ch06.c3_1 import Solution
        sol = Solution()
        print(sol.reorderLogFiles(logs))

    if menu == 4:  # 819 https://leetcode.com/problems/most-common-word/
        paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
        banned = ["hit", "wa"]

        from c2_python.ch06.c4_1 import Solution
        sol = Solution()
        print(sol.mostCommonWord(paragraph, banned))


    if menu == 5:  # 49 https://leetcode.com/problems/group-anagrams/
        strs = ["eat","tea","tan","ate","nat","bat"]

        from c2_python.ch06.c5_1 import Solution
        sol = Solution()
        print(sol.groupAnagrams(strs))

    if menu == 6:  # 5 https://leetcode.com/problems/longest-palindromic-substring/
        paragraph = "Bob hit a llall a hit Bob"

        from c2_python.ch06.c6_1 import Solution
        sol = Solution()
        print(sol.longestPalindrome(paragraph))


    if menu == 7:  # 1 https://leetcode.com/problems/two-sum/
        nums = [1,10,6,7,18,5,2]
        target = 9

        from c3_linear_data_structures.ch07.c7_0 import Solution
        sol = Solution()
        print(sol.twoSum(nums, target))

    if menu == 8:  # 42. Trapping Rain Water https://leetcode.com/problems/trapping-rain-water/
        height = [0,1,0,2,1,0,1,3,2,1,2,1]

        from c3_linear_data_structures.ch07.c8_0 import Solution
        sol = Solution()
        print(sol.trap(height))

    if menu == 9:  # 15 https://leetcode.com/problems/3sum/
        nums = [-1,0,1,2,-1,-4]

        from c3_linear_data_structures.ch07.c9_1 import Solution
        sol = Solution()
        print(sol.threeSum(nums))


if __name__ == '__main__':
    main_c3_linear_data_structures()
    # main_c2_python()