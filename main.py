import sys
from time import sleep

#edit this if you want to debug a specific scene
scene = "intro"

def typewriter(text, pace):
    for char in text:
        sleep(pace)
        sys.stdout.write(char)

if scene == "intro":
    typewriter("[intro text]\n\n", 0.2)
    scene = "bouncers"
if scene == "bouncers":
    typewriter("An ankylosaurus blocks your way.\n\n",0.1)
    #ideally this next bit is formatted differently somehow
    typewriter("Ey there, ", 0.1)
    typewriter("chump. ", 0.3)
    typewriter("You got any ID?\n\n", 0.1)
    #nobody wants strings this long in their code.
    chump_reply = input("How do you respond?\n\n(a) Yessiree, right here!\n(b) U-uh, ID? Do you mean, like, a driver's license or something? The UK has no straightforward system of ID cards.\n(c) *You have a fake ID ready on hand.*\n(d) Hey, watch who you're calling a chump!\n")
    if chump_reply == "a" or "A" or "(a)": #is there a more straightforward way of getting it to read the input correctly regardless of its format?
        personality = "confident"
        #does it matter that I have created the variable separately within each if statement?
    elif chump_reply == "b" or "B" or "(b)":
        personality = "nervous"
    elif chump_reply == "c" or "C" or "(c)":
        personality = "confrontational"
    elif chump_reply == "d" or "D" or "(d)":
        personality = "criminal" #is there a more overseeable way of keeping all of your variables (e.g. personality, street cred, money, etc.) in one place?
#the branching + nesting is quickly getting out of hand, especially if there is more interactive dialogue with the bouncers based on previous answers. How to organise this more coherently?


# comment