from flask import Blueprint, render_template

blueprint = Blueprint('index', __name__,
                      template_folder='templates',
                      static_folder='static')


@blueprint.route('/', methods=['GET'])
def index():
    return render_template('index.html')
