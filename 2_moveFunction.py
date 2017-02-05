#usr/bin/env python
#use reset when struck
from unicurses import *

def main(): #{
    stdscr = initscr()

    move ( 5, 0 );

    addstr("Hello world");

    getch();
    endwin();
    return 0;
#}

if ( __name__ == "__main__" ): #{
    main();
#}
