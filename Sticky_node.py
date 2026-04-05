#when the user click on the sticky node simple, the app will rederect it to this , and when the user click finish, return 
#to main menu 

#Hwat must have: Editable title ( todya'focus is auto) sticky_note_title
#Add icon next the the stickly_note_sitle( to the right )
#The sticky_note box able to store maxiumum of 5 task 
#When the user havent enter anything: 
#Check box + ( tap to add task) ( when the user click on it ), heightlight the check box and text
#When the user enter a letter on task 1 , task 2 auto appear ( with the check box and tap to add task )
#then conitnue untrill task 5  ( then no more sticky editable check box aand tap to add task thing)
#add a highlightter btn ( when the user click on the btn then select a task out of 5, high light the selected task then )
import tkinter as tk
from Sticky_note_logic import sticky_note_title, confrim_edit, add_note, highlight_note_finished_work, highlight_note_piority, finish_sticky_note

# Create main window
window = tk.Tk()
window.title("WAKE UP")
window.geometry("600x750")

#Title section 
title_frame = tk.Frame(window)
title_frame.pack(pady=20, padx=20, anchor="w")

title_text = tk.StringVar(value="Today's Focus")
title_label = tk.Label(title_frame, textvariable=title_text, font=("Arial", 24))
title_label.pack(side="left", padx=20)

icon_Label = tk.Label(title_frame, text="", font=("Arial", 24))  # will change this later when the user drag icon
icon_Label.pack(side="left", padx=20)

# Bind click to edit title
title_label.bind("<Button-1>", lambda event: sticky_note_title(event, title_frame, title_text, title_label))

#the board container
box_sticky_note = tk.Frame(window, width=450, height=400, bg="white", relief="solid", bd=1)
box_sticky_note.pack(pady=20)
box_sticky_note.pack_propagate(False)  # keep the frame size (prevents shrinking)

notes = []  # To store note entries

#Hightlight note when the user click on the check box
highlight_btn = tk.Button(window, text="Hightlight Taks", command=lambda: highlight_note_finished_work(notes))
highlight_btn.pack(pady=10)

#hHighlight btn to show piority 
hightlight_btn_piority = tk.Button(window, text="Highlight Piority Task", command=lambda: highlight_note_piority(notes))
hightlight_btn_piority.pack(pady=10)

# Finish button
finish_btn = tk.Button(window, text="Finish", command=lambda: finish_sticky_note(window))
finish_btn.pack(pady=10)

add_note(box_sticky_note, notes)

window.mainloop()