#usr/bin/env python
#use reset when struck
#NEW FIND: OLD THINGS GET BEHIND NEW THINGS
from unicurses import *

def main():
    stdscr = initscr()
    #move( col, row)
    move( 0, 0 )
    addstr( "First line" )
    #move before adding string
    mvaddstr(1, 1, "mvaddstr")

    for i in range( 2, 50 ):
        mvaddstr( i,i, "Hello there" )

    getch()
    endwin()
    return 0;

if ( __name__ == "__main__" ):
    main()
