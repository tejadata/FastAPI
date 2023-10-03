from flask import Flask, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)


@app.route("/customer", methods=['POST'])
def add():
    print(1)
    with open('./customer.json') as data:
        data = json.loads(data.read())
    return json.dumps(data)


# http://localhost/api/new_user
if __name__ == '__main__':
    app.run()
