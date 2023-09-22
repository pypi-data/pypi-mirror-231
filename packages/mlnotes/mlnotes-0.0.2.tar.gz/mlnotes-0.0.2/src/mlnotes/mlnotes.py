import json

# Load existing notes from "ai_info.json" if it exists
try:
    with open("ai_info.json", "r") as f:
        notes = json.load(f)
except FileNotFoundError:
    notes = {}


def add_notes(note_no, note):
    # Update the notes dictionary with the new note
    if str(note_no) in notes:
        return "Note already exits"
    else:
        notes[note_no] = note

        # Save the updated notes dictionary to "ai_info.json"
        with open("ai_info.json", "w") as f:
            json.dump(notes, f)


def show_notes(note_no=None):
    try:
        with open("ai_info.json", "r") as f:
            notes_ = json.load(f)

        if note_no is not None:
            return notes_[str(note_no)]
        else:
            return notes_
    except FileNotFoundError:
        return {} if note_no is None else None