from flask import Flask

server = Flask(__name__)


@server.route('/')
def hello():
    return 'Hello, World!'


server.run()  # Ctrl + Shift + F10
