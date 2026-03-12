class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        # def add(num1, num2):
        #     return num1+num2
        
        # def sub(num1, num2):
        #     return num1-num2

        # def dev(num1, num2):
        #     return num1/num2
        
        # def mul(num1, num2):
        #     return num1*num2
        
        op = {
            "+": lambda a,b: a+b,
            "-":lambda a,b: a-b,
            "*":lambda a,b: a*b,
            "/":lambda a,b: int(a/b)}

        stack = []
        for i in tokens:
            if i in op:
                b = stack.pop()
                a= stack.pop()
                new_num = op[i](a,b)
                stack.append(new_num)
            else:
                stack.append(int(i))

        return stack[0]
            
s = Solution()

print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))