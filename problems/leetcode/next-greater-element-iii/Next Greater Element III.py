class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits, stack, nge = [i for i in str(n)], [], n
        for i in range(len(digits)-1, -1, -1):
            if stack and stack[-1] > digits[i]:
                j = 0
                while stack[j] <= digits[i]:
                    digits[i+j+1] = stack[j]
                    j += 1
                digits[i], stack[j] = stack[j], digits[i]
                for j in range(j, len(stack)):
                    digits[i+j+1] = stack[j]
                stack, nge = [], int("".join(digits))
                break
            stack.append(digits[i])
            
        
        return nge if nge < 2**31 and nge > n else -1