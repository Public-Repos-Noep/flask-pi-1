from flask import Blueprint

blueprint = Blueprint('blue', __name__, template_folder='templates')


@blueprint.route('/')
def show():
    return 'blue'
