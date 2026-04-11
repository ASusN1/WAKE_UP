import os
import tkinter as tk

import UI_sticky_notes
import brain_dump_note
import store_note

PANEL_BG = "#f4f0e8"
PANEL_BORDER = "#d4c8b8"
ACTION_BG = "#d7cc67"
ACTION_FG = "#2f2a23"
ACTION_ACTIVE_BG = "#c6bc57"

#Check note type for sticky note or brain dump note --> 0 for sticky note, 1 for brain dump note
def note_type_from_key(note_key):
	return 0 if note_key == "sticky" else 1


# Get the exiting saved data for each notes
def open_note(note_key, mode, file_path="notes.json"):
	if note_key == "sticky":
		UI_sticky_notes.StickyNotes(mode=mode, file_path=file_path).run()
	else:
		brain_dump_note.BrainDumpNote(mode=mode, file_path=file_path).run()

# Check for saved notes; if none exist, there is nothing to load.
def list_saved_note_files(note_type):
	directory = store_note.get_note_directory(note_type)
	if not os.path.isdir(directory):
		return []

	files = [name for name in os.listdir(directory) if name.lower().endswith(".json")]
	files.sort()
	return files


# Close the current note-mode panel if it exists on the parent window
def destroy_mode_panel(parent_window):
	existing = getattr(parent_window, "note_mode_panel", None)
	if existing is not None and existing.winfo_exists():
		existing.destroy()
		setattr(parent_window, "note_mode_panel", None)


# Open the most recently saved note for the selected note type
def open_latest_note(note_key, status_var):
	note_type = note_type_from_key(note_key)
	saved_files = list_saved_note_files(note_type)
	if not saved_files:
		status_var.set("No saved notes yet.")
		return
	open_note(note_key, mode="load", file_path=saved_files[-1])


# Show the menu panel that lets the user create, load, or reopen notes.
def open_note_with_mode(parent_window, note_key):
	destroy_mode_panel(parent_window)

	note_type = note_type_from_key(note_key)
	saved_files = list_saved_note_files(note_type)
	note_label = "Sticky Notes" if note_key == "sticky" else "Brain Dump"
	status_var = tk.StringVar(master=parent_window, value=f"{note_label}: choose an action")

	panel = tk.Frame(parent_window, bg=PANEL_BG, bd=1, relief="solid", highlightthickness=1, highlightbackground=PANEL_BORDER)
	panel.place(relx=0.5, rely=0.83, anchor="center")
	setattr(parent_window, "note_mode_panel", panel)

	header = tk.Frame(panel, bg=PANEL_BG)
	header.pack(fill="x", padx=14, pady=(10, 0))

	tk.Label(header, text=note_label, bg=PANEL_BG, fg="#4d4033", font=("Arial", 11, "bold")).pack(side="left")
	tk.Button(header, text="X", width=3, command=lambda: destroy_mode_panel(parent_window)).pack(side="right")

	action_row = tk.Frame(panel, bg=PANEL_BG)
	action_row.pack(padx=14, pady=(8, 8))

	# Load the note selected in the list box.
	def load_selected(list_box):
		selection = list_box.curselection()
		if not selection:
			status_var.set("Select a saved file first.")
			return
		selected_file = list_box.get(selection[0])
		destroy_mode_panel(parent_window)
		open_note(note_key, mode="load", file_path=selected_file)

	load_area = tk.Frame(panel, bg=PANEL_BG)

	# Show or hide the saved-file picker inside the mode panel.
	def toggle_load_area():
		if not saved_files:
			status_var.set("No saved notes yet. Use Create.")
			return

		if load_area.winfo_ismapped():
			load_area.pack_forget()
			status_var.set(f"{note_label}: choose an action")
			return

		for child in load_area.winfo_children():
			child.destroy()

		list_box = tk.Listbox(load_area, width=34, height=5)
		list_box.pack(side="left", padx=(0, 8))
		for name in saved_files:
			list_box.insert(tk.END, name)
		list_box.selection_set(0)

		load_btn_col = tk.Frame(load_area, bg=PANEL_BG)
		load_btn_col.pack(side="left", fill="y")
		tk.Button(load_btn_col, text="Open", width=8, command=lambda: load_selected(list_box)).pack(pady=(0, 4))
		tk.Button(load_btn_col, text="Hide", width=8, command=lambda: load_area.pack_forget()).pack()

		load_area.pack(padx=14, pady=(0, 6))
		status_var.set("Pick a saved note and click Open.")
		list_box.bind("<Double-Button-1>", lambda _event: load_selected(list_box))

	tk.Button(action_row, text="Create", width=10, bg=ACTION_BG, fg=ACTION_FG, activebackground=ACTION_ACTIVE_BG, activeforeground=ACTION_FG, relief="flat", bd=0, command=lambda: (destroy_mode_panel(parent_window), open_note(note_key, mode="create"))).pack(side="left", padx=4)
	tk.Button(action_row, text="Load", width=10, bg=ACTION_BG, fg=ACTION_FG, activebackground=ACTION_ACTIVE_BG, activeforeground=ACTION_FG, relief="flat", bd=0, command=toggle_load_area).pack(side="left", padx=4)
	tk.Button(action_row, text="Latest", width=10, bg=ACTION_BG, fg=ACTION_FG, activebackground=ACTION_ACTIVE_BG, activeforeground=ACTION_FG, relief="flat", bd=0, command=lambda: open_latest_note(note_key, status_var)).pack(side="left", padx=4)
	tk.Button(action_row, text="Cancel", width=10, bg=ACTION_BG, fg=ACTION_FG, activebackground=ACTION_ACTIVE_BG, activeforeground=ACTION_FG, relief="flat", bd=0, command=lambda: destroy_mode_panel(parent_window)).pack(side="left", padx=4)

	tk.Label(panel, textvariable=status_var, bg=PANEL_BG, fg="#6a5b4f", font=("Arial", 9)).pack(pady=(0, 10), padx=14)
