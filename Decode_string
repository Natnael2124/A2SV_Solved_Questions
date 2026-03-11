class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        temp = deque()
        num = deque()

        for i in s:
            if i == "]":
                val = 1
                while stack and stack[-1] != "[":
                    temp.appendleft(stack.pop())
                if stack:
                    stack.pop()
                while stack and stack[-1].isdigit():
                    num.appendleft(stack.pop())
                if num:
                    val = int("".join(num))
                    num.clear()
                if temp:
                    string = "".join(temp)
                    temp.clear()
                    stack.append(val*string)
            else:
                stack.append(i)
        return "".join(stack)
                
              
