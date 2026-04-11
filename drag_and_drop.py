from tkinter import * 

def drag_notes(event):
    widget = event.widget
    Label.startX = event.x 
    Label.startY = event.y

def drag_motion(event):
    x = Label.winfo_x() - Label.startX + event.x
    y = Label.winfo_y() - Label.startY + event.y
    Label.place(x=x, y=y)

window = Tk()

#testing label will chagne to actual notes, later 
Label = Label(window, bg='green', width=10, height=5) #later change to a cuztome icone for sticky note and brain not, add picture note
Label.place(x=0, y=0)


Label.bind("<Button-1>", drag_notes)
Label.bind("<B1-Motion>", drag_motion)

#snap to grid
def snap_to_grid_board(event): #Get the size of board_box, seperate them 
    x = event.x
    y = event.y
    grid_size = 50  # adjust this for larger/smaller grid
    snapped_x = (x // grid_size) * grid_size
    snapped_y = (y // grid_size) * grid_size
    Label.place(x=snapped_x, y=snapped_y)

Label.bind("<ButtonRelease-1>", snap_to_grid_board)
window.mainloop()