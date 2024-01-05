import curses 
import logic as back
difficulty = 'intermediate'

def main():

    # stdscr = curses.initscr()
    # print(stdscr)

    sweep = back.logic(difficulty)
    sweep.grid()
    sweep.mask_grid()






if __name__ == '__main__':
    main()