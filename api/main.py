from flask import Flask
from flask_caching import Cache
from products import product

config = {
    "DEBUG": True,
    "CACHE_TYPE": "SimpleCache",
    "CACHE_DEFAULT_TIMEOUT": 60
}
app = Flask(__name__)

app.config.from_mapping(config)
cache = Cache(app)

app.register_blueprint(product)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
