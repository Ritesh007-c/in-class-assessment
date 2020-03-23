class Portfolio:
    def __init__(self,b={}):
        self.__balance = b.copy()
        
    def getBalance(self,sym):
        if sym not in self.__balance:
            return 0
        return self.__balance[sym]
    
    def invest(self,sym,qty):
        self.__balance[sym]= self.getBalance(sym)+qty
    
