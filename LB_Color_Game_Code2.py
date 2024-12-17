import random                                                                                                           #random choice is imported 

def print_colored_text(text, color_name):                                                                               # prints given text in a color 
    color_codes = {                                                                                                     # color dictonary/list variable   
        'black': '\033[0;30m',                                                                                          # Black 
        'red': '\033[0;31m',                                                                                            # Red 
        'yellow':'\033[0;33m',                                                                                          # yellow 
        'cyan': '\033[0;36m',                                                                                           # Cyan 
        'green': '\033[0;32m',                                                                                          # Green 
        'blue': '\033[0;34m',                                                                                           # Blue 
        'white': '\033[0;37m',                                                                                          # White 
        'magenta': '\033[0;35m',                                                                                        # Magenta 
        'reset': '\033[0;37m',                                                                                          # Resets text color 
    }

    print(color_codes.get(color_name) + text + color_codes.get('reset'))                                                # prints given text in a color              

name = input('What is your name?')                                                                                      # Asks user name                                             
print('hello', name)                                                                                                    # prints name in color 
correct = 0                                                                                                             # Variable for Colors guessed correctly 
rounds = 0                                                                                                              # Variable for Number of rounds played 
colors = ['black', 'red', 'yellow','magenta','white','black','green','cyan']                                            # list of colors 

while True:                                                                                                             # forever loop                                                                    
    text_color = random.choice(colors)                                                                                  # Text Color is randomized 
    print_color = random.choice(colors)                                                                                 # Color printed is randomized 
    print_colored_text(text_color, print_color)                                                                         # prints text color + print color 

    user_color = input('Quick! Enter the color of the text: ').lower()                                                  # Print Message, "Quick! Enter the color of the text"

    if user_color == print_color:                                                                                       # User guess = Print Color 
        print('Right!')                                                                                                 # prints message, "Right!"
        correct += 1                                                                                                    # Adds +1 to score 
    else:                                                                                                               # User guess X Print Color 
        print('Wrong!')                                                                                                 # prints message, "Wrong!"                                                  
    rounds += 1                                                                                                         # adds +1  to rounds 

    while True:                                                                                                         # forever loop 
        play = input (f'You have gotten {correct} out of {rounds} right. Would you like to play again? y/n: ')          # Asks User if they want to play again 

        if play == 'y':                                                                                                 # User wants to play again 
            break                                                                                                       # End Code 
        elif play == 'n':                                                                                               # User does not want to play again 
            exit()                                                                                                      # leave code
        else:                                                                                                           # User has another input 
            print('Invalid')                                                                                            # print message, Invalid 
