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
        return
    #initializes memory
    main_mem = ['#' for i in range(80)]
    for j in range(20):
        letter=next(letters)
        for k in range(randint(10,100)):
            main_mem.append(letter)
    main_mem += ['.' for i in range(2400-len(main_mem))]
    display_memory(main_mem)
    #main loop
    while(True):
        user_input = input("Type c and hit ENTER to continue.")
        if user_input == 'q':
            return
        elif user_input == 'c':
            #put stuff here
            pass
    
main()
