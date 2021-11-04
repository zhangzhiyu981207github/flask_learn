from flask import Flask, make_response

app = Flask(__name__)


@app.route('/')
def demo():
    # return '状态码为 666'
    # return '状态码为 666', 666
    # return '状态码为 666', 666, [('Itcast', 'Python')]
    return '状态码为 666', 666, {'Itcast': 'Python'}

@app.route('/demo4')
def demo4():
    resp = make_response('make response测试')
    resp.headers['Itcast'] = 'Python'
    resp.status = "404 not found"
    return resp



if __name__ == '__main__':
    app.run()