class Portfolio:
    def __init__(self,b={}):
        self.__balance = b.copy()
        
    def getBalance(self,sym):
        if sym not in self.__balance:
            return 0
        return self.__balance[sym]
    
    def invest(self,sym,qty):
        if qty<0:
            raise ValueError('Negative amounts not permitted')
        self.__balance[sym]= self.getBalance(sym)+qty
    
    def divest(self,sym,qty):
        if qty<0:
            raise ValueError('Negative amounts not permitted')
        if self.getBalance(sym)<qty:
            raise ValueError('Insufficient Funds')
        self.__balance[sym]= self.getBalance(sym)-qty
    
