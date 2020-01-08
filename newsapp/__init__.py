from flask import Flask

from newsapp.config import Config

app = Flask(__name__)
app.config.from_object(Config)

from newsapp import routes
