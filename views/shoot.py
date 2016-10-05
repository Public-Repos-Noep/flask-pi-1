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
    camera = Camera()

    return Response(getframe(camera)
                    , mimetype='multipart/x-mixed-replace; boundary=frame')





#단일 출력
def getframe(camera):
    frame = camera.get_frame()
    #todo filesave는 멀티파트로 입력받을때
    #filesave(frame)
    return (b'--frame\r\n'
           b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


def filesave(frame):
    with open('temp.jpeg', 'wb'):
        file.write(frame)
    print 'file saved'
    return True

