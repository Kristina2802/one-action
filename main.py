from flask import Flask, render_template, request, make_response
import datetime as dt

app = Flask(__name__)


@app.route('/')

@app.route('/index', methods=['POST', 'GET'])

def index():
    answer = ""
    resp = make_response(render_template('index.html'))
    if (request.method == 'POST'):
        a = float(request.form['select'])
        delta_time = dt.timedelta(hours=a)
        answer = str((dt.datetime.now() + delta_time).strftime("%d-%m-%Y %H:%M:%S"))
    return render_template('index.html', answer=answer)

if __name__ == "__main__":
    app.run()