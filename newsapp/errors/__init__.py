from flask import Blueprint

bp = Blueprint('error', __name__)

from newsapp.errors import handlers
