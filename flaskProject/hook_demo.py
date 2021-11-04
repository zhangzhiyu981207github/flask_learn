from flask import Flask, request, abort, current_app, g, make_response

app = Flask(__name__)


# 请求钩子(尝试判断用户的身份， 对于未登录的用户不做处理， 放行) (用g对象保存用户身份信息：g.user_id=123, g.user_id= None)
@app.before_request
def authentication():
    user_id = request.cookies.get('user_id')
    if user_id:
        g.user_id = user_id
    else:
        g.user_id = None


# 强制登陆的装饰器
def login_required(func):
    def wrapper(*args, **kwargs):
        # 判断用户是否登录
        if g.user_id is None:
            abort(401)  # 没有经过认证的意思
        else:
            # 已登录
            return func(*args, **kwargs)

    return wrapper


# 普通视图视图
@app.route('/')
def index():
    return f'home page user_id={g.user_id}'


# 强制登录视图
@app.route('/profile')
@login_required
def get_user_profile():
    return f'user profile page user_id={g.user_id}'


# 模拟登录
@app.route('/login')
def set_cookie():
    resp = make_response('set cookie ok')
    # resp.set_cookie('cookie名字', 'cookie值', max_age=有效时间)
    resp.set_cookie('user_id', '123456', max_age=3600)  # 设置有效期
    return resp


if __name__ == '__main__':
    app.run()


