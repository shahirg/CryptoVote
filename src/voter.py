from address import Address, AddressParser
import datetime
class Voter:
    def __init__(self,name: str,dob:datetime,address) -> None:
        self.NAME = name
        self.DOB = dob
        self.ADDRESS = address
        
    
    def __repr__(self) -> str:
        return (f'{self.__class__.__name__}('
                f'{self.NAME!r}, {repr(self.DOB)!r},{repr(self.ADDRESS)!r})')
