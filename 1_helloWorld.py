#usr/bin/env python
#use reset when struck
from unicurses import *

def main(): #{
    #CAUTION: DON'T USE SEMICOLONS IN UNICURSES CODE
    #initialize ncurses
    stdscr = initscr()
    #string added to screen at current position of cursor
    addstr("Hello world");

    getch();
    endwin();

    return 0;
#}

if ( __name__ == "__main__" ): #{
    main();
#}
