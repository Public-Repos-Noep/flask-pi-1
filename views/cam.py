from flask import Blueprint, render_template, Response
from camera.camera import Camera

blueprint = Blueprint('camera', __name__, template_folder='templates')


@blueprint.route('/', methods=['GET'])
def camera():
    return render_template('camera.html')


@blueprint.route('/feed', methods=['GET'])
def feed():
    camera = Camera()
    return Response(gen(camera)
                    ,mimetype='multipart/x-mixed-replace; boundary=frame')


@blueprint.route('/shoot', methods=['GET'])
def shoot():
    camera = Camera()
    return Response(capture(camera)
                    , mimetype='multipart/x-mixed-replace; boundary=frame')


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


def capture(camera):
    frame = camera.get_frame()
    yield (b'--frame\r\n'
           b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
