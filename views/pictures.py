from flask import Blueprint, render_template

blueprint = Blueprint('pictures', __name__, template_folder='templates')


@blueprint.route('/', methods=['GET'])
def pictures():
    return render_template('pictures.html')
