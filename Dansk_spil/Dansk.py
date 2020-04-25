import random 

f = open("tekst.txt", "r")
vokaler = ["a","e","i","o","u","y"]

tekst=[]

for i in f:
    tekst += i.split()
while True:
    chosen = tekst[int(random.uniform(0,len(tekst)))]

    chosen_p=""

    for i in chosen:
        if i in vokaler:
            chosen_p+="_"
        else:
            chosen_p += i
            
    print(chosen_p)
    guess =input()
    if guess == chosen:
        print("you guess right")
            
        