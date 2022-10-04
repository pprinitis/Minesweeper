from tkinter import Button, Label
import random
import settings
import ctypes 
import sys


class Cell:
    all = []
    cells_left = settings.TOTAL_CELLS
    mines_left = settings.TOTAL_MINES
    cell_count_label = None
    mine_count_label = None
    def __init__(self,x,y, is_mine=False):
        self.is_mine = is_mine
        self.cell_button = None
        self.x = x
        self.y = y
        self.left_mouse_pressed = False
        self.right_mouse_pressed = False
        self.pressed = False
        self.marked = False

        #Append the object the Cell.mines list
        Cell.all.append(self)

    def create_cell_button(self, location):
        t_button = Button(
            location, 
            width=4,
            height=2,
        )
        t_button.bind("<Button-1>", self.onAnyofTwoPressed)
        t_button.bind("<Button-3>", self.onAnyofTwoPressed)

        t_button.bind("<ButtonRelease-1>", self.resetPressedState)
        t_button.bind("<ButtonRelease-3>", self.resetPressedState)

        self.cell_button = t_button

    @staticmethod
    def create_mine_count_label(location):
        lbl = Label(
            location,
            bg = 'black',
            fg = 'white',
            text = f"Mines Left: {Cell.mines_left}",
 
            font = ("", 15)
        )
        Cell.mine_count_label = lbl
    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            bg = 'black',
            fg = 'white',
            text = f"Cells Left: {Cell.cells_left}",
 
            font = ("", 15)
        )
        Cell.cell_count_label = lbl

    def onAnyofTwoPressed(self, event):
        if event.num==1:
            self.left_mouse_pressed = True
        if event.num==3:
            self.right_mouse_pressed = True
  
    def resetPressedState(self, event):
            if (self.left_mouse_pressed and self.right_mouse_pressed):
                if(self.pressed == True):
                    print("Yayyy")
                    

            elif (self.left_mouse_pressed):
                if self.is_mine:
                    self.show_mine()
                else:
                    self.show_cell()    

            elif ( self.right_mouse_pressed):
                if not self.marked:
                    self.cell_button.configure(bg = 'red')
                    self.marked = True
                    Cell.mines_left -=1
                else:
                    self.cell_button.configure(bg = 'SystemButtonFace')
                    self.marked = False
                    Cell.mines_left +=1

                if Cell.mine_count_label:
                    Cell.mine_count_label.configure( text = f"Mines Left: {Cell.mines_left}",)
                
            self.left_mouse_pressed = False
            self.right_mouse_pressed = False

    def test_Cell_For_Mine(self,x,y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y and cell.is_mine == True:
                return True
    
    def show_cell(self):
        if(self.pressed == False):
            near_mines = 0
            if(self.test_Cell_For_Mine(self.x-1,self.y-1)):
                near_mines +=1
            if(self.test_Cell_For_Mine(self.x-1,self.y)):
                near_mines +=1
            if(self.test_Cell_For_Mine(self.x-1,self.y+1)):
                near_mines +=1
            if(self.test_Cell_For_Mine(self.x,self.y-1)):
                near_mines +=1
            if(self.test_Cell_For_Mine(self.x,self.y+1)):
                near_mines +=1
            if(self.test_Cell_For_Mine(self.x+1,self.y-1)):
                near_mines +=1
            if(self.test_Cell_For_Mine(self.x+1,self.y)):
                near_mines +=1
            if(self.test_Cell_For_Mine(self.x+1,self.y+1)):
                near_mines +=1    

            self.cell_button.configure(text = near_mines)     
            self.pressed = True 
            Cell.cells_left -= 1
            if Cell.cell_count_label:
                Cell.cell_count_label.configure( text = f"Cells Left: {Cell.cells_left}",)
            if(near_mines == 0):
                self.show_surround(self.x, self.y)


    def show_surround(self,x,y):
        for cell in Cell.all:
            if(cell.x == x-1 and cell.y ==y-1):
                cell.show_cell()
            elif(cell.x == x-1 and cell.y ==y):
                cell.show_cell()
            elif(cell.x == x-1 and cell.y ==y+1):
                cell.show_cell()
            elif(cell.x == x and cell.y ==y-1):
                cell.show_cell()
            elif(cell.x == x and cell.y==y+1):
                cell.show_cell()
            elif(cell.x == x+1 and cell.y==y-1):
                cell.show_cell()
            elif(cell.x == x+1 and cell.y==y):
                cell.show_cell()
            elif(cell.x == x+1 and cell.y==y+1):
                cell.show_cell()
    
    def show_mine(self):
        #Terminate game
        self.cell_button.configure(bg = 'red')
        ctypes.windll.user32.MessageBoxW(0, '\n     Clicked mine\n\n', 'Game Over', 0)
        sys.exit()
        

    @staticmethod
    def generate_mines():

        mines = random.sample(Cell.all,settings.TOTAL_MINES)

        for mine in mines:
            mine.is_mine = True
