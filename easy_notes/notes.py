from . import path
import markdown


def all_notes_generator():
    return path.NOTES.glob("*.md")


def get_note_title(note_name):
    return note_name[: len(note_name) - len(".md")]


def get_note_body(note_name):
    with open(path.NOTES / note_name, mode="r") as f:
        text = f.read()
    md = markdown.Markdown()
    body_html = md.convert(text)
    return body_html
