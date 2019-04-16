from flask import Flask
from flask import render_template
app = Flask(__name__)
import os
APP_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_PATH = os.path.join(APP_PATH,"../front-end")


@app.route("/")
def indexWebsite():
	return "Hello World!"
