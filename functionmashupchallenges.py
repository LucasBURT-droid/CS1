import random                                                                                         

'''
FLOWER POT: 
Title: Function Extra Challanges 
Author: Lucas Burt  
Date: 5.1.25
Bugs: 0 
Functions:  
- Singing a song
- Math operations
- List operations
- String manipulations
- Random number generation

'''

def chorus(): 
    '''
    Prints the chorus of a song
    Args:
        None
    Returns:
        print: chorus
    '''    
    print('''                                                                                         
Chest now
He takes off her dress now
Let me go
And I just can't look, it's killing me
They're taking control

Jealousy
Turning saints into the sea
Swimming through sick lullabies
Choking on your alibi
But it's just the price I pay
Destiny is calling me
Open up my eager eyes
'Cause I'm Mr. Brightside
    ''')
def sing_song():      
    '''
    Prints an entire song
    Args:
        None
    Returns:
        print: song  
    '''                                                                                   #
    print('''
Comin' out of my cage and I've been doin' just fine
Gotta, gotta be down because I want it all
It started out with a kiss, how did it end up like this?
It was only a kiss, it was only a kiss
Now I'm falling asleep and she's calling a cab
While he's having a smoke and she's taking a drag
Now they're goin' to bed and my stomach is sick
And it's all in my head, but she's touching his
''')
    chorus()                                                                                           #
    print('''
I'm comin' out of my cage and I've been doin' just fine
Gotta, gotta be down because I want it all
It started out with a kiss, how did it end up like this?
(It was only a kiss) It was only a kiss
Now I'm falling asleep and she's calling a cab
While he's havin' a smoke and she's taking a drag
Now they're goin' to bed and my stomach is sick
And it's all in my head, but she's touching his
    ''')
    chorus()
    print('''
I never
I never
I never
I never
    ''')
def add(a, b):
    '''
    Takes two numbers and adds them together
    Args:
        a (int): first number
        b (int): second number
    Returns:
        print: sum of a and b
    '''
    print(a + b)
def print_list(array):
    '''
    Takes a list and prints every element
    Args:
        takes in array (list): list to be printed
    Returns:
        print: printing every element in list 
    '''
    for element in array: 
        print(element)
def in_list(element,array):
    '''
    Takes an element and checks if it is in a given list
    Args:
        element (any): item you are looking for in the list
        array (list): the given list
    Returns:
        bool: True/False depending on whether the element is in the array
    '''
    return element in array
def get_integer(): 
    '''
    Checks if something is an integer
    Args:
        number (any): parameter to check
    Returns:
        bool: True/False depending on if number is an integer
    Raises:
        ValueError: if number is not an integer
    '''
    while True:
        try: 
            a = int(input("Enter Number"))
            return a
        except ValueError:
            print('Not a number') 
def get_integers(): 
    '''
    Asks user for 2 numbers 
    Args:
        converts user input into an integer 
    Returns:
        int: a and b as integers 
    '''
    a = get_integer()
    b = get_integer()
    return a, b
def get_random(): 
    '''
    prints a random number between the two given integers. 
    Args:
        none
    Returns:
        print: random integer between given integers
    '''
    a, b = get_integers()
    print(random.randint(a,b))

def count_vowels(string):  
    '''
    Takes a string and returns the number of vowels in it 
    Args:
        string (str): given word or phrase
    Returns:
        int: total count of vowels
    '''
    count = 0 
    for character in string:
        if character in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            count += 1 
    return count  

def reverse_string(string):
    return string[::-1]
'''
 Takes a string and reverses it
    Args:
        string (str): given word or phrase
    Returns:
        int: reversed string
'''
def is_palindrome(string):
    return string == reverse_string(string)
'''
 Takes user input and checks if palindrome
    Args:
       
    Returns:
        true/false palindrome 
'''
def get_initials(fullname):
    names = fullname.split(' ')
    initials = ''
    for name in names:
        initials += name[0]
    return initials

'''
takes in name  
    Args; 

Returns: 
    First inital in given name

'''
def main():
    while True:
        option = input('What would you like to do? (Press "q" to quit) 1. Sing a song, 2. Add, 3. Print a list, 4. Check if something is in a list.... 5. What is a random number between the two given integers 6. Enter word or phrase to count vowels 7. Enter string to reverse it 8. Enter string to check if its a palendrome 9. Enter your full name to recive your first inital     ')

        if option.lower() == 'q':
            break 
        elif option == '1':
            sing_song()
        elif option == '2':
            a, b = get_integers()
            add(a, b)
        elif option == '3':
            user_list = input('Enter a list, separate each item with a space ').split(' ')
            print_list(user_list) 
        elif option == '4':
            user_list = input('Enter a list, separate each item with a space ').split(' ')
            check = input('Enter thing to check: ')
            print(in_list(check, user_list))
        elif option == '5':
            get_random()
        elif option == '6':
            string = input('Enter word or phrase: ')
            print(count_vowels(string)) 
        elif option == '7':
            string = input('Enter string to reverse: ')
            print(reverse_string(string))
        elif option == '8':
            string = input('Enter string to check: ')
            print(is_palindrome(string))
        elif option == '9':
            fullname = input('Enter your full name: ')
            print(get_initials(fullname))
        else:
            print('Invalid')
main() 
