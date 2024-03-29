from flask import Flask
from gevent.wsgi import WSGIServer
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

http_server = WSGIServer(('', 5000), app)

if __name__ == "__main__":
    http_server.serve_forever()
