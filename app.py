from flask import Flask, request, make_response, redirect, render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
bootstrap = Bootstrap(app)
todos = ['Comprar café', 'ir a el banco', 'Compar fruta']

@app.errorhandler(500)
def not_found_500(error):
    return render_template('500.html', error=error)

@app.errorhandler(404)
def not_found_404(error):
    return render_template('404.html', error=error)



@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response((redirect('/hello')))
    response.set_cookie('user_ip', user_ip)
    return response


@app.route('/hello')
def hello_world():
    user_ip = request.cookies.get('user_ip')
    context ={
        'user_ip': user_ip,
        'todos': todos
    }
    return render_template('hello.html', **context)


@app.route('/500_error_test')
def index_pandas():
    500


if __name__ == '__main__':
    app.run()

