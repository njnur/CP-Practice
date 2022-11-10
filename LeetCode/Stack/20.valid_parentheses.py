class Solution:
    def is_valid(self, s: str) -> bool:
        stack_list = []

        for strs in s:
            if strs == '(' or strs == '{' or strs == '[':
                stack_list.append(strs)
            else:
                if stack_list:
                    if (stack_list[-1] == '(' and strs == ')') or (stack_list[-1] == '{' and strs == '}') or \
                            (stack_list[-1] == '[' and strs == ']'):
                        stack_list.pop()
                    else:
                        stack_list.append(strs)
                else:
                    stack_list.append(strs)

        if stack_list:
            return False
        return True


if __name__ == '__main__':
    print(Solution().is_valid(s="()"))
    print(Solution().is_valid(s="()[]{}"))
    print(Solution().is_valid(s="(]"))
    print(Solution().is_valid(s="]"))
    print(Solution().is_valid(s="(])"))
    print(Solution().is_valid(s="[])"))
