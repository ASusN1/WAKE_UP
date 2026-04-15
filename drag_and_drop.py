import os
import tkinter as tk
import store_note


def when_user_press_note(event, drag_state):
    #["start_x", "start_y"] to store the initial position of the mouse when the drag starts
    drag_state ['start_x'] = event.x 
    drag_state ['start_y'] = event.y

def when_user_dragging_note(event, widget, parent, drag_state):
    x = widget.winfo_x() + event.x - drag_state["start_x"]
    y = widget.winfo_y() + event.y - drag_state["start_y"]
    widget.place(x=x, y=y)


def when_user_release_note(_event, widget, parent, grid_size):
    x = widget.winfo_x()
    y = widget.winfo_y()
    snapped_x = (x // grid_size) * grid_size
    snapped_y = (y // grid_size) * grid_size
    max_x = max(0, parent.winfo_width() - widget.winfo_width())
    max_y = max(0, parent.winfo_height() - widget.winfo_height())
    snapped_x = max(0, min(snapped_x, max_x))
    snapped_y = max(0, min(snapped_y, max_y))
    widget.place(x=snapped_x, y=snapped_y)

#Update the draggable note so the user will be able to drag note outside the board, and when they release it outside
#snap back to the nearest grid/row
def make_dragable_note(widget, parent, grid_size=30):
    drag_state= {"start_x": 0, "start_y": 0}

    def on_drag_outside(event):
        root = widget.winfo_toplevel()
        if str(widget.place_info().get("in", "") != str(root)): 
            x = widget.winfo_rootx() -root.winfo_rootx() 
            y = widget.winfo_rooty() -root.winfo_rooty()
            widget.place(in_=root, x=x, y=y)
        
        widget.lift()
        x = widget.winfo_x() + event.x - drag_state["start_x"]
        y = widget.winfo_y() + event.y - drag_state["start_y"]

    widget.bind("<Button-1>", lambda event: when_user_press_note(event, drag_state))
    widget.bind("<B1-Motion>", lambda event: when_user_dragging_note(event, widget, parent, drag_state))
    widget.bind("<ButtonRelease-1>", lambda event: when_user_release_note(event, widget, parent, grid_size))


def _list_saved_note_files(note_type):
    directory = store_note.get_note_directory(note_type)
    if not os.path.isdir(directory):
        return []
    return sorted([name for name in os.listdir(directory) if name.lower().endswith(".json")])


def _collect_saved_note_items():
    items = []
    for note_type in (0, 1, 2):
        for file_name in _list_saved_note_files(note_type):
            items.append({"note_type": note_type, "file_name": file_name})
    return items


def show_saved_notes_on_board(board_box, visual_art_dir, on_open_note=None):
    for child in board_box.winfo_children():
        child.destroy()

    saved_note_items = _collect_saved_note_items()
    if not saved_note_items:
        tk.Label(board_box, text="No saved notes yet.", bg=board_box.cget("bg"), fg="#3d2415", font=("Arial", 16)).pack(pady=20)
        return

    notes_icon_path = {
        0: os.path.join(visual_art_dir, "sticky note.png"),
        1: os.path.join(visual_art_dir, "brain dump.png"),
        2: os.path.join(visual_art_dir, "fat_seal.png"),
    }
    text_by_type = {
        0: "Sticky Note",
        1: "Brain Dump Note",
        2: "Picture Note",
    }

    board_box.drag_icon_refs = {}
    for note_type, icon_path in notes_icon_path.items():
        try:
            board_box.drag_icon_refs[note_type] = tk.PhotoImage(file=icon_path).subsample(3, 3)
        except tk.TclError:
            board_box.drag_icon_refs[note_type] = None

    max_cols = 5
    spacing_x = 105
    spacing_y = 90
    start_x = 10
    start_y = 10

    board_box.drag_note_widgets = []
    open_note_callback = on_open_note

    for index, item in enumerate(saved_note_items):
        row, col = divmod(index, max_cols)
        x = start_x + col * spacing_x
        y = start_y + row * spacing_y

        title = os.path.splitext(item["file_name"])[0][:12]
        note_type = item["note_type"]
        label_text = f"{text_by_type.get(note_type, 'Note')}\n{title}"
        icon = board_box.drag_icon_refs.get(note_type)

        if icon is not None:
            widget = tk.Label(
                board_box,
                image=icon,
                text=label_text,
                compound="top",
                bg=board_box.cget("bg"),
                fg="#fff4d8",
                font=("Arial", 8, "bold"),
                cursor="fleur",
            )
        else:
            widget = tk.Label(
                board_box,
                text=label_text,
                bg="#f4e38b",
                fg="#4d4033",
                width=11,
                height=4,
                font=("Arial", 8, "bold"),
                cursor="fleur",
            )

        widget.place(x=x, y=y)
        make_dragable_note(widget, board_box)

        if callable(open_note_callback):
            widget.bind(
                "<Double-Button-1>",
                lambda _event, ntype=note_type, fname=item["file_name"]: open_note_callback(ntype, fname),
            )

        board_box.drag_note_widgets.append(widget)

def drag_note_outside_board(note_widget, board_box, on_open_note=None):
    note_widget.place_forget()
    if callable(on_open_note):
        on_open_note()
    