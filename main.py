def main():
    menu = 7

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
        nums = [1,7,2,15]
        target = 9

        from c3_linear_data_structures.ch07.c7_1 import Solution
        sol = Solution()
        print(sol.twoSum(nums, target))



if __name__ == '__main__':
    main()