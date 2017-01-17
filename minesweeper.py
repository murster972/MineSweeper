#!/usr/bin/env python3
import tkinter as tk
from random import randint

class MineSweeper:
    board = []

    def __init__(self, width=10, height=10, number_mines=20):
        #TODO: check number of mines doesnt exceed the size of the board
        self.width = width
        self.height = height
        self.number_mines = number_mines

        self.board = []

        self.win = tk.Tk()
        self.gen_grid()
        self.show_mines()

        self.win.mainloop()

    def gen_grid(self):
        '''generates the board, places normal cells and mines on the board'''
        total_mines = 0

        for i in range(self.height):
            MineSweeper.board.append([])
            for j in range(self.width):
                is_mine = False
                if total_mines < self.number_mines: is_mine = True if randint(1, 2) % 2 == 0 else False
                c = Cell(self.win, is_mine, i, j)
                c.grid(row=i, column=j)
                c["command"] = c.clicked
                MineSweeper.board[i].append(c)

    def show_mines(self):
        '''changes bg colour of mines to red'''
        for r in range(self.height):
            for c in range(self.width):
                if MineSweeper.board[r][c].is_mine:
                    MineSweeper.board[r][c].config(bg="red", activebackground="red")



class Cell(tk.Button):
    '''instance of a cell on the board'''
    def __init__(self, win, is_mine, row, col):
        super().__init__(win)
        self.is_mine = is_mine
        self.row = row
        self.col = col

    def clicked(self):
        '''Method called when cell is clicked'''
        print(self.is_mine, self.row, self.col)
        #print(MineSweeper.board[self.row][self.col + 1].is_mine)

    def surrounding_mines(self):
        '''calculates the number of mines touching the cell'''
        surr_mines = []
        #above
        if self.row != 0:
            surr_mines.append(MineSweeper.board[self.row - 1][self.col].is_mine)

        #below

        #left

        #right

if __name__ == '__main__':
    MineSweeper(width=10, height=10)
