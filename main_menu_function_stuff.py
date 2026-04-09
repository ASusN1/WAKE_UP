import os
import tkinter as tk
from tkinter import messagebox

import UI_sticky_notes
import brain_dump_note
import store_note


def note_type_from_key(note_key):
	return 0 if note_key == "sticky" else 1


def open_note(note_key, mode, file_path="notes.json"):
	if note_key == "sticky":
		UI_sticky_notes.StickyNotes(mode=mode, file_path=file_path).run()
	else:
		brain_dump_note.BrainDumpNote(mode=mode, file_path=file_path).run()


def list_saved_note_files(note_type):
	directory = store_note.get_note_directory(note_type)
	if not os.path.isdir(directory):
		return []

	files = [name for name in os.listdir(directory) if name.lower().endswith(".json")]
	files.sort()
	return files


def show_load_picker(parent_window, note_key, chooser_window):
	note_type = note_type_from_key(note_key)
	saved_files = list_saved_note_files(note_type)

	if not saved_files:
		messagebox.showinfo("No Saved Note", "No saved note found yet. Opening a new note.")
		chooser_window.destroy()
		open_note(note_key, mode="create")
		return

	picker = tk.Toplevel(parent_window)
	picker.title("Select Saved Note")
	picker.geometry("340x260")
	picker.transient(parent_window)
	picker.grab_set()

	tk.Label(picker, text="Choose a saved note file:", font=("Arial", 11)).pack(pady=(12, 8))

	list_box = tk.Listbox(picker, width=42, height=8)
	list_box.pack(padx=12, pady=6, fill="both", expand=True)

	for name in saved_files:
		list_box.insert(tk.END, name)

	if saved_files:
		list_box.selection_set(0)

	def load_selected():
		selection = list_box.curselection()
		if not selection:
			messagebox.showinfo("Select File", "Please select a file to load.")
			return

		selected_file = list_box.get(selection[0])
		picker.destroy()
		chooser_window.destroy()
		open_note(note_key, mode="load", file_path=selected_file)

	button_row = tk.Frame(picker)
	button_row.pack(pady=(6, 10))

	tk.Button(button_row, text="Load", width=12, command=load_selected).pack(side="left", padx=6)
	tk.Button(button_row, text="Cancel", width=12, command=picker.destroy).pack(side="left", padx=6)

	list_box.bind("<Double-Button-1>", lambda event: load_selected())


def open_note_with_mode(parent_window, note_key):
	chooser = tk.Toplevel(parent_window)
	chooser.title("Create or Load")
	chooser.geometry("300x150")
	chooser.transient(parent_window)
	chooser.grab_set()

	tk.Label(chooser, text="Choose an option:", font=("Arial", 12)).pack(pady=(16, 10))

	button_row = tk.Frame(chooser)
	button_row.pack(pady=8)

	tk.Button(button_row, text="Create New", width=12, command=lambda: (chooser.destroy(), open_note(note_key, mode="create"))).pack(side="left", padx=6)
	tk.Button(button_row, text="Load Saved", width=12, command=lambda: show_load_picker(parent_window, note_key, chooser)).pack(side="left", padx=6)
