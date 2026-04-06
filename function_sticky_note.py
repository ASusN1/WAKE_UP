import tkinter as tk

selected_task = None

def select_task(note_row):
    global selected_task
    selected_task = note_row

def sticky_note_title(event, title_frame, title_text, title_label):
    title_entry = tk.Entry(title_frame, font=("Arial", 24))
    title_entry.insert(0, title_text.get())
    title_entry.pack(side="left", padx=20)
    title_label.pack_forget()  # Hide the title when the user click on it
    title_entry.focus_set()
    title_entry.bind("<Return>", lambda e: confrim_edit(e, title_entry, title_label, title_text))

def confrim_edit(event, title_entry, title_label, title_text):
    title_text.set(title_entry.get())
    title_entry.destroy()  # Destroy the entry widget after the user finish editing
    title_label.pack(side="left", padx=20)  # Show the title again after the user finish editing

def add_note(box, notes, event=None):
    if len(notes) < 5:  # maximum of 5 tasks
        # create a container "the board" to store the task and the check box
        note_row = tk.Frame(box, bg="white")
        note_row.pack(anchor="w", pady=5, padx=10)
        # remember to add the animation when all check btn is pressed
        check_var = tk.IntVar()
        check_btn = tk.Checkbutton(note_row, bg="white", variable=check_var)
        check_btn.pack(side="left")

        note_entry = tk.Entry(note_row, width=40, bg="white", font=("Arial", 14))
        note_entry.pack(side="left", padx=5)

        # new stuff just learn: basically the | when click on browser (search bar stuff)
        note_entry.focus_set()
        notes.append({
            "row": note_row,
            "check_btn": check_btn,
            "check_var": check_var,
            "entry": note_entry,
        })  # store the note row, check btn and note entry in a list for later use

        note_row.bind("<Button-1>", lambda e, row=note_row: select_task(row))
        check_btn.bind("<Button-1>", lambda e, row=note_row: select_task(row))
        note_entry.bind("<Button-1>", lambda e, row=note_row: select_task(row))

        note_entry.bind("<Return>", lambda e: add_note(box, notes, e))  # when the user press enter, it will add a new note
        return
    return

def highlight_note_finished_work(notes):
    for item in notes:
        note_row = item["row"]
        check_var = item["check_var"]
        if check_var.get() == 1:  # if the check btn is checked
            note_row.config(bg="yellow")  # highlight the note row
        else:
            note_row.config(bg="white")  # unhighlight the note row

def highlight_note_piority(notes):
    target = selected_task

    if target is None:
        return

    for item in notes:
        item["row"].config(bg="white")
        item["check_btn"].config(bg="white")
        item["entry"].config(bg="white")

    for item in notes:
        if item["row"] is target:
            item["row"].config(bg="red")
            item["check_btn"].config(bg="red")
            item["entry"].config(bg="red")
            break

def finish_sticky_note(window):
    window.destroy()
