#Brett Kaplan and Jeff Johnston

import string
import itertools
from random import randint
import sys
import re

lastplaced=0

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
    if len(sys.argv) != 4 or (sys.argv[1] != "noncontiguous" and sys.argv[1] != "first" and sys.argv[1] != "best" and sys.argv[1] != "next" and sys.argv[1] != "worst") or sys.argv[2] not in range(101) or sys.argv[3] not in range(101):
        print("USAGE: memsim.py { noncontiguous | first | best | next | worst } <process-termination-probability> <new-process-probability>")
        sys.exit()
    
    #initializes memory
    main_mem = list(itertools.repeat("#",80))
    for j in range(20):
        letter=next(letters)
        for k in range(randint(10,100)):
            main_mem.append(letter)
    global lastplaced
    lastplaced=len(main_mem)
    main_mem += ['.' for i in range(2400-lastplaced)]
    
    display_memory(main_mem)
    
    #main loop
    while(True):
        user_input = input("Type c and hit ENTER to continue. ")
        if user_input == 'q':
            return
        elif user_input == 'c':
            for letter in set(main_mem):
                if letter=="." or letter=="#":
                    continue
                #removal of letters
                if(randint(1,100)<=int(sys.argv[2])):
                    remove_proc(main_mem,letter)
            #adding new letters/processes
            if(randint(1,100)<=int(sys.argv[3])):
                letter=next(letters)
                
                startletter = letter
                while letter in main_mem:
                    letter=next(letters)
                    if letter == startletter:
                        print("PROCESS-LIMIT, EXITING")
                        sys.exit()
                
                toplace=randint(10,100)
                worked=switch(main_mem,letter,toplace)
                #after failure, try defragmenting, then stop if reached failure again
                if not worked:
                    main_mem=defrag(main_mem)
                    worked=switch(main_mem,letter,toplace)
                    if not worked:
                        print("OUT-OF-MEMORY, EXITING")
                        sys.exit()
        display_memory(main_mem)

#switching between algorithms for placement based on command line arguments
def switch(main_mem,letter,toplace):
    return {
        "noncontiguous": lambda x:noncontiguous_place(main_mem,letter,toplace),
        "first": lambda x:first_place(main_mem,letter,toplace),
        "best": lambda x:best_place(main_mem,letter,toplace),
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
    pattern = "\.{%d}"%toplace
    memory=''.join(main_mem)
    result=re.search(pattern,memory)
    if(result):
        for i in range(result.start(),result.end()):
            main_mem[i]=letter
        return 1
    return 0
    
def best_place(main_mem,letter,toplace):
    pattern = "\.{%d,}"%toplace
    memory=''.join(main_mem)
    allpossible=re.finditer(pattern,memory)
    #keep track of smallest space open
    try:
        smallest=next(allpossible)
        for result in allpossible:
            if len(result.group(0)) < len(smallest.group(0)):
                smallest=result
        for i in range(smallest.start(),smallest.start()+toplace):
            main_mem[i]=letter
        return 1
    except:
        return 0
    
def next_place(main_mem,letter,toplace):
    global lastplaced
    pattern = "\.{%d}"%toplace
    memory=''.join(main_mem)
    #look for next open space following the last placement
    result=re.search(pattern,memory[lastplaced:]+memory[:lastplaced])
    if(result):
        for i in range(result.start(),result.end()):
            main_mem[(i+lastplaced)%len(main_mem)]=letter
        lastplaced=(result.end()+lastplaced)%len(main_mem)
        return 1
    return 0
    
def worst_place(main_mem,letter,toplace):
    pattern = "\.{%d,}"%toplace
    memory=''.join(main_mem)
    allpossible=re.finditer(pattern,memory)
    #keep track of the largest space open
    try:
        largest=next(allpossible)
        for result in allpossible:
            if len(result.group(0)) > len(largest.group(0)):
                largest=result
        for i in range(largest.start(),largest.start()+toplace):
            main_mem[i]=letter
        return 1
    except:
        return 0

#defragments, but keeps the OS where it belongs
def defrag(main_mem):
    print("OUT-OF-MEMORY\nPERFORMING DEFRAGMENTATION")
    
    nonsys=main_mem[80:]
    #the defragmentation:
    nonsys.sort()
    global lastplaced
    lastplaced=0
    defragged=list(itertools.repeat("#",80))+nonsys
    display_memory(defragged)
    
    print("DEFRAGMENTATION COMPLETED")
    percent="%0.2f"%(defragged.count('.')/24)
    print("Relocated ",len(set(main_mem))-2," processes to create free memory block of ",defragged.count('.')," units (",percent,"% of total memory)")
    return defragged

#emptying out space
def remove_proc(main_mem,letter):
    for i in range(len(main_mem)):
        if main_mem[i]==letter:
            main_mem[i]='.'

main()
