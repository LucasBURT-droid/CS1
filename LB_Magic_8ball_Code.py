import random                                                                                   #imports random Response
print("hello human, I am the magic 8 ball!")                                                    #displays the message, “hello human, I am the magic 8 ball!"
responses = ["yes","no","maybe","ask later"]                                                    #creates a list called responses 
question_words = ["will", "how", "which","is","where","who","what","whom","whose","when"]       #creates a list called question_words

while True:                                                                                     #forever loop
    question = str.lower(input("Ask Any Question! "))                                           #sets question to user input, then displays the message
    first_word = question.split()[0]                                                            #sets first_word to the first word of question

    if question == "stop":                                                                      #IF Question equals “stop”:
        break                                                                                   #Ends Code 
    elif "?" in question and first_word in question_words:                                      #Else IF in question and first_word is in question_words:
        print(random.choice(responses))                                                         #displays a random response from responses
    else:                                                                                       #Anything thats not a question 
        print("Sorry that is not a question!")                                                  #displays the message, "Sorry that is not a question!"
    
    


