#!/usr/bin/env python3
import tkinter as tk
from random import randint

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
        self.show_mines()
        self.set_surronding_mines_text()

        self.win.mainloop()

    def gen_grid(self):
        '''generates the board, places normal cells and mines on the board'''
        total_mines = 0

        for i in range(MineSweeper.height):
            MineSweeper.board.append([])
            for j in range(MineSweeper.width):
                is_mine = False
                if total_mines < self.number_mines: is_mine = True if randint(1, 2) % 2 == 0 else False
                c = Cell(self.win, is_mine, i, j)
                c.grid(row=i, column=j)
                c["command"] = c.clicked
                MineSweeper.board[i].append(c)

    def show_mines(self):
        '''changes bg colour of mines to red'''
        for r in range(MineSweeper.height):
            for c in range(MineSweeper.width):
                if MineSweeper.board[r][c].is_mine:
                    MineSweeper.board[r][c].config(bg="red", activebackground="red")

    def set_surronding_mines_text(self):
        #TEMP METHOD USED FOR TESTING
        '''sets the text of all cells to their number of surrounding mines'''
        for r in range(MineSweeper.height):
            for c in range(MineSweeper.width):
                if not MineSweeper.board[r][c].is_mine:
                    MineSweeper.board[r][c].calc_surrounding_mines()

class Cell(tk.Button):
    '''instance of a cell on the board'''
    def __init__(self, win, is_mine, row, col):
        #two spaces are set as the default text so that when the cells text is changed
        #the size of the cell doesnt change
        super().__init__(win, text="  ")
        self.is_mine = is_mine
        self.row = row
        self.col = col

    def clicked(self):
        '''Method called when cell is clicked'''
        self.calc_surrounding_mines()
        #print(MineSweeper.board[self.row][self.col + 1].is_mine)

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

        self.config(text=sum(surr_mines), state=tk.DISABLED, relief=tk.SUNKEN)

if __name__ == '__main__':
    MineSweeper(width=10, height=10)
