
from flask import Flask, render_template
from config import Config

def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('error.html'), 500

app = Flask(__name__)
app.config.from_object(Config)
app.register_error_handler(500, page_not_found)

from app import routes