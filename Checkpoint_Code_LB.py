import random 
musicians = ["Baby Kia", "King Von", "TayK"] 
instruments = ["Vocals", "Piano", "Drums"] 
print(musicians)

#first for loop to iterate through the elements of instruments and print each
for instrument in instruments:
    print(instrument) 

#second for loop to iterate through the indexes in the musicians list and print the pair at every index for both musicians and instruments
for i in range(len(musicians)): 
    print(musicians[i], instruments[i]) 
