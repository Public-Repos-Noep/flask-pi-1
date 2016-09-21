from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/camera', methods=['GET'])
def camera():
    return render_template('camera.html')


@app.route('/pictures', methods=['GET'])
def pictures():
    return render_template('pictures.html')


@app.errorhandler(404)
def not_found(error):
    return render_template('error/404.html'), 404


@app.errorhandler(500)
def not_found(error):
    return render_template('error/500.html'), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)
