class calculator:
    def cal(self,a,b,op):
        if op == "+" or op == "add":
            return a+b
        elif op == "-" or op == "subtract":
            return a-b
        elif op == "*" or op == "multiply":
            return a*b
        elif op == "/" or op == "divide":
            if b==0:
                return "zero division error"
            return a/b
        else:
            return "Invalid Operation"
a = float(input("Enter the first number: ")) 
b = float(input("Enter the second number: "))
op = input("Enter the desired Operation: ")
cal1 = calculator()
print(cal1.cal(a,b,op))