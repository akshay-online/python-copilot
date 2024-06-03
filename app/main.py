from flask import Flask
from routes.account_routes import account_routes
from routes.transaction_routes import transaction_routes
from routes.loans_routes import loans_routes
from routes.offer_routes import offer_routes
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

app.route('/')
def home():
    return "Welcome to the Banking API!"
# Register account routes
app.register_blueprint(account_routes)

# Register transaction routes
app.register_blueprint(transaction_routes)

app.register_blueprint(loans_routes)

app.register_blueprint(offer_routes)

if __name__ == "__main__":
    app.run()