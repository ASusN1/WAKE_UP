import tkinter as tk
from function_sticky_note import sticky_note_title, confrim_edit, add_note, highlight_note_finished_work, highlight_note_piority, finish_sticky_note, get_priority_number
from store_note import load_notes, save_notes

# Create main window
class StickyNotes:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("WAKE UP")
        self.window.geometry("600x750")

        self.notes_type = 0
        self.notes = []  # To store note entries

        #Title section 
        title_frame = tk.Frame(self.window)
        title_frame.pack(pady=20, padx=20, anchor="w")

        title_text = tk.StringVar(value="Today's Focus")
        title_label = tk.Label(title_frame, textvariable=title_text, font=("Arial", 24))
        title_label.pack(side="left", padx=20)

        icon_Label = tk.Label(title_frame, text="", font=("Arial", 24))  # will change this later when the user drag icon
        icon_Label.pack(side="left", padx=20)

        # Bind click to edit title
        title_label.bind("<Button-1>", lambda event: sticky_note_title(event, title_frame, title_text, title_label))

        #the board container
        box_sticky_note = tk.Frame(self.window, width=450, height=400, bg="white", relief="solid", bd=1)
        box_sticky_note.pack(pady=20)
        box_sticky_note.pack_propagate(False)  # keep the frame size (prevents shrinking)

        add_note(box_sticky_note, self.notes)

        #Hightlight note when the user click on the check box
        highlight_btn = tk.Button(self.window, text="Hightlight Taks", command=lambda: highlight_note_finished_work(self.notes))
        highlight_btn.pack(pady=10)

        #hHighlight btn to show piority 
        hightlight_btn_piority = tk.Button(self.window, text="Highlight Piority Task", command=lambda: highlight_note_piority(self.notes))
        hightlight_btn_piority.pack(pady=10)

        #store note data
        store_info_btn = tk.Button(self.window, text ="Save Note", command=lambda: save_notes(title_text, self.notes, get_priority_number(self.notes), note_type=self.notes_type))
        store_info_btn.pack(pady=10)

        do_not_store_info_btn = tk.Button(self.window, text="Don't Save Note", command=lambda: finish_sticky_note(self.window))
        do_not_store_info_btn.pack(pady=10)

        # Finish button
        finish_btn = tk.Button(self.window, text="Finish", command=lambda: (save_notes(title_text, self.notes, get_priority_number(self.notes), note_type=self.notes_type), finish_sticky_note(self.window)))
        finish_btn.pack(pady=10)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = StickyNotes()
    app.run() 