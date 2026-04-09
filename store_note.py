import json
import os

#This will update where the user will save their note data for easier finding.
def get_note_directory(note_type):
    if note_type == 0:  
        directory = "sticky_note_data"
    elif note_type == 1:
        directory = "brain_dump_data"
    else:     #Will update the feature later ( 1 specical notes ? , like a creator notes for somt? )
        directory = "other_stuff_data"  # Default to sticky notes
    
    # Create directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    return directory


def get_note_file_path(note_type, file_path="notes.json"):
    directory = get_note_directory(note_type)
    return os.path.join(directory, file_path)


def _sanitize_filename(text):
    clean_chars = []
    for char in (text or "").strip():
        if char.isalnum() or char in ("-", "_", " "):
            clean_chars.append(char)
    return "".join(clean_chars).strip().replace(" ", "_")


def unique_name(title_text, note_type=0, initial_title="", extension=".json"):
    directory = get_note_directory(note_type)
    cleaned_title = _sanitize_filename(title_text)
    cleaned_initial = _sanitize_filename(initial_title)

    use_initial_counter = (not cleaned_title) or ((title_text or "").strip() == (initial_title or "").strip())

    if use_initial_counter:
        base_name = cleaned_initial or "note"
        index = 0
        while True:
            candidate = f"{base_name}_{index}{extension}"
            if not os.path.exists(os.path.join(directory, candidate)):
                return candidate
            index += 1

    candidate = f"{cleaned_title}{extension}"
    if not os.path.exists(os.path.join(directory, candidate)):
        return candidate

    suffix = 1
    while True:
        candidate = f"{cleaned_title}_{suffix}{extension}"
        if not os.path.exists(os.path.join(directory, candidate)):
            return candidate
        suffix += 1


def save_notes(board_title_var, notes, priority=None, note_type=0, file_path="notes.json"):
    title_value = board_title_var.get() if board_title_var is not None and hasattr(board_title_var, "get") else ""

    if file_path == "notes.json":
        file_path = unique_name(title_value, note_type=note_type, initial_title="Today's Focus")

    # Get the correct directory based on note type
    file_path_abs = get_note_file_path(note_type, file_path)

    stuff_need_to_save = {
        "board_title": title_value,
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

    with open(file_path_abs, "w", encoding="utf-8") as file:
        json.dump(stuff_need_to_save, file, indent=2)

    return file_path


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
def save_brain_dump_note(board_title_var, brain_dump_notes, note_type=1, file_path="notes.json"):
    title_value = board_title_var.get() if board_title_var is not None and hasattr(board_title_var, "get") else ""

    if file_path == "notes.json":
        file_path = unique_name(title_value, note_type=note_type, initial_title="Brain Dump Note")

    # Get the correct directory based on note type
    file_path_abs = get_note_file_path(note_type, file_path)

    saved_data_bd = load_notes(file_path=file_path_abs)
    if not isinstance(saved_data_bd, dict):
        saved_data_bd = {}

    paragraph = ""
    if brain_dump_notes:
        paragraph_widget = brain_dump_notes[0].get("paragraph")
        if paragraph_widget is not None:
            paragraph = paragraph_widget.get("1.0", "end-1c")

    saved_data_bd["brain_dump_note"] = paragraph

    saved_data_bd["brain_dump_title"] = title_value

    with open(file_path_abs, "w", encoding="utf-8") as file:
        json.dump(saved_data_bd, file, indent=2)

    return file_path


def load_saved_note_data(note_type=0, file_path="notes.json"):
    file_path = get_note_file_path(note_type, file_path)
    saved_data = load_notes(file_path=file_path)
    if not isinstance(saved_data, dict):
        return {}
    return saved_data


def load_brain_dump_note(note_type=1, file_path="notes.json"):
    saved_data_bd = load_saved_note_data(note_type=note_type, file_path=file_path)
    if not isinstance(saved_data_bd, dict):
        return ""
    return saved_data_bd.get("brain_dump_note") or ""
