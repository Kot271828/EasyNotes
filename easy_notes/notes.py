

from . import path

def all_notes_generator():
    return path.NOTES.glob("*.md")

