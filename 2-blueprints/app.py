from flask import Flask
from user.routes import user_bp

app = Flask(__name__)
app.register_blueprint(user_bp, url_prefix='/user')

if __name__ == '__main__':
    app.run(debug=True)
