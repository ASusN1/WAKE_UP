import json

def save_notes(notes):
    data = []
    for item in notes: 
        text = item["note_entry"].get()
        check_btn = item ["check_btn"].get()
        data.append({
            "text": text,
            "check_btn": check_btn
        })

        with open("notes.json", "w") as f:
        json.dump(data, f)

def load_notes(box, notes):
    try:
        with open("notes.json", "r") as f:
            data = json.load(f)

        for note in data:
            add_note(box, notes)

            notes[-1]["entry"].insert(0, note["text"])
            notes[-1]["check_var"].set(note["checked"])

    except FileNotFoundError:
        pass  # first time running, no file yet

#when the user like reopen the app after writgint the stickky node, when click on the sticky node list ( )
load_notes(box, notes)