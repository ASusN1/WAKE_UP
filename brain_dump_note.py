import os
import tkinter as tk 
from brain_dump_note_function import add_brain_dump_note, brain_dump_note_title, finish_brain_dump_note
import sound_effect_maneger
from store_note import load_saved_note_data, save_brain_dump_note

WINDOW_BG = "#f7e7bf"
BOARD_BG = "#c98a5a"
BUTTON_BG = "#8a4f2b"
BUTTON_FG = "#fff4d8"

class BrainDumpNote:
    def __init__(self, mode="create", file_path="notes.json", window=None, on_return=None):
        self.owns_window = window is None
        self.window = window if window is not None else tk.Tk()
        self.on_return = on_return

        if not self.owns_window:
            for child in self.window.winfo_children():
                child.destroy()

        self.window.title("Brain Dump Note")
        self.window.geometry("600x720")
        self.window.configure(bg=WINDOW_BG)

        self.note_type = 1
        self.brain_dump_notes = [] #to store what user entered
        self.mode = mode
        self.file_path = file_path
        self.saved_data = load_saved_note_data(note_type=self.note_type, file_path=self.file_path) if self.mode == "load" else {}

        #Title section
        title_frame_bd = tk.Frame(self.window, bg=WINDOW_BG)
        title_frame_bd.pack(pady=(20, 10), padx=20, anchor="w")

        initial_title = self.saved_data.get("brain_dump_title") or "Brain Dump Note"
        self.title_text_bd = tk.StringVar(master=self.window, value=initial_title)
        title_label = tk.Label(title_frame_bd, textvariable=self.title_text_bd, font=("Arial", 24), bg=WINDOW_BG, fg="#3d2415")
        title_label.pack(side="left", padx=20)

        icon_Label = tk.Label(title_frame_bd, text ="", font = ("Arial", 24), bg=WINDOW_BG, fg="#3d2415") # will change this later when the user drag icon
        icon_Label.pack(side="left", padx=20)

        #bind click to edit 
        title_label.bind("<Button-1>", lambda event: brain_dump_note_title(event, title_frame_bd, self.title_text_bd, title_label)) #update this later with the actual notes 

        #the text container
        box_brain_dump_note = tk.Frame(self.window, width=450, height=400, bg=BOARD_BG, relief="solid", bd=1)
        box_brain_dump_note.pack(pady=20)
        box_brain_dump_note.pack_propagate(False) # keep the frame size (prevents shrinking)

        saved_paragraph = self.saved_data.get("brain_dump_note", "")
        add_brain_dump_note(box_brain_dump_note, self.brain_dump_notes, initial_paragraph=saved_paragraph)

        #store data
        save_icon_path = os.path.join(os.path.dirname(__file__), "visual_art", "save_icon.png")
        self.save_btn_icon_base = tk.PhotoImage(file=save_icon_path)
        self.save_btn_icon = self.save_btn_icon_base.zoom(3, 3)
        store_info_btn = tk.Button(
            self.window,
            image=self.save_btn_icon,
            command=lambda: (self.save_current_note(), sound_effect_maneger.play_save_note_sound()),
            bg=BUTTON_BG,
            activebackground="#6e3c21",
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
        )
        store_info_btn.pack(pady=12, ipadx=4, ipady=4)

        #don't store data
        do_not_store_info_btn = tk.Button(self.window, text="Don't Save Note", command=self.finish_note, bg=BUTTON_BG, fg=BUTTON_FG, activebackground="#6e3c21", activeforeground=BUTTON_FG)
        do_not_store_info_btn.pack(pady=10)

        finish_btn = tk.Button(self.window, text="Finish", command=lambda: (self.save_current_note(), sound_effect_maneger.play_close_note(), self.finish_note()), bg=BUTTON_BG, fg=BUTTON_FG, activebackground="#6e3c21", activeforeground=BUTTON_FG)
        finish_btn.pack(pady=10)

    def save_current_note(self):
        self.file_path = save_brain_dump_note(
            self.title_text_bd,
            self.brain_dump_notes,
            note_type=self.note_type,
            file_path=self.file_path,
        )

    def run(self):
        if self.owns_window:
            self.window.mainloop()

    def finish_note(self):
        if callable(self.on_return):
            self.on_return(self.window)
            return
        finish_brain_dump_note(self.window)

if __name__ == "__main__":
    app = BrainDumpNote()
    app.run() 

