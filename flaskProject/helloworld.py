from flask import Flask

#配置对象方式加载配置信息
# class DefaultConfig(object):
#     """
#     默认配置
#     """
#     SECRET_KEY = 'ahsdhjkahdjha2544564654'


app = Flask(__name__, static_url_path='/s')

#设置
# app.config.from_object(DefaultConfig)
# app.config.from_pyfile('setting.py')
app.config.from_envvar('PROJECT_SETTING')

# 定义视图
@app.route("/")
def hello_world():  # put application's code here
    print(app.config['SECRET_KEY'])
    return 'Hello World!'


# @app.route("/", method=["post"])
# def view_func_1():
#     return "hello world 1"



# if __name__ == '__main__':
#     app.run()
