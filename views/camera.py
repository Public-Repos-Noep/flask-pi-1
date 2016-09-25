from flask import Blueprint, render_template, Response
import camera

blueprint = Blueprint('camera', __name__, template_folder='templates')


@blueprint.route('/', methods=['GET'])
def camera():
    return render_template('camera.html')


@blueprint.route('/feed', methods=['GET'])
def feed():
    return Response(gen(camera.Camera()),mimetype='multipart/x-mixed-replace; boundary=frame')


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')



