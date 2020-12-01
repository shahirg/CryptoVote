
from voter import Voter
from address import AddressParser, Address
import datetime
import csv


def get_dob():
    valid_dob = False;
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
        fix = input("Type 'yes' to confirm: ")
    return full_address
               

def pad_string(x: str,length: int) ->str:
    while(len(x) < length):
        x += ' '
    return x

def register(min_age = 18,city= 'New Brunswick',state= 'NJ') -> None:
    print('---------Voter Registration---------\n')
    
    first_name = input("Enter First Name: ").upper()
    last_name = input("Enter Last Name: ").upper()
    dob = get_dob()
    age = (datetime.date.today() - dob).days/365
    print(age)
    if age < min_age:
        print("Too Young to Register")
        return 

    address = get_address()
    #FOR now voter id will just be a numbering system
    with open('voterid.txt','r') as file:
        voter_id = int(file.readline())
    voter_id += 1
    with open('voterid.txt','w') as file:
        file.write(str(voter_id))
        
    registered_voter = Voter(voter_id,first_name,last_name,dob,address)

    with open('voters.csv','a') as file:
        writer = csv.writer(file, delimiter = ',')
        writer.writerow([str(voter_id),repr(registered_voter)])


if __name__ == "__main__":
    register()
