from typing import ValuesView

import address
from voter import Voter
from address import AddressParser, Address
import datetime

def check_dob(dob) -> bool:
    if len(dob != 10):
        return False
    dob = dob.split('-', maxsplit = 2)

def get_dob():
    valid_dob = False;
    now = datetime.datetime.now()
    while not valid_dob:
        dob = input('\nEnter DOB (XX-XX-XXXX):\nex: 01-27-1965\n')

        if (len(dob) != 10 or len(dob.split('-', maxsplit = 2)) != 3):
            print('Invalid Date!')
            continue
        dob = dob.split('-', maxsplit = 2)
        try:
            dob = datetime.date(year = int(dob[2]),month = int(dob[0]),day = int(dob[1]))
        except ValueError as e:
            print('Invalid Date!\n{}'.format(e))
            continue
    return dob

def get_address():
    fix = ''
    while fix.lower() != 'yes':
        address = input('Enter Address: ')
        city = input('Enter City: ')
        state = input('Enter State: ')
        zip_code = input('Enter Zip Code: ')
        ap = AddressParser()
        full_address = ap.parse_address('{}, {}, {}, {}'.format(address,city,state,zip_code))
        print('\n-------- Verify Address -------\n{}'.format(full_address))
        fix = input("Type 'yes' to confirm")
    return full_address
               

def pad_string(x: str,length: int):
    while(len(x) < length):
        x += ' '
    return x

def register(min_age = 18,city= 'New Brunswick',state= 'NJ') -> None:
    print('---------Voter Registration---------\n')
    name = input("Enter Name:")
    dob = get_dob()
    age = (datetime.date.today() - dob).days/365
    print(age)
    if age < min_age:
        print("Too Young to Register")
        return 

    address = get_address()
    registered_voter = Voter(name,dob,address)


if __name__ == "__main__":
    register()
