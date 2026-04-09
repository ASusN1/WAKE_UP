import tkinter as tk
import UI_sticky_notes
import store_note
import brain_dump_note
import time_logic

# Create main window
window = tk.Tk()
window.title("WAKE UP")
window.geometry("600x750")

# Create a display box at the top
display_box = tk.Frame(window, width=550, height=400, bg="white", relief="solid", bd=1)
display_box.pack(pady=20, padx=20)
display_box.pack_propagate(False)  # keep the frame size (prevents shrinking)

# Create timer control frame (timer + start button)
timer_control_frame = tk.Frame(window)
timer_control_frame.pack(pady=10)

# Create editable timer display using time_logic
timer_vars = time_logic.create_editable_timer(timer_control_frame)

# Add start timer button beside the timer
start_timer_btn = tk.Button(timer_control_frame, text="Start Timer", command=lambda: time_logic.start_countdown(timer_vars, window))
start_timer_btn.pack(side="left", padx=10)

# Create button frame at the bottom
button_frame = tk.Frame(window)
button_frame.pack(pady=20)

#enter the sticky notes
btn_sticky = tk.Button(button_frame, text="Sticky Notes", command=lambda: UI_sticky_notes.StickyNotes().run(), width=15)
btn_sticky.pack(side="left", padx=10)

btn_brain_dump = tk.Button(button_frame, text="Brain Dump", command=lambda: brain_dump_note.BrainDumpNote().run(), width=15)
btn_brain_dump.pack(side="left", padx=10)

btn_close_app = tk.Button(button_frame, text="Quit", command=window.destroy, width=15)
btn_close_app.pack(side="left", padx=10)

if __name__ == "__main__":
    window.mainloop()
