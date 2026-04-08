import tkinter as tk 
from brain_dump_note_function import add_brain_dump_note, brain_dump_note_title, finish_brain_dump_note
from store_note import load_brain_dump_note, save_brain_dump_note

window = tk.Tk()
window.title("Brain Dump Note")
window.geometry("600x720")

#Title section
title_frame_bd = tk.Frame(window)
title_frame_bd.pack(pady=20, padx=20, anchor="w")

title_text_bd = tk.StringVar(value="Brain Dump Note")
title_label = tk.Label(title_frame_bd, textvariable=title_text_bd, font=("Arial", 24))
title_label.pack(side="left", padx=20)

icon_Label = tk.Label(title_frame_bd, text ="", font = ("Arial", 24)) # will change this later when the user drag icon
icon_Label.pack(side="left", padx=20)

#bind click to edit 
title_label.bind("<Button-1>", lambda event: brain_dump_note_title(event, title_frame_bd, title_text_bd, title_label)) #update this later with the actual notes 

#the text container
box_brain_dump_note = tk.Frame(window, width=450, height=400, bg="white", relief="solid", bd=1)
box_brain_dump_note.pack(pady=20)
box_brain_dump_note.pack_propagate(False) # keep the frame size (prevents shrinking)

brain_dump_notes = [] #to store what user entered, 

saved_paragraph = load_brain_dump_note()
add_brain_dump_note(box_brain_dump_note, brain_dump_notes, initial_paragraph=saved_paragraph)

#store data
store_info_btn = tk.Button(window, text ="Save Note", command=lambda: save_brain_dump_note(title_text_bd, brain_dump_notes, note_type=note_type))
store_info_btn.pack(pady=10)

#don't store data
do_not_store_info_btn = tk.Button(window, text="Don't Save Note", command=lambda: finish_brain_dump_note(window))
do_not_store_info_btn.pack(pady=10)

finish_btn = tk.Button(window, text="Finish", command=lambda: (save_brain_dump_note(title_text_bd, brain_dump_notes, note_type=note_type), finish_brain_dump_note(window)))
finish_btn.pack(pady=10)

note_type= 1 

window.mainloop()