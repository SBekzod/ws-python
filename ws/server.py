from flask import Flask
app = Flask(__name__)


@app.route("/", methods=['GET'])
def home_enter():
    print('user connected on home')
    return "<div>Hello World</div>"


@app.route("/users", methods=['GET'])
def users_list():
    print('user arrived on /users')
    return "<div>Users are here</div>"

