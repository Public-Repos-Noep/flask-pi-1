#2016-2 소프트웨어 특강

## 모듈1 스티커사진 부스

## 실행 테스트
    
    python __init__.py
    
## 웹 더미 모듈 설정방법

    views/cam.py
        from camera.camera_pi import Camera
        from camera.camera_dummy import Camera
    
    두 모듈을 필요에 따라 취사선택하여 사용하면 된다
    
