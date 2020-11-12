from flask import Flask
from wsgiref.simple_server import make_server
app = Flask(__name__)

@app.route('/api/v1/hello-world-6')
def hello_world():
    return 'Hello, World 6!'

with make_server('',228,app)as server:
    print("Port 127.0.0.1:228")

    server.serve_forever()