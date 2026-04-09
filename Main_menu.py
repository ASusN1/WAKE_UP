import tkinter as tk
import UI_sticky_notes
import store_note
import brain_dump_note

# Create main window
window = tk.Tk()
window.title("WAKE UP")
window.geometry("600x750")

# Create a box container
box_container = tk.Frame(window, width=450, height=450, bg="white", relief="solid", bd=1)
box_container.pack(pady=20)
box_container.pack_propagate(False)  # keep the frame size (prevents shrinking)

#enter the sticky notes
btn_sticky = tk.Button(box_container, text="Sticky Notes", command=lambda: UI_sticky_notes.StickyNotes().run())
btn_sticky.pack(pady=10)

btn_brain_dump = tk.Button(box_container, text="Brain Dump", command=lambda: brain_dump_note.BrainDumpNote().run())
btn_brain_dump.pack(pady=10)

btn_close_app = tk.Button(window, text="Close App", command=window.destroy)
btn_close_app.pack(pady=10)

if __name__ == "__main__":
    window.mainloop()
