class MyStack(object):

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q1.append(x)


    def pop(self):
        """
        :rtype: int
        """
        
        for i in range(len(self.q1) - 1):
            self.q2.append(self.q1.pop(0))
            
        top_element = self.q1.pop(0)
        
        self.q1 , self.q2 = self.q2 , self.q1
        
        return top_element
        
        

    def top(self):
        """
        :rtype: int
        """
        for i in range(len(self.q1) - 1):
            self.q2.append(self.q1.pop(0))
            
        top_element = self.q1.pop(0)
        
        self.q2.append(top_element)
        
        self.q1 , self.q2 = self.q2 , self.q1
        
        return top_element
        
        

    def empty(self):
        """
        :rtype: bool
        """
        
        return (len(self.q1) == 0)
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()