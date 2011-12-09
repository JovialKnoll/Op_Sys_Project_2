#Brett Kaplan and Jeff Johnston

import string
import itertools
from random import randint
import sys

#displays the memory with 80 characters to a line
def display_memory(main_mem):
    for i in range(30):
        print(''.join(map(str, main_mem[i*80:i*80+80])))



#main function
def main():
    
    #all valid letters for processes to have
    #call next(letters) to pull the next availible letter
    letters=itertools.cycle(string.ascii_uppercase+string.ascii_lowercase)
    
    
    #checks for proper usage
    if len(sys.argv) != 4 or (sys.argv[1] != "first" and sys.argv[1] != "best" and sys.argv[1] != "next" and sys.argv[1] != "worst"):
        print("USAGE: memsim.py { noncontiguous | first | best | next | worst } <process-termination-probability> <new-process-probability>")
    
    #initializes memory
    main_mem = list(itertools.repeat("#",80))
    for j in range(20):
        letter=next(letters)
        for k in range(randint(10,100)):
            main_mem.append(letter)
    main_mem += ['.' for i in range(2400-len(main_mem))]
    
    display_memory(main_mem)
    
    
    #main loop
    while(True):
        user_input = input("Type c and hit ENTER to continue. ")
        if user_input == 'q':
            return
        elif user_input == 'c':
            letter=next(letters)
            while letter in main_mem:
                letter=next(letters)
            toplace=randint(10,100)
            worked=switch(main_mem,letter,toplace)
            if not worked:
                defrag(main_mem)
                worked=switch(main_mem,letter,toplace)
                if not worked:
                    print("out of memory")
                    sys.exit()
        
        display_memory(main_mem)   

def switch(main_mem,letter,toplace):
    return {
        "noncontiguous": lambda x:noncontiguous_place(main_mem,letter,toplace),
        "first": lambda x:first_place(main_mem,letter,toplace),
        "best": lambda x:best_place(main_mem,lette,toplacer),
        "next": lambda x:next_place(main_mem,letter,toplace),
        "worst": lambda x:worst_place(main_mem,letter,toplace)
    }[sys.argv[1]](-1)

#these functions are for placing letter into appropriate place in main_mem
def noncontiguous_place(main_mem,letter,toplace):
    for i in range(80,len(main_mem)):
        if main_mem[i]==".":
            main_mem[i]=letter
            toplace-=1
        if toplace==0:
            return 1
    return 0
    
def first_place(main_mem,letter,toplace):
    print("first")
    return 1
    
def best_place(main_mem,letter,toplace):
    print("best")
    return 1
    
def next_place(main_mem,letter,toplace):
    print("next")
    return 1
    
def worst_place(main_mem,letter,toplace):
    print("worst")
    return 1
    

#defragments, but keeps the OS where it belongs
def defrag(main_mem):
    nonsys=main_mem[80:]
    nonsys.sort()
    return list(itertools.repeat("#",80))+nonsys

main()
