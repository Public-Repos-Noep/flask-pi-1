from flask import Blueprint, render_template, Response

blueprint = Blueprint('camera', __name__, template_folder='templates')


@blueprint.route('/', methods=['GET'])
def camera():
    return render_template('camera.html')


@blueprint.route('/shoot', methods=['GET'])
def shoot():
    print('/camera/shoot')
    return render_template('shoot.html')


@blueprint.route('/feed', methods=['GET'])
def feed():
    print('/camera/feed')
    return 'feed'


@blueprint.route('/picture', methods=['GET'])
def picture():
    print 'picture'
    return 'picture'
