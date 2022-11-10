class Solution:

    @staticmethod
    def length_of_longest_substring_bruteforce(s: str) -> int:
        max_str_count = 0
        str_count = 0
        substring = ''

        for index, _ in enumerate(s):
            if substring:
                if s[index] in substring:

                    substring = s[index]
                    str_count = 1

                else:
                    substring += s[index]
                    str_count += 1
            else:
                substring += s[index]
                str_count += 1

            if str_count > max_str_count:
                max_str_count = str_count

        return max_str_count

    @staticmethod
    def length_of_longest_substring_two_pointer(s: str) -> int:
        max_str_count = 0

        for index, _ in enumerate(s):
            pass

        return max_str_count


if __name__ == '__main__':
    # ================= BruteForce ================= #
    print(Solution().length_of_longest_substring_bruteforce(s="abcabcbb"))
    print(Solution().length_of_longest_substring_bruteforce(s="bbbbb"))
    print(Solution().length_of_longest_substring_bruteforce(s="pwwkew"))
    print(Solution().length_of_longest_substring_bruteforce(s="  b"))
    print(Solution().length_of_longest_substring_bruteforce(s="dvdf"))
    # ================= Two Pointer ================= #
    # print(Solution().length_of_longest_substring_two_pointer(s="abcabcbb"))
    # print(Solution().length_of_longest_substring_two_pointer(s="bbbbb"))
    # print(Solution().length_of_longest_substring_two_pointer(s="pwwkew"))
    # print(Solution().length_of_longest_substring_two_pointer(s=" "))
