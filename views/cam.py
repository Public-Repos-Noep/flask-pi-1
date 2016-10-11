# coding=utf-8
import io
from flask import Blueprint, render_template, Response
from camera.camera_pi import Camera
#from camera.camera_dummy import Camera

blueprint = Blueprint('camera', __name__, template_folder='templates')


#  카메라 메인 웹 뷰
@blueprint.route('/', methods=['GET'])
def camera():
    return render_template('camera.html')


#  카메라 메인에서 요청하는 미리보기 스트리밍
@blueprint.route('/feed', methods=['GET'])
def feed():
    print('/camera/feed')
    camera = Camera()
    return Response(stream(camera)
                    , mimetype='multipart/x-mixed-replace; boundary=frame')




#스트리밍 출력
def stream(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


