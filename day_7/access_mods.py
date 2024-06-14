class Super:

    #public data member
    var1 = None

    #protected data member
    _var2 = None

    #private data member
    __var3 = None

    #constructor
    def __init__(self, var1, _var2, __var3):
        self.var1 = var1
        self._var2 = _var2
        self.__var3 = __var3

    #public member function
    def displayPublicMembers(self):
        print("Public Data Member: ", self.var1)

    def _displayProtectedMembers(self):
        print("Protected Data Member", self._var2)

    def __displayPrivateMembers(self):
        print("Private Data Member", self.__var3)
    

class Sub(Super):
    def __init__(self, var1, var2, var3):
        Super.__init__(self, var1, var2, var3)

    def accessProtectedMembers(self):
        self._displayProtectedMembers()

    
obg = Sub("Hello", "all", "people")
obg.accessProtectedMembers()
obg.displayPublicMembers()
# obg.__displayPrivateMembers() will throw an error

print("Object is accessing protected data member: ",obg._var2)