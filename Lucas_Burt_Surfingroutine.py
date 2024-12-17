import time
                                                       
print("Go to the beach!")                                               #displays the message "Go to the Beach!"
                                                              
while True:                                                              #forever loop                             
    Check_waves = str.lower(input("Size <3meters y/n: "))               #stores user response in variable Check_Waves and converts to lowercase               
    if Check_waves == "y":                                               #if the user y
        print("Put on Wetsuit")                                         #displays the message "Put on Wetsuit"                                        
        break                                                            #end code 
    elif Check_waves == "n":                                             #if the user n 
        print("Wait for Swell")                                         #displays the message "Wait for Swell"
        time.sleep(3)                                                    #waits 3 seconds 
        break                                                            #end code 
    else:                                                                #if user responds with another variable 
        print("Invalid Response")                                       #display message "Invalid Response"
while True:                                                              #forever loop
    Get_in_Water = input("Water Temp Freezing? y/n: ").lower()          #stores user response in variable Get_in_Water and converts to lowercase  
    if Get_in_Water == "y":                                              #if the user y          
        print("Get Thicker Wetsuit!")                                   #displays the message "Get Thicker Wetsuit!"
        time.sleep(3)                                                    #waits 3 seconds  
        break                                                            #end code 
    elif Get_in_Water == "n":                                            #if the user n 
        print("Go Surf!")                                               #displays the message "Go Surf"
        break                                                            #end code
    else:                                                                #if the user responds with anoter variable 
        print("invalid Response")                                       #displays the message "Invalid Response" 
while True:                                                              #forever loop 
    Surfboard_wax = input("Surfboard has wax? y/n: ").lower()           #stores user response in variable Surfboard_wax
    if Surfboard_wax == "y":                                             #if user y  
        print("Continue Surfing")                                       #displays the message "Continue Surfing"
        break                                                            #end code
    elif Surfboard_wax == "n":                                           #if user n
        print("Go Grab Some Wax!")                                      #displays the message "Go Grab Some Wax!"
        time.sleep(3)                                                    #waits 3 seconds 
        break                                                            #ends code 
    else:                                                                #if user responds with another variable 
        print("Invalid Response")                                       #displays the message "Invalid Response" 
while True:                                                              #forever loop
    Surfboard_Fins = input(" Are Fins in Surfboard? y/n: ").lower()     #ends code
    if Surfboard_Fins == "y":                                            #Input  = y
        print("Good Job! You Came Perpared.")                           #displays the message "Good Job! You Came Prepared"
        break                                                            #ends code
    elif Surfboard_Fins == "n":                                          #Input = n 
        print("Go back to beach!")                                      #displays the message "Go back to beach!"      
        break                                                            #ends code
    else:                                                                #any other input than y or n
        print("Invalid Response")                                       #displays the message "Invalid Response"
while True:                                                              #forever loop
    Surfing_Mood = input("How Did You Surf? Good/Bad: ").lower()        #stores user response in varibable Surfing_Mood
    if Surfing_Mood == "good":                                           #if variable = good 
        print("Awesome Sauce!!!")                                       #displays the message "Awesome Sauce!!!"
        break                                                            #ends code 
    elif Surfing_Mood == "bad":                                          #if variable = bad
        print(":(")                                                     #displays the message :(
        break                                                            #ends code
    else:                                                                #if variable = anything else  
        print("Invalid Response")                                       #displays the message, "Invalid Response"

    

                            
    
    
    
    
