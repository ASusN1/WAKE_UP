import os
import tkinter as tk

from function_sticky_note import confrim_edit, sticky_note_title
import sound_effect_maneger
from store_note import load_saved_note_data, save_picture_note

WINDOW_BG = "#f7e7bf"
BOARD_BG = "#c98a5a"
BUTTON_BG = "#8a4f2b"
BUTTON_FG = "#fff4d8"


class PictureNote:
    def __init__(self, mode="create", file_path="notes.json", window=None, on_return=None):
        self.owns_window = window is None
        self.window = window if window is not None else tk.Tk()
        self.on_return = on_return

        if not self.owns_window:
            for child in self.window.winfo_children():
                child.destroy()

        self.window.title("Picture Note")
        self.window.geometry("600x720")
        self.window.configure(bg=WINDOW_BG)

        self.note_type = 2
        self.mode = mode
        self.file_path = file_path
        self.saved_data = load_saved_note_data(note_type=self.note_type, file_path=self.file_path) if self.mode == "load" else {}

        self.picture_state = {"image_name": "fat_seal_2.png"}
        self.picture_image = tk.PhotoImage(file=os.path.join(os.path.dirname(__file__), "visual_art", "fat_seal_2.png"))

        title_frame = tk.Frame(self.window, bg=WINDOW_BG)
        title_frame.pack(pady=(20, 10), padx=20, anchor="w")

        initial_title = self.saved_data.get("picture_note_title") or "Picture Note"
        self.title_text = tk.StringVar(master=self.window, value=initial_title)
        title_label = tk.Label(title_frame, textvariable=self.title_text, font=("Arial", 24), bg=WINDOW_BG, fg="#3d2415")
        title_label.pack(side="left", padx=20)
        title_label.bind("<Button-1>", lambda event: sticky_note_title(event, title_frame, self.title_text, title_label))

        picture_frame = tk.Frame(self.window, width=450, height=400, bg="white", relief="solid", bd=4)
        picture_frame.pack(pady=20)
        picture_frame.pack_propagate(False)

        picture_label = tk.Label(picture_frame, image=self.picture_image, bg="white")
        picture_label.image = self.picture_image
        picture_label.pack(expand=True)

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

        do_not_store_info_btn = tk.Button(self.window, text="Don't Save Note", command=self.finish_note, bg=BUTTON_BG, fg=BUTTON_FG, activebackground="#6e3c21", activeforeground=BUTTON_FG)
        do_not_store_info_btn.pack(pady=10)

        finish_btn = tk.Button(self.window, text="Finish", command=lambda: (self.save_current_note(), sound_effect_maneger.play_close_note(), self.finish_note()), bg=BUTTON_BG, fg=BUTTON_FG, activebackground="#6e3c21", activeforeground=BUTTON_FG)
        finish_btn.pack(pady=10)

    def save_current_note(self):
        self.picture_state["image_name"] = "fat_seal_2.png"
        self.file_path = save_picture_note(
            self.title_text,
            self.picture_state,
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
        self.window.destroy()


if __name__ == "__main__":
    app = PictureNote()
    app.run()