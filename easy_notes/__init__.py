from flask import Flask, render_template

from . import notes


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return render_template(
            "index.html", all_notes={"notes": notes.all_notes_generator()}
        )

    @app.route("/notes/<note_name>")
    def notes_page(note_name):
        note = {
            "title": notes.get_note_title(note_name),
            "body": notes.get_note_body(note_name),
        }
        return render_template("note.html", note=note)

    return app
