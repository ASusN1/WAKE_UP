import tkinter as tk
import os
import time_logic
from main_menu_function_stuff import open_note_with_mode

WINDOW_BG = "#f7e7bf"
BOARD_BG = "#c98a5a"
BUTTON_BG = "#8a4f2b"
BUTTON_FG = "#fff4d8"

# Create main window
window = tk.Tk()
window.title("WAKE UP")
window.geometry("600x750")
window.configure(bg=WINDOW_BG)

# Create the board box at the top
board_box = tk.Frame(window, width=550, height=400, bg=BOARD_BG, relief="solid", bd=1)
board_box.pack(pady=20, padx=20)
board_box.pack_propagate(False)  # keep the frame size (prevents shrinking)

# Create timer control frame (timer + start button)
timer_control_frame = tk.Frame(window, bg=WINDOW_BG)
timer_control_frame.pack(pady=10)

# Create editable timer display using time_logic
timer_vars = time_logic.create_editable_timer(timer_control_frame)

# Add start timer button beside the timer
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

# Create button frame at the bottom
button_frame = tk.Frame(window, bg=WINDOW_BG)
button_frame.pack(pady=20)

note_maneger_icon = tk.PhotoImage(file=os.path.join(os.path.dirname(__file__), "visual_art", "note_maneger_icon.png"))
btn_note_maneger = tk.Button(button_frame, image=note_maneger_icon, command=lambda: open_note_with_mode(window, "manager"), bg=BUTTON_BG, activebackground="#6e3c21")
btn_note_maneger.pack(side="left", padx=10)

#enter the sticky notes
sticky_note_icon = tk.PhotoImage(file=os.path.join(os.path.dirname(__file__), "visual_art", "sticky note.png"))
btn_sticky = tk.Button(button_frame, image=sticky_note_icon, command=lambda: open_note_with_mode(window, "sticky"), bg=BUTTON_BG, activebackground="#6e3c21")
btn_sticky.pack(side="left", padx=10)

brain_dump_icon = tk.PhotoImage(file=os.path.join(os.path.dirname(__file__), "visual_art", "brain dump.png"))
btn_brain_dump = tk.Button(button_frame, image=brain_dump_icon, command=lambda: open_note_with_mode(window, "brain_dump"), bg=BUTTON_BG, activebackground="#6e3c21")
btn_brain_dump.pack(side="left", padx=10)

delete_note_icon = tk.PhotoImage(file=os.path.join(os.path.dirname(__file__), "visual_art", "trash_can.png"))
btn_delete_note = tk.Button(button_frame, image=delete_note_icon, command=lambda: open_note_with_mode(window, "delete"), bg=BUTTON_BG, activebackground="#6e3c21")
btn_delete_note.pack(side="left", padx=10)

btn_sticky.bind("<Return>", lambda event: open_note_with_mode(window, "sticky"))
btn_brain_dump.bind("<Return>", lambda event: open_note_with_mode(window, "brain_dump"))

btn_close_app = tk.Button(button_frame, text="Quit", command=window.destroy, width=15, bg=BUTTON_BG, fg=BUTTON_FG, activebackground="#6e3c21", activeforeground=BUTTON_FG)
btn_close_app.pack(side="left", padx=10)

if __name__ == "__main__":
    window.mainloop()
