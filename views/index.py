from flask import Blueprint, render_template

blueprint = Blueprint('index', __name__, template_folder='templates')


@blueprint.route('/', methods=['GET'])
def index():
    # return render_template('views/../templates/index.html')
    return 'index'
