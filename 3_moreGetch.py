#usr/bin/env python
#use reset when struck
from unicurses import *

def main():
    stdscr = initscr()

    #getch returns what was pressed
    #c = getch()
    #addstr(str(c))

    running = True
    while ( running ):
        key = getch()

        #keycode 10 is enter
        if ( key == 10 ):
            running = False
            break
        elif ( key == ord('a') ):
            move ( 2, 0 )
            addstr ( "You pressed the A key" )
            continue

        move( 10, 0 )
        addstr( "Keycode pressed was" + str(key) + " and the key was " + chr(key) )
        #chr( value ) is ascii to alphabet
        move ( 0, 0 )

    getch()
    endwin()
    return 0;

if ( __name__ == "__main__" ):
    main()
