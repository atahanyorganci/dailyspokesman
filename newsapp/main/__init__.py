from flask import Blueprint

bp = Blueprint("main", __name__)

from newsapp.main import routes
