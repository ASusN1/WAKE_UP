import tkinter as tk
import os
import time_logic
from main_menu_function_stuff import open_note_with_mode, clear_window, open_note_from_board
from drag_and_drop import show_saved_notes_on_board

WINDOW_BG = "#f7e7bf"
BOARD_BG = "#c98a5a"
BUTTON_BG = "#8a4f2b"
BUTTON_FG = "#fff4d8"

window = tk.Tk()
window.title("WAKE UP")
window.geometry("600x750")
window.configure(bg=WINDOW_BG)

def build_main_menu(_window=None):
    clear_window(window)

    board_box = tk.Frame(window, width=550, height=400, bg=BOARD_BG, relief="solid", bd=1)
    board_box.pack(pady=20, padx=20)
    board_box.pack_propagate(False)

    timer_control_frame = tk.Frame(window, bg=WINDOW_BG)
    timer_control_frame.pack(pady=10)

    timer_vars = time_logic.create_editable_timer(timer_control_frame)

    start_timer_btn = tk.Button(
        timer_control_frame,
        text="Start Timer",
        command=lambda: time_logic.start_countdown(timer_vars, window),
        bg=BUTTON_BG,
        fg=BUTTON_FG,
        activebackground="#6e3c21",
        activeforeground=BUTTON_FG,
    )
    start_timer_btn.pack(side="left", padx=10)

    button_frame = tk.Frame(window, bg=WINDOW_BG)
    button_frame.pack(pady=20)

    note_maneger_icon = tk.PhotoImage(file=os.path.join(os.path.dirname(__file__), "visual_art", "note_maneger_icon.png"))
    btn_note_maneger = tk.Button(button_frame, image=note_maneger_icon, command=lambda: open_note_with_mode(window, "manager", on_return_to_menu=build_main_menu), bg=BUTTON_BG, activebackground="#6e3c21")
    btn_note_maneger.pack(side="left", padx=10)

    sticky_note_icon = tk.PhotoImage(file=os.path.join(os.path.dirname(__file__), "visual_art", "sticky note.png"))
    btn_sticky = tk.Button(button_frame, image=sticky_note_icon, command=lambda: open_note_with_mode(window, "sticky", on_return_to_menu=build_main_menu), bg=BUTTON_BG, activebackground="#6e3c21")
    btn_sticky.pack(side="left", padx=10)

    brain_dump_icon = tk.PhotoImage(file=os.path.join(os.path.dirname(__file__), "visual_art", "brain dump.png"))
    btn_brain_dump = tk.Button(button_frame, image=brain_dump_icon, command=lambda: open_note_with_mode(window, "brain_dump", on_return_to_menu=build_main_menu), bg=BUTTON_BG, activebackground="#6e3c21")
    btn_brain_dump.pack(side="left", padx=10)

    delete_note_icon_base = tk.PhotoImage(file=os.path.join(os.path.dirname(__file__), "visual_art", "trash_can.png"))
    delete_note_icon = delete_note_icon_base.zoom(2, 2)

    trash_button_frame = tk.Frame(window, bg=WINDOW_BG)
    trash_button_frame.pack(pady=(0, 10))

    trash_button = tk.Button(
        trash_button_frame,
        image=delete_note_icon,
        command=lambda: open_note_with_mode(window, "delete", on_return_to_menu=build_main_menu),
        bg=BUTTON_BG,
        activebackground="#6e3c21",
    )
    trash_button.pack()
    trash_button.image = delete_note_icon

    show_saved_notes_on_board(
        board_box,
        os.path.join(os.path.dirname(__file__), "visual_art"),
        on_open_note=lambda note_type, file_name: open_note_from_board(note_type, file_name, window, build_main_menu),
        trash_widget=trash_button,
    )

    btn_sticky.bind("<Return>", lambda event: open_note_with_mode(window, "sticky", on_return_to_menu=build_main_menu))
    btn_brain_dump.bind("<Return>", lambda event: open_note_with_mode(window, "brain_dump", on_return_to_menu=build_main_menu))

    btn_close_app = tk.Button(button_frame, text="Quit", command=window.destroy, width=15, bg=BUTTON_BG, fg=BUTTON_FG, activebackground="#6e3c21", activeforeground=BUTTON_FG)
    btn_close_app.pack(side="left", padx=10)

    window.main_menu_icons = [note_maneger_icon, sticky_note_icon, brain_dump_icon, delete_note_icon_base, delete_note_icon, trash_button]


build_main_menu()

if __name__ == "__main__":
    window.mainloop()
