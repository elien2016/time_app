from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/time')
def get_time():
    return render_template("./time.html")

app.run(host='0.0.0.0',
        port=8080,
        debug=True)
