from flask import Flask, render_template
from views import index, pictures, test
from views import cam, shoot
app = Flask(__name__)
app.register_blueprint(index.blueprint)
app.register_blueprint(cam.blueprint, url_prefix='/camera')
app.register_blueprint(shoot.blueprint, url_prefix='/shoot')
app.register_blueprint(pictures.blueprint, url_prefix='/pictures')
app.register_blueprint(test.blueprint, url_prefix='/test')


#simple error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('error/404.html'), 404


@app.errorhandler(500)
def not_found(error):
    return render_template('error/500.html'), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)
