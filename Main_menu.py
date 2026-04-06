import tkinter as tk
import UI_sticky_notes
#import store_note

# Create main window
window = tk.Tk()
window.title("WAKE UP")
window.geometry("600x750")

# Create a box (Frame)
box = tk.Frame(window, width=450, height=400, bg="white")
box.pack(pady=20)

# Keep the frame size (prevents shrinking)
box.pack_propagate(False)

window.mainloop()