from flask import Flask
from flask import jsonify


app = Flask(__name__)

@app.route('/')
def get_json():
    json_dict = {
        "user_id": 10,
        "user_name": 'dkj'
    }
    return jsonify(json_dict)


if __name__ == '__main__':
    app.run()