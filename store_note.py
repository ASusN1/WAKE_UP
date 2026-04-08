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
    if not os.path.exists(file_path):
        return None

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except (OSError, json.JSONDecodeError):
        return None


#store the paragrpah and the title of the brain dump notes 
#
def save_brain_dump_note(board_title_var, brain_dump_notes, file_path="notes.json"):
    saved_data_bd = load_notes(file_path=file_path)
    if not isinstance(saved_data_bd, dict):
        saved_data_bd = {}

    paragraph = ""
    if brain_dump_notes:
        paragraph_widget = brain_dump_notes[0].get("paragraph")
        if paragraph_widget is not None:
            paragraph = paragraph_widget.get("1.0", "end-1c")

    saved_data_bd["brain_dump_note"] = paragraph

    if board_title_var is not None and hasattr(board_title_var, "get"):
        saved_data_bd["brain_dump_title"] = board_title_var.get()

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(saved_data_bd, file, indent=2)


def load_brain_dump_note(file_path="notes.json"):
    saved_data_bd = load_notes(file_path=file_path)
    if not isinstance(saved_data_bd, dict):
        return ""
    return saved_data_bd.get("brain_dump_note") or ""

#def unique_stored_note_id():