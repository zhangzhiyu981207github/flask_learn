from flask import Flask, current_app
from flask import session, request, abort, g
# 注册蓝图
from passport import bp
app = Flask(__name__)
# 模拟redis_cli
app.redis_cli = 'redis client'
app.register_blueprint(bp)

if __name__ == '__main__':
    app.run()