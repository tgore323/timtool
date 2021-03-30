from gtts import gTTS # import Google's TTS
import os # for file system access
from time import sleep # for delaying program output
import glob
import pyfiglet
import requests
import json

# Display banner once
ascii_banner = pyfiglet.figlet_format("TimTool")
print(' ')
print('Welcome to ....')
print(ascii_banner)
print(' ')
print(50 * '=')
print('TimTool v1 by Tim Gore, KE6QBV')
print(50 * '=')
print(' ')

# main menu
def print_menu():   
    print('[1] Radio ID query')
    print('[2] Create channel announcement files')
    print('[3] View the help file')
    print('[4] Exit TimTool\n')


print_menu()
choice = input('Please enter your selection [1-4]: ')




# radio id menu
def radioid_menu():
    ''' Prints the actual menu '''
    print(' ')
    print('1. Search for user by callsign')
    print('2. Search for user by radio ID')
    print('3. Search for user by surname')
    print('4. Return to the main menu')
    print('5. Exit from this program')
    print(' ')



loop = True
int_choice = -1

# radio id
while loop:
    radioid_menu()
    id_choice = input('Please enter your selection [1-5]: ')
    if id_choice == '1':
        int_choice = 1
        # loop = False
        callsign = input('\nPlease enter desired callsign: ')
        callsign = callsign.upper()
        try:
            url = requests.get('https://database.radioid.net/api/dmr/user/?callsign='+callsign)
            data = json.loads(url.text)
            print('\nThe following ID(s) are registered to '+callsign+' : \n')
            for record in data['results']:
                print(record['fname'], record['surname'], record['callsign'], record['id'], record['remarks'])
            input('\nPress ENTER to return to the main menu.')
        except:
            print('\nSorry, no results for '+callsign)
            input('\nPress ENTER to return to the main menu.')
    elif id_choice == '2':
        int_choice = 2
        #loop = False
        radioid = input('\nPlease enter the desired ID: ')
        try:
            url = requests.get('https://database.radioid.net/api/dmr/user/?id='+radioid)
            data = json.loads(url.text)
            print('\nThe following user is registered to ID '+radioid+' : \n')
            for record in data['results']:
                print(record['fname'], record['surname'], record['callsign'], record['id'], record['remarks'])
            input('\nPress ENTER to return to the main menu.')
        except:
            print('\nSorry, no results for '+radioid+'')
            input('\nPress ENTER to return to the main menu.')
    elif id_choice == '3':
        int_choice = 3
        # loop = False
        surname = input('Please enter the desired user\'s surname: ')
        try:
            url = requests.get('https://database.radioid.net/api/dmr/user/?surname='+surname)
            data = json.loads(url.text)
            print('\nThe following surname is registered to '+surname+' : ')
            for record in data['results']:
                print(record['fname'], record['surname'], record['callsign'], record['id'], record['remarks'])
            input('\nPress ENTER to return to the main menu.')
        except:
            print('\nSorry, no results for '+surname)
            input('\nPress ENTER to return to the main menu.')
    elif id_choice == '4':
        int_choice = 4
        print('Returning to main menu...')
        loop = True
    elif id_choice == '5':
        int_choice = -1
        print('\nExiting program...\n')
        loop = False
    else:
        input('Invalid menu selection. Press ENTER to go back... ')
