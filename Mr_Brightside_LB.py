import random                                                                                         
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
def is_integer(parameter): 
    '''
    Checks if something is an integer
    Args:
        number (any): parameter to check
    Returns:
        bool: True/False depending on if number is an integer
    Raises:
        ValueError: if number is not an integer
    '''
    try: 
        int(parameter)
        return True
    except ValueError:
        return False 
def get_integers(): 
    '''
    Asks user for 2 numbers 
    Args:
        converts user input into an integer 
    Returns:
        int: a and b as integers 
    '''
    while True: 
        a = input("Enter Number") 
        b = input("Enter Another Number")  
        if is_integer(a) and is_integer(b): 
            return int(a), int(b)
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
def main():
    sing_song()
    add(2, 3)
    print_list(['September', '29', '2003']) 
    Date = ['September', '29', '2003']
    in_list("Records", Date) 
    is_integer("1") 
    a,b = get_integers() 
    get_random(a,b)
    print(count_vowels("Lucas")) 
    
main() 
