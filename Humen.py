class Humen:
    
    def __init__(self,Pol):
         self._Pol = Pol 
    def _init2_(self):
        Pol="Women"
        self._Pol = Pol 

        
    def name(self):
        print(self._str_())
    @property
    def Pol(self):
        return self._Pol
    @Pol.setter
    def Pol(self, Pol):
        self._Pol=Pol
    def _str_(self):
        return "Hello, my name is Sasha and i am a {}".format(self.Pol)