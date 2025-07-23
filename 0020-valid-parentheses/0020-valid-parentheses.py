class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]

        for char in s:
            if char in ['(','{','[']:
                stack.append(char)

            else:
                if not stack:
                    return False

                if char == ')' and stack.pop()!='(':
                    return False
                elif char == '}' and stack.pop()!='{':
                    return False
                elif char == ']' and stack.pop()!='[':
                    return False


        return len(stack)==0