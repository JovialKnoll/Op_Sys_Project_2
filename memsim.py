#Brett Kaplan and Jeff Johnston

from random import randint
import sys

def display_memory(main_mem):
    print '\n'.join(map(str, [''.join(map(str, main_mem[i*80:i*80+80])) for i in range(30)]))
    

def main():
    main_mem = ['#' for i in range(80)]+[chr(j+65) for j in range(20) for k in range(randint(10,100))]
    main_mem += ['.' for i in range(2400-len(main_mem))]
    display_memory(main_mem)
    
main()