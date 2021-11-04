import json

from flask import Flask

#配置对象方式加载配置信息
class DefaultConfig(object):
    """
    默认配置
    """
    SECRET_KEY = 'ahsdhjkahdjha2544564654'

#继承复用
class DevementConfig(DefaultConfig):
    DEBUG = True

#进行封装
def creat_flask_app(config):
    app = Flask(__name__, static_url_path='/s', static_folder='static_files')
    app.config.from_object(config)

#设置
    app.config.from_envvar('PROJECT_SETTING')
    return app

app = creat_flask_app(DefaultConfig)

#定义视图
@app.route('/')
def route_map():
    """
    主视图，返回所有视图网址
    :return:
    """
    rules_iterator = app.url_map.iter_rules()
    return json.dumps(({rule.endpoint: rule.rule for rule in rules_iterator}))


# print(app.url_map)

# for rule in app.url_map.iter_rules():
#     print("name={}, payh={}".format(rule.endpoint, rule.rule))


# if __name__ == '__main__':
#     app.run()
