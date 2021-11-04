from flask import Flask
from flask import session, request, abort, g

app = Flask(__name__)


# 在第一次请求之前调用，  可以在此方法内部做一些初始化操作
@app.before_first_request
def before_first_request():
    print('before_first_request')


# 在每一次请求之前调用， 这时候已经有请求了， 可能在这个方法里面做请求的校验
# 如果请求的校验不成功， 可以直接在此方法中进行响应， 直接return之后就不会执行视图函数了
@app.before_request
def before_request():
    print('before_request')
    # if not hasattr(g, 'user'):
    #     setattr(g, 'user', 'xxxx')
    #     return '不符合条件不执行视图函数'


# 在执行完试图函数的时候调用， 并且把视图函数所生成的响应传入， 可以在此方法中对响应做最后一部统一的处理
@app.after_request
def after_request(response):
    print('after_request')
    response.headers['Content_type'] = 'application/jaon'
    return response


# 在每一次请求之后会调用， 会接受一个参数， 参数是服务器出现的错误信息
@app.teardown_request
def teardown_request(response):
    print('teardown_request')


@app.route('/index')
def index():
    print('view called')
    return 'index'

# 运行flask提供的测试服务器
if __name__ == '__main__':
     app.run()