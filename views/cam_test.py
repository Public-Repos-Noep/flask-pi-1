from flask import Blueprint, render_template, Response

blueprint = Blueprint('camera', __name__, template_folder='templates')


@blueprint.route('/', methods=['GET'])
def camera():
    return render_template('camera.html')


@blueprint.route('/feed', methods=['GET'])
def feed():
    print('/camera/feed')
    # camera = Camera()
    # return Response(gen(camera)
    #                 ,mimetype='multipart/x-mixed-replace; boundary=frame')
    return 'feed'


@blueprint.route('/shoot', methods=['GET'])
def shoot():
    print('/camera/shoot')
    # ca = Camera()
    # return Response(capture(ca)
    #                 , mimetype='multipart/x-mixed-replace; boundary=frame')
    return 'shoot'


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


def capture(camera):
    frame = camera.get_frame()
    yield (b'--frame\r\n'
           b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
