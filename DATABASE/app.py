from flask import Flask
from sqlalchemy.orm.exc import NoResultFound
from flask_jwt_extended import JWTManager

from blueprint import api_blueprint

def server_error():
    return jsonify(
        {
            "code": 500,
            "type": "server_error",
        }
    )



DEBUG = True
app = Flask(__name__)

app.register_blueprint(api_blueprint, url_prefix="/api/store")

#app.register_error_handler(Exception, server_error)


app.config['JWT_SECRET_KEY'] = '841B865EB87E8EC40281F72F4A8B8690219C1784BA16AEF0408DC712A6F3B4D3'
jwt = JWTManager(app)

if __name__ == '__main__':
    app.run(debug=True)
    

