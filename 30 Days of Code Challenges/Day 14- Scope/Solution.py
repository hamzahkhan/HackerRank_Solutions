def const(self, a):
        self.__elements = a
        
    def computeDifference(self):
        self.__elements = sorted(self.__elements)
        self.maximumDifference = max(self.__elements) - min(self.__elements)
