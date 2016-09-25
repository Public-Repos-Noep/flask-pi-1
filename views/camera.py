from flask import Blueprint, render_template

blueprint = Blueprint('camera', __name__, template_folder='templates')


@blueprint.route('/', methods=['GET'])
def camera():
    return render_template('camera.html')
