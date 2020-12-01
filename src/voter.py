import datetime
from address import Address, AddressParser

class Voter:
    def __init__(self,voter_id,first_name,last_name,dob,address) :
        self.VOTER_ID = voter_id #voter id need to still be decided
        self.FIRST_NAME = first_name
        self.LAST_NAME = last_name
        self.DOB = dob
        self.ADDRESS = address
        
    def __eq__(self, other):
        return (self.VOTER_ID == other.VOTER_ID and self.FISRT_NAME == other.FIRST_NAME 
                and self.LAST_NAME == other.LAST_NAME and self.DOB == other.DOB 
                and self.ADDRESS == other.ADDRESS)
                
    def __repr__(self) -> str:
        return (f'{self.__class__.__name__}('
                f'{self.VOTER_ID!r},{self.FIRST_NAME!r}, {self.LAST_NAME!r},{repr(self.DOB)!r},{repr(self.ADDRESS)!r})')
