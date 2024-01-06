import curses
import generate as back

difficulty = "intermediate"


def main():
    # stdscr = curses.initscr()
    # print(stdscr)

    sweep = back.logic(difficulty)
    print(sweep.main())


if __name__ == "__main__":
    main()
