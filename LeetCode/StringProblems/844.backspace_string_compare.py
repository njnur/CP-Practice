class Solution:

    @staticmethod
    def create_array_without_backspace_bruteforce(chars: str) -> list:
        final_arr = []
        for _index in range(0, len(chars)):
            if chars[_index] == '#':
                if final_arr:
                    final_arr.pop()
            else:
                final_arr.append(chars[_index])

        return final_arr

    def backspace_compare_bruteforce(self, s: str, t: str) -> bool:
        """
        Brute force method to solve the Backspace Compare problem.
        Time Complexity: O(n)
        Space Complexity: O(n)

        :param s: string
        :param t: string
        :return: bool
        """
        s_arr = self.create_array_without_backspace_bruteforce(chars=s)
        t_arr = self.create_array_without_backspace_bruteforce(chars=t)

        if len(s_arr) != len(t_arr):
            return False
        else:
            if len(s_arr) == 0:
                return True

            for _index in range(0, len(s_arr)):
                if s_arr[_index] != t_arr[_index]:
                    return False
                return True

    @staticmethod
    def backspace_compare_two_pointer(s: str, t: str) -> bool:
        s_last_index = len(s) - 1
        t_last_index = len(t) - 1
        s_skip = 0

        while s_last_index >= 0 or t_last_index >= 0:
            if s[s_last_index] == '#' or t[t_last_index] == '#':
                if s[s_last_index] == '#':
                    s_skip += 1



        return True


if __name__ == '__main__':
    print("====BruteForce Method====")
    print(Solution().backspace_compare_bruteforce(s="ab#c", t="ad#c"))
    print(Solution().backspace_compare_bruteforce(s="ab##", t="c#d#"))
    print(Solution().backspace_compare_bruteforce(s="a#c", t="b"))
    print(Solution().backspace_compare_bruteforce(s="a##c", t="#a#c"))
