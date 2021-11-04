from flask import Flask, render_template
from flask import redirect

app = Flask(__name__)

@app.route('/demo')
def home():
    mint = 123454
    mstr = 'hello'

    data = dict(
        my_int=123,
        my_str='asdja'
    )
    # return render_template('index.html', **data)
    return render_template('index.html', my_int=123, my_str='asjdkhfjk')


if __name__ == '__main__':
    app.run()