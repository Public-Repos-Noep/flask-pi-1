# coding=utf-8
import io
from flask import Blueprint, render_template, Response, request
import subprocess

blueprint = Blueprint('composite', __name__, template_folder='templates')

MODIFY = 'modify.png'
RESULT = 'result.png'
SHELLPATH = '/home/pi/Projects/flask-pi-1/resultcopy.sh'


#  사진합성 웹 뷰
@blueprint.route('/', methods=['GET'])
def composite():
    return render_template('composite.html')


#  사진찍기 웹 뷰에서 요청하는 사진찍기
@blueprint.route('/feed', methods=['GET'])
def feed():
    frame = getframe()
    return Response(frame
                    , mimetype='multipart/x-mixed-replace; boundary=frame')


@blueprint.route('/send', methods=['POST'])
def send():
    data = dict(request.form)
    imagesave(data['data'][0].split(",")[1], RESULT)
    imagesend()
    return 'success', 200


def getframe():
    frame = fileopen(MODIFY)
    return (b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


def fileopen(name):
    with open(name, 'rb') as f:
        print 'file loaded '
        return f.read()


def imagesave(frame, name):
    with open(name, 'wb') as f:
        f.write(frame.decode('base64'))
    print 'iamge saved '
    return True


def imagesend():
    subprocess.call(SHELLPATH)
    return True
