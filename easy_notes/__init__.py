from flask import Flask, render_template

from . import notes

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('index.html', all_notes={"notes": notes.all_notes_generator()})
        #return render_template('index.html', all_notes={"notes": "d"})

    return app
