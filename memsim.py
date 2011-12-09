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
    if len(sys.argv) != 4:
        print("USAGE: memsim.py { noncontiguous | first | best | next | worst } <process-termination-probability> <new-process-probability>")
        return
    
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
            {
                
                "noncontiguous": lambda x:noncontiguous_place(main_mem,letter),
                "first": lambda x:first_place(main_mem,letter),
                "best": lambda x:best_place(main_mem,letter),
                "next": lambda x:next_place(main_mem,letter),
                "worst": lambda x:worst_place(main_mem,letter)
            }.get(sys.argv[1],-1)(2)
            
            pass

#these functions are for placing letter into appropriate place in main_mem
def noncontiguous_place(main_mem,letter):
    print("noncon")
    
def first_place(main_mem,letter):
    print("first")
    
def best_place(main_mem,letter):
    print("best")
    
def next_place(main_mem,letter):
    print("next")
    
def worst_place(main_mem,letter):
    print("worst")
    

#defragments, but keeps the OS where it belongs
def defrag(main_mem):
    nonsys=main_mem[80:]
    nonsys.sort()
    return itertools.repeat("#",80)+nonsys

main()
