class Postfix:
    def __init__(self):
        self.stack=[]
        
    def evaluate(self,expression):
        tokens=expression.split()
        for token in tokens:
            if self.is_integer(token):
                self.stack.append(int(token))
            else:
                operand2 = self.stack.pop()
                operand1=self.stack.pop()
                result=self.perform_operation(token,operand1,operand2)
                self.stack.append(result)
        return self.stack.pop()
            
    def perform_operation(self,operator,operand1,operand2):
        if operator =='+':
            return operand1 + operand2
        elif operator =='-':
            return operand1 -operand2
        elif operator =='*':
            return operand1 * operand2
        elif operator =='/':
            return int(operand1/operand2)
    
    def is_integer(self,token):
        try:
            int(token)
            return True
        except ValueError:
            return False
     
def main():        
    postfix_expression=input("Enter the string:")
    evaluator =Postfix()
    result=evaluator.evaluate(postfix_expression)
    print("Result:",result)
        
if __name__=="__main__":
    main()
    
    
    
    
    
    
    
    
    
    
    
    

    