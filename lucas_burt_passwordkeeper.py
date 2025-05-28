import random  
import os
import time
import csv 
import secrets
import string

def enter_password():
    '''
    DOCUMENT
    '''
    master_password = input('Enter password: ')
    time.sleep(1)
    os.system('cls')
    return master_password 

def logged(master_password, tries):
    '''
    DOCUMENT
    '''
    for i in range(tries):
        password = input ("Enter Password: ")

        if password == master_password:
            print("Login successful!")
            return True
        print(f'Incorrect password. You have {tries - i - 1} tries remaining')
    return False

def get_password_length():
    '''
    DOCUMENT
    '''
    while True:
        try:
            length = int(input('Enter a desired password length: ')) #prompt user to enter a desired password length and convert to an integer
            return length
        except ValueError:
            print('Not an integer!')
def generate_password():
    '''
    DOCUMENT
    '''
    length = get_password_length() 
    charaters = list("qwertyuiopasdfghjklzxcvbnm!!@#$%^&*?:|\}{+_-~()1234567890ABCDEFGHIJKLMNOPQRSTUZWXYZ")
    return ''.join(random.sample(charaters, length))
def add_entry(websites, usernames, passwords):
    '''
    Adds an entry to the parallel array of websites, usernames, and passwords
    Args:
        websites (list): the list of websites
        usernames (list): the list of usernames
        passwords (list): the list of passwords
    Returns:
        parallel array: newly added to array of websites, usernames, and passwords
    '''
    website = input("Enter a website: ")
    username = input(f"Enter your username for {website} ")
    password = input(f"Enter your password for {website} (Press 'g' to generate) ")

    if password.lower()  == "g":
        password = generate_password()
    websites.append(website)
    usernames.append(username)
    passwords.append(password)

def print_entry(website, username, password):  
    '''
    Prints an entry given a website username and password
    Args:
        website (str): given website
        username (str): given username
        password (str): given password
    Returns:
        print: f'string with entry data
    '''
    print(f"Website: {website}, Username:{username}, Password: {password}")
   
def get_index(websites):
    '''
    Gets the index of a given website in websites
    Args:
        websites (list): given website list
    Returns:
        int: index of website in websites
    '''
    while True:
        website = input("Enter a website: ")
        
        if website in websites: 
            return websites.index(website)
        else:
            print("That website is not in the list")

def change_entry(websites, usernames, passwords):
    index = get_index(websites)
    websites[index] = input('Enter new website: ')
    usernames[index] = input('Enter new username: ')
    passwords[index] = input('Enter new password: ')

def export_to_csv(filename, headers, *arrays):
    '''
    Exports parallel arrays to a CSV file.

    Args:
        filename (str): The name of the CSV file to create.
        headers (list): A list of header names for each column.
        *arrays: Variable number of array arguments (lists or tuples).
               All arrays must have the same length.
    '''
    if not arrays:
        raise ValueError("At least one array must be provided.")
    
    num_rows = len(arrays[0])

    for arr in arrays:
        if len(arr) != num_rows:
            raise ValueError("All arrays must have the same length.")
    
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(headers)

        for i in range(num_rows):
            row = [arr[i] for arr in arrays]
            csvwriter.writerow(row) 

def password_strength(password):
    '''
    DOCUMENT
    '''
    security = ""
    if len(password) < 8:
        security += "Weak: Password too short, please enter 8 charaters\n"
    if not any(char.islower() for char in password):
        security += "Weak: Missing lowercase letter\n"
    if not any(char.isupper() for char in password):
        security += "Weak: Missing uppercase letter\n"
    if security == any(char.isdigit() for char in password):
        security += "Weak: Missing digit\n"
    
    if len(security) == 0:
        print("Strong password")
    else:
        print(security)

def main():
    websites = [] 
    usernames = []  
    passwords = [] 

    master_password = enter_password()

    while True:
        add_entry(websites, usernames, passwords) 
        stop = input('Enter q to stop: ').lower()

        if stop == 'q':
            break
    os.system('cls')

    if not logged(master_password, 3):
        print('Password did not match! You are banned... Exiting now...')
        exit()

    os.system('cls')
 
    while True: 
        option = input ('''What would you like to do “q” for quit
1. Add an entry
2. print an entry
3. Print all entries
4. Change an entry
5. Store the list of websites with usernames and passwords 
6. Generate a secure password for user
        ''').lower()

        if option == "q":
            break 
        elif option == "1": 
            add_entry(websites, usernames, passwords) 
        elif option == "2": 
            index = get_index(websites)
            print_entry(websites[index], usernames[index], websites[index]) 
        elif option == "3": 
            for i in range(len(websites)): 
                print_entry(websites[i], usernames[i], passwords[i])
        elif option == "4":
            change_entry(websites, usernames, passwords)
        elif option == "5":
            filename = input('Enter your file name: ')
            export_to_csv(filename + ".csv", ["Website", "Username", "Password"], websites, usernames, passwords) 
            print(f'Data successfully exported to {filename}.csv')
        elif option == "6": 
            print(f'The generated password is: {generate_password()}')
        else: 
            print('invalid --> answer the question!')
main () 
