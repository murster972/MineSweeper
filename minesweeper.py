#!/usr/bin/env python3
import tkinter as tk
from random import randint

#TODO: Add Menu with options - New Game, Solve Game, Board Options(Size, Number of mines)
#TODO: If an empty cell is clicked, make every empty cell surronding it in a "clicked" state aswell
#TODO: add flags
#TODO: Add error checking for module imports
#TODO: Add status bar along bottom

class MineSweeper:
    board = []
    width = []
    height = []

    def __init__(self, width=10, height=10, number_mines=20):
        #TODO: check number of mines doesnt exceed the size of the board
        MineSweeper.width = width
        MineSweeper.height = height
        self.number_mines = number_mines

        self.board = []

        self.win = tk.Tk()
        self.gen_grid()
        self.set_mines()
        self.show_mines()
        self.set_surronding_mines_text()

        #add status bar
        MineSweeper.status = tk.Label(self.win, text="MINES: {}".format(self.number_mines))
        MineSweeper.status.grid(row=MineSweeper.width, column=0, columnspan=MineSweeper.width - 1, pady=5)

        #self.show_mines()
        #self.set_surronding_mines_text()

        self.win.mainloop()

    def gen_grid(self):
        '''generates the board, places normal cells and mines on the board'''
        total_mines = 0

        for i in range(MineSweeper.height):
            MineSweeper.board.append([])
            for j in range(MineSweeper.width):
                c = Cell(self.win, i, j)
                c.grid(row=i, column=j)
                c["command"] = c.clicked
                MineSweeper.board[i].append(c)

    def set_mines(self):
        '''sets certain cells as mines'''
        total = 0
        while total != self.number_mines:
            x, y = randint(0, MineSweeper.width - 1), randint(0, MineSweeper.height - 1)
            if not MineSweeper.board[x][y].is_mine:
                MineSweeper.board[x][y].is_mine = True
                total += 1

    def show_mines(self):
        '''changes bg colour of mines to red'''
        for r in range(MineSweeper.height):
            for c in range(MineSweeper.width):
                if MineSweeper.board[r][c].is_mine:
                    MineSweeper.board[r][c].config(bg="red", activebackground="red", state=tk.DISABLED, text="X")

    def set_surronding_mines_text(self):
        #TEMP METHOD USED FOR TESTING
        '''sets the text of all cells to their number of surrounding mines'''
        for r in range(MineSweeper.height):
            for c in range(MineSweeper.width):
                if not MineSweeper.board[r][c].is_mine:
                    MineSweeper.board[r][c].calc_surrounding_mines()

class Cell(tk.Button, MineSweeper):
    '''instance of a cell on the board'''
    def __init__(self, win, row, col):
        #two spaces are set as the default text so that when the cells text is changed
        #the size of the cell doesnt change
        super().__init__(win, text="  ")
        self.is_mine = False
        self.row = row
        self.col = col
        self.surr_mines = None
        self.checked_surr = False

    def clicked(self):
        '''Method called when cell is clicked'''
        if self.is_mine:
            self.game_over()
        else:
            self.calc_surrounding_mines()

    def game_over(self):
        '''revels cells as mine, and sets gameover'''
        self.config(text="X")

        self.set_surronding_mines_text()
        self.show_mines()
        MineSweeper.status.config(text="GAME OVER")

    def calc_surrounding_mines(self):
        '''calculates and sets cell text to the number of mines touching the cell'''
        surr_mines = []
        #above, below
        for i in [[0, -1], [MineSweeper.height - 1, 1]]:
            if self.row != i[0]:
                surr_mines.append(MineSweeper.board[self.row + i[1]][self.col].is_mine)
                if self.col != 0:
                    surr_mines.append(MineSweeper.board[self.row + i[1]][self.col - 1].is_mine)
                if self.col != MineSweeper.width - 1:
                    surr_mines.append(MineSweeper.board[self.row + i[1]][self.col + 1].is_mine)

        #left, right
        if self.col != 0: surr_mines.append(MineSweeper.board[self.row][self.col - 1].is_mine)
        if self.col != MineSweeper.width - 1: surr_mines.append(MineSweeper.board[self.row][self.col + 1].is_mine)

        self.surr_mines = sum(surr_mines)

        #ONLY TEMP, SHOULD STILL BE CHANGED IF EMTPY
        #if not total: total = "  "
        if not self.checked_surr:
            if self.surr_mines:
                self.config(text=self.surr_mines, state=tk.DISABLED, relief=tk.SUNKEN)
            else:
                self.no_surronding_mines()

        #self.checked_surr = True

    def no_surronding_mines(self):
        '''method called when the cell has no mines touching it, it reveals all the emtpy cells around the cell, upto
           and including cells surronding mines, and upto mines'''
        empty_surr_cells = []

        

if __name__ == '__main__':
    MineSweeper(width=10, height=10)
