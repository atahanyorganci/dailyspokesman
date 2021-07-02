from flask import render_template

from newsapp.errors import bp
from newsapp.errors.descriptions import DESCRIPTIONS


@bp.app_errorhandler(400)
def bad_request(error):
    return render_template('error.html', error=DESCRIPTIONS[404]), 400


@bp.app_errorhandler(404)
def not_found_error(error):
    return render_template('error.html', error=DESCRIPTIONS[404]), 404


@bp.app_errorhandler(500)
def internal_error(error):
    return render_template('error.html', error=DESCRIPTIONS[404]), 500
