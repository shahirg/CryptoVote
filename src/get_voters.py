import csv
import datetime
from address import Address, AddressParser
from voter import Voter
#will handle reading voters from csv

def get_voter_dict() -> dict:
    voters = {}
    #creates dictionary of voters
    #key = voter_id
    #value = Voter class
    with open('voters.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            voters[row['voterid']] = eval(row['voter'])
    print(voters)
    return voters

def purge_csv():
    with open('voters.csv','w+') as file:
        file.write('voterid,voter\n\n')

actions = {
    '1':lambda:get_voter_dict(),
    '2':lambda:purge_csv(),

}

if __name__ == "__main__":
    while(True):
        action = input('Select Option Number\n1)Get Registered Voters \n2)Purge Registered Voters \n')
        if(action == '5'):
            break
        try:
            x = actions[action]()
        except KeyError:
            continue