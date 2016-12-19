import curses
stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)

stdscr.addstr(0,10,"Hit 'q' to quit")
stdscr.refresh()

y = 10
x = 50

yo = y - 1
xo = x + 2

key = ''
while key != curses.KEY_DOWN:
    key = stdscr.getch()
    #stdscr.addch(20,25,key)

    #if key == curses.KEY_DOWN:
    #    yo += 3
    if key == curses.KEY_RIGHT:
        if(xo < x + 2 + 4*6):
            xo += 4
    if key == curses.KEY_LEFT:
        if(xo > x + 2): 
            xo -= 4

    stdscr.refresh()
    stdscr.addstr(y, x,     ' ___ ___ ___ ___ ___ ___ ___ ')
    stdscr.addstr(y+1, x,   '|   |   |   |   |   |   |   |')
    stdscr.addstr(y+2, x,   '|   |   |   |   |   |   |   |')
    stdscr.addstr(y+3, x,   '|___|___|___|___|___|___|___|')    
    stdscr.addstr(y+4, x,   '|   |   |   |   |   |   |   |')
    stdscr.addstr(y+5, x,   '|   |   |   |   |   |   |   |')
    stdscr.addstr(y+6, x,   '|___|___|___|___|___|___|___|')    
    stdscr.addstr(y+7, x,   '|   |   |   |   |   |   |   |')
    stdscr.addstr(y+8, x,   '|   |   |   |   |   |   |   |')
    stdscr.addstr(y+9, x,   '|___|___|___|___|___|___|___|')    
    stdscr.addstr(y+10, x,  '|   |   |   |   |   |   |   |')
    stdscr.addstr(y+11, x,  '|   |   |   |   |   |   |   |')
    stdscr.addstr(y+12, x,  '|___|___|___|___|___|___|___|')    
    stdscr.addstr(y+13, x,  '|   |   |   |   |   |   |   |')
    stdscr.addstr(y+14, x,  '|   |   |   |   |   |   |   |')
    stdscr.addstr(y+15, x,  '|___|___|___|___|___|___|___|')    
    stdscr.addstr(y+16, x,  '|   |   |   |   |   |   |   |')
    stdscr.addstr(y+17, x,  '|   |   |   |   |   |   |   |')
    stdscr.addstr(y+18, x,  '|___|___|___|___|___|___|___|')        


    stdscr.addstr(y-2 ,x+2, '                             ')
    stdscr.addstr(y-1 ,x+2, '                             ')
    stdscr.addstr(yo-1,xo,'|')
    stdscr.addstr(yo,  xo, 'v')   
    
    stdscr.addstr(35,25, 'cursor -> ')
    stdscr.refresh()
    
        
curses.endwin()
        
