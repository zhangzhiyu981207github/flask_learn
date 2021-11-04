from flask import Flask, make_response, request,session

app = Flask(__name__)

# class DefaultConfige(object):
#     SECRET_KEY = 'fdjasfkljaskl'
#
# app.config.from_object(DefaultConfige)
"""或者"""
app.secret_key='fdjasfkljaskl'

# @app.route('/')
# def set_cookie():
#     resp = make_response('set cookie ok')
#     resp.set_cookie('username', 'itcast', max_age=36000)
#     return resp
#
# @app.route('/get_cookie')
# def get_cookie():
#     resp = request.cookies.get('username')
#     return resp
#
# @app.route('/delete_cookie')
# def delete_cookie():
#     resp = make_response('hello world')
#     resp.delete_cookie('username')
#     return  resp


@app.route('/set_session')
def set_cookie():
    session['username'] = 'zzy'
    return 'set session ok'


@app.route('/get_session')
def get_session():
    username = session.get('username')
    return 'get session username {}'.format(username)



if __name__ == '__main__':
    app.run()