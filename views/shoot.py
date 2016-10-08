# coding=utf-8
import io
from flask import Blueprint, render_template, Response
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


def getframe(camera):
    frame = camera.get_frame()
    filesave(frame)
    return (b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def filesave(frame):
    with open('temp.jpg', 'wb') as f:
        f.write(frame)
    print 'file saved'
    return True
