import pickle, os, urllib.request as ur

def displayRecord(): #Provide here with the link-
    with ur.urlopen("") as data:
        recd = pickle.load(data)
        return recd
    
recd = displayRecord()
if len(recd.keys()) == 0:
    print("No Flights Are Scheduled! Come Back Later!\n"+"-"*80)
else:
    print("Here Are The Flights Scheduled-\n")
    for i in recd.keys():
        print("-"*80)
        print("Flight No: "+i+"\n")
        for j,k in recd[i].items():
            print(f"{j} {k}")
print("-"*80)   
input("Hit Enter to exit")