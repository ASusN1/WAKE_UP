import tkinter as tk
from function_sticky_note import sticky_note_title, confrim_edit, add_note, highlight_note_finished_work, highlight_note_piority, finish_sticky_note, get_priority_number
from store_note import load_notes, save_notes

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

add_note(box_sticky_note, notes)

#Hightlight note when the user click on the check box
highlight_btn = tk.Button(window, text="Hightlight Taks", command=lambda: highlight_note_finished_work(notes))
highlight_btn.pack(pady=10)

#hHighlight btn to show piority 
hightlight_btn_piority = tk.Button(window, text="Highlight Piority Task", command=lambda: highlight_note_piority(notes))
hightlight_btn_piority.pack(pady=10)

#store note data
store_info_btn = tk.Button(window, text ="Save Note", command=lambda: save_notes(title_text, notes, get_priority_number(notes), note_type=notes_type))
store_info_btn.pack(pady=10)

do_not_store_info_btn = tk.Button(window, text="Don't Save Note", command=lambda: finish_sticky_note(window))
do_not_store_info_btn.pack(pady=10)

# Finish button
finish_btn = tk.Button(window, text="Finish", command=lambda: (save_notes(title_text, notes, get_priority_number(notes), note_type=notes_type), finish_sticky_note(window)))
finish_btn.pack(pady=10)

notes_type = 0

window.mainloop()