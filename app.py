from flask import Flask, jsonify
from flask_restful import Api
from flask_cors import CORS
from routes import URLShortener, URLRedirect
from werkzeug.exceptions import HTTPException
from database import check_mongodb_connection
from cache import check_memcached_connection

app = Flask(__name__)
CORS(app)
api = Api(app)

# Global error handler
@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return jsonify({"error": e.description}), e.code
    return jsonify({"error": "An unexpected error occurred"}), 500

api.add_resource(URLShortener, '/shorten')
api.add_resource(URLRedirect, '/<string:short_id>')

def check_dependencies():
    if not check_mongodb_connection():
        print("Failed to connect to MongoDB. Server is shutting down.")
        return False
    if not check_memcached_connection():
        print("Failed to connect to Memcached. Server is shutting down.")
        return False
    return True

if __name__ == '__main__':
    if check_dependencies():
        app.run(host='0.0.0.0', port=5000, debug=True)
    else:
        print("Failed to start server due to dependency issues.")
