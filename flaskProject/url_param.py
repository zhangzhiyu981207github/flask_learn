from flask import Flask, request, abort
from werkzeug.routing import BaseConverter

app = Flask(__name__)


@app.route('/user/<int:user_id>')
def user_info(user_id):
    print(type(user_id))
    return 'hello {}'.format(user_id)


class MobileConverter(BaseConverter):
    """
    用正则表达式制定手机号格式
    """
    regex = r'1[3-9]\d{9}'


app.url_map.converters['mobile'] = (MobileConverter)

@app.route('/sms/<mobile:phone>')
def get_phone(phone):
    return "my phone is {}".format(phone)


@app.route('/articles')
def get_articles():
    channel_id = request.args.get('channel_id')
    if channel_id is None:
        abort(400)  #400 Bad Request
    return 'your articles is {}'.format(channel_id)

if __name__ == '__main__':
    app.run()




