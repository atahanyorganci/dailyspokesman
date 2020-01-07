from flask import Flask

app = Flask(__name__)

from newsapp import routes
