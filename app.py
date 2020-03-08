from flask import Flask, request, make_response, redirect, render_template


app = Flask(__name__)

todos = ['Comprar café', 'ir a el banco', 'Compar fruta']

@app.errorhandler(404)
def not_found(error):
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


if __name__ == '__main__':
    app.run()

