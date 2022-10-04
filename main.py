from pdb import Restart
from tkinter import *
import settings
import util
from cell import Cell
import time

def vp_start_gui():
    global root
    root = Tk()

    # Override the setting of the window
    root.configure(bg = 'black')
    root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
    root.title('Minesweeper')
    root.resizable(False,False)



    top_frame = Frame(
        root,
        bg='black',
        width = settings.WIDTH,
        height= util.height_percent(0.1)
    )
    top_frame.place(x=0,y=0)

    game_title = Label(
        top_frame,
        bg = 'black',
        fg = 'White',
        text = f"Minesweeper",
        font = ("bold", 25)
    )
    game_title.place(x = 600, y = 2)

    right_frame = Frame(
        root,
        bg='black',
        width=util.width_percent(0.2),
        height = util.height_percent(0.9)
    )
    right_frame.place(x=util.width_percent(0.8) ,y=util.height_percent(0.1))

    author_title = Label(
        right_frame,
        bg = 'black',
        fg = 'White',
        text = f"Polydoros Prinitis",
        font = ("italic", 10)
    )
    author_title.place(x = 170, y = 630)


    restart_button = Button(
                right_frame, 
                text = f"Restart Game",
                command = restart_game
            )
    restart_button.place(x = 135, y = 50)

    center_frame = Frame(
        root,
        bg='black',
        width = util.width_percent(0.8),
        height= util.height_percent(0.9)
    )
    center_frame.place(x=0,y=util.height_percent(0.1))


    #Generate the cells 
    for x in range(settings.GRID):
        for y in range(settings.GRID*2):
                c = Cell(x,y)
                c.create_cell_button(center_frame)
                c.cell_button.grid(
                    column = y , row = x
                )

    #Make the label for the total cells 
    Cell.create_cell_count_label(top_frame)   
    Cell.cell_count_label.place(x=10 , y=10)

    #Make the label for the total mines 
    Cell.create_mine_count_label(top_frame)   
    Cell.mine_count_label.place(x=1280 , y=10)
    #Create mines
    Cell.generate_mines()


    #Run the window
    root.mainloop()
    
def restart_game():
    root.destroy()
    vp_start_gui()

vp_start_gui()    