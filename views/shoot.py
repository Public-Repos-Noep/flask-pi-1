# coding=utf-8
import io
from flask import Blueprint, render_template, Response, request
# from camera.camera_pi import Camera
from camera.camera_dummy import Camera

blueprint = Blueprint('shoot', __name__, template_folder='templates')


#  사진찍기 웹 뷰
@blueprint.route('/', methods=['GET'])
def shoot():
    print('/camera/shoot')
    return render_template('shoot.html')


#  사진찍기 웹 뷰에서 요청하는 사진찍기
@blueprint.route('/feed', methods=['GET'])
def feed():
    frame = getframe(Camera())
    return Response(frame
                    , mimetype='multipart/x-mixed-replace; boundary=frame')


@blueprint.route('/upload', methods=['POST'])
def upload():
    data = dict(request.form)
    imagesave(data['data'][0].split(",")[1], 'test.png')
    return 'success', 200


def getframe(camera):
    frame = camera.get_frame()
    filesave(frame, 'temp.jpg')
    return (b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


def filesave(frame, name):
    with open(name, 'wb') as f:
        f.write(frame)
    print 'file saved'
    return True


def imagesave(frame, name):
    with open(name, 'wb') as f:
        f.write(frame.decode('base64'))
    print 'iamge saved'
    return True
