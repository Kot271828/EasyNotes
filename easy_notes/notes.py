from . import path
import markdown


def all_notes_generator():
    return path.NOTES.glob("*.md")


def get_note_title(note_name):
    return note_name[: len(note_name) - len(".md")]


def get_note_body(note_name):
    with open(path.NOTES / note_name, mode="r", encoding="utf8") as f:
        text = f.read()
    # extension は次を参照
    # https://facelessuser.github.io/pymdown-extensions/
    md = markdown.Markdown(
        extensions=[
            "pymdownx.superfences",
            "pymdownx.inlinehilite",
            "pymdownx.highlight",
            "pymdownx.tasklist",
            "tables",
        ]
    )
    # md = markdown.Markdown()
    body_html = md.convert(text)
    return body_html
