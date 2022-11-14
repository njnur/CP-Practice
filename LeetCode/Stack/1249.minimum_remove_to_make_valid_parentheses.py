class Solution:
    def min_remove_to_make_valid(self, s: str) -> str:
        if len(s) == 0:
            return ""

        s_arr = list(s)
        temp_stack = []

        for index, elements in enumerate(s_arr):
            if elements == '(':
                temp_stack.append(index)

            if elements == ')':
                if len(temp_stack) > 0:
                    temp_stack.pop()
                else:
                    s_arr[index] = ''

        for elements in temp_stack:
            s_arr[elements] = ''

        return "".join(s_arr)


print(Solution().min_remove_to_make_valid(s="lee(t(c)o)de)"))
print(Solution().min_remove_to_make_valid(s="a)b(c)d"))
print(Solution().min_remove_to_make_valid(s="))(("))
print(Solution().min_remove_to_make_valid(s=""))
