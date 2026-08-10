class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in "+-/*":
                operand2 = int(stack.pop())
                operand1 = int(stack.pop())
                if t == "+":
                    res = operand1 + operand2
                if t == "-":
                    res = operand1 - operand2
                if t == "*":
                    res = operand1 * operand2
                if t == "/":
                    res = operand1 / operand2
                stack.append(res)
            else:
                stack.append(int(t))
        print(stack)
        return int(stack[0])



        
        