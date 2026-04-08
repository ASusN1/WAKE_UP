import tkinter as tk 


def brain_dump_note_title(event, title_frame, title_text, title_label):
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

def add_brain_dump_note(box, brain_dump_notes, event=None, initial_paragraph=""):
    if brain_dump_notes:
        existing = brain_dump_notes[0].get("paragraph")
        if existing is not None:
            return existing

    scrollbar = tk.Scrollbar(box)
    scrollbar.pack(side="right", fill="y")

    paragraph = tk.Text(box,wrap="word",font=("Arial", 13), undo=True, yscrollcommand=scrollbar.set, bg="white", relief="flat", padx=10, pady=10,)
    paragraph.pack(side="left", fill="both", expand=True)
    scrollbar.config(command=paragraph.yview)

    if initial_paragraph:
        paragraph.insert("1.0", initial_paragraph)

    paragraph.focus_set()
    brain_dump_notes.append({"paragraph": paragraph})
    return paragraph


def finish_brain_dump_note(window):
    window.destroy()
    