import json
import os

def save_notes(board_title_var, notes, priority=None, file_path="notes.json"):

    stuff_need_to_save = {
        "board_title": board_title_var.get(),
        "priority": priority,
        "notes": [],
    }

    for note in notes:
        row = note.get("row")
        check_btn = note.get("check_btn")
        check_var = note.get("check_var")
        entry = note.get("entry")

        note_info = {
            "row": str(row) if row is not None else "",
            "check_btn": str(check_btn) if check_btn is not None else "",
            "check_var": int(check_var.get()) if check_var is not None else 0,
            "entry": entry.get() if entry is not None else "",
        }
        stuff_need_to_save["notes"].append(note_info)

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(stuff_need_to_save, file, indent=2)


def load_notes(file_path="notes.json"):
    """Load raw saved JSON data if available."""
    if not os.path.exists(file_path):
        return None

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except (OSError, json.JSONDecodeError):
        return None
