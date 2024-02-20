from flask import Flask
from app import routes

app = Flask(__name__)

# Register your routes
app.register_blueprint(routes.main)
# app.register_blueprint(routes.home)
# app.register_blueprint(routes.about)
# app.register_blueprint(routes.contact)

if __name__ == '__main__':
    app.run(debug=True)
