from flask import *

app = Flask(__name__)

@app.route("/")
def testing():
    return render_template('FlaskDeploy1.html')


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')