import tkinter as tk
import Sticky_node
#import store_note

# Create main window
window = tk.Tk()
window.title("WAKE UP")
window.geometry("600x750")

# Create a box (Frame)
box = tk.Frame(window, width=450, height=400, bg="white")
box.pack(pady=20)

# Keep the frame size (prevents shrinking)
box.pack_propagate(False)

#stuff need to do next 
#sticky note btn 
#when click on this it will goes to stsicky_node and run it. when the user finsihed and press save_notes then stores ( use the store note py).update 
#next time user reopen the app, when they click btn_the_sticky_note, it will show the list of note they have saved before, and when they click on the note, it will open the sticky note with the content they have before (use the load_note function in store_note.py to load the content)
#btn_the_sticky_note = tk.Button(window, text="Sticky Note", command=lambda: sticky_node())  # when the user click on the sticky note button, it will open a pop up show a list of notes the user has saved before 


#delect note: when the user press this btn, a pop up shown up , and show the name of the note. Ex) Get the tile from title_text from sticky note, saved that name finish, return to main menu, click detelect, delect the note with same name as the title_text
#btn_delecct_note = tk.Button(window, text="Delect Note", command=lambda: window.destroy())  # when the user click on the delect note button, it will open a pop up show a list of notes the user has saved before and ask which one they want to delect
# Run the app
window.mainloop()