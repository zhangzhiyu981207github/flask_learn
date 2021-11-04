from flask import Flask
from flask import redirect

app = Flask(__name__)

@app.route('/demo')
def get_redir():
    return redirect('https://www.baidu.com/')



if __name__ == '__main__':
    app.run()