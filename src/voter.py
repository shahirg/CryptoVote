
class Voter:
    def __init__(self,name: str,dob,address) :
        self.NAME = name
        self.DOB = dob
        self.ADDRESS = address
        
    def __eq__(self, other):
        return (self.NAME == other.NAME and self.DOB == other.DOB 
                and self.ADDRESS == other.ADDRESS)
                
    def __repr__(self) -> str:
        return (f'{self.__class__.__name__}('
                f'{self.NAME!r}, {repr(self.DOB)!r},{repr(self.ADDRESS)!r})')
