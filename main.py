from flask import Flask, render_template, request, make_response
import datetime as dt
def toweb(f):
    app = Flask(__name__)

    @app.route("/", methods=['GET', 'POST'])
    def myfunc():
        about = f.__doc__
        a = f.__annotations__
        if 'return' in a:
            a.pop('return')

        if request.form:
            res = f(**request.form)
        else:
            res = None

        return render_template('index.html', about=about, a=a, res=res)

    return app

@toweb
def index(a: int) -> str:
    """
    Эта функция считает, сколько сейчас времени в каком-то часовом поясе России. Пожалуйста, введите разницу часового пояса с Москвой.
    """
    a = float(a)
    delta_time = dt.timedelta(hours=a)
    answer = str((dt.datetime.now() + delta_time).strftime("%d-%m-%Y %H:%M:%S"))
    return answer

index.run(host='0.0.0.0', port="5001")