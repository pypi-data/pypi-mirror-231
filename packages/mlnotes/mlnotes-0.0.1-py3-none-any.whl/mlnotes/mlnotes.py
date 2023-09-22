import json

# Load existing notes from "ai_info.json" if it exists
try:
    with open("ai_info.json", "r") as f:
        notes = json.load(f)
except FileNotFoundError:
    notes = {}

def add_notes(note_no, note):
    # Update the notes dictionary with the new note
    notes[note_no] = note

    # Save the updated notes dictionary to "ai_info.json"
    with open("ai_info.json", "w") as f:
        json.dump(notes, f)

def show_notes(note_no = None):
    try:
        with open("ai_info.json", "r") as f:
            notes = json.load(f)
        
        if note_no is not None:
            return notes.get(note_no)
        else:
            return notes
    except FileNotFoundError:
        return {} if note_no is None else None