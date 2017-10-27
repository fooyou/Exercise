/**
 * @File Name: curses.c
 * @Author: Joshua Liu
 * @Email: liuchaozhenyu@gmail.com
 * @Create Date: 2017-08-22 15:08:18
 * @Last Modified: 2017-08-22 15:08:01
 * @Description:
**/
#include <ncurses.h>
#include <string.h>

int main() {
    char msg[] = "Enter a string: ";
    char str[80];
    int row, col;

    initscr();
    getmaxyx(stdscr, row, col);
    mvprintw(row/2, (col-strlen(msg))/2, "%s", msg);

    getstr(str);
    mvprintw(LINES-2, 0, "You Entered: %s", str);
    getch();
    endwin();
    return 0;
}
