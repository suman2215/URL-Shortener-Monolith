import random
import string
from database import url_collection
from pymongo.errors import PyMongoError


class URLModel:
    @staticmethod
    def generate_short_id(num_of_chars=6):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=num_of_chars))

    @staticmethod
    def save_url_mapping(original_url, short_id):
        try:
            url_collection.insert_one({'original_url': original_url, 'short_id': short_id})
        except PyMongoError as e:
            raise Exception("Database insertion failed") from e

    @staticmethod
    def get_original_url(short_id):
        try:
            url_data = url_collection.find_one({'short_id': short_id})
            return url_data['original_url'] if url_data else None
        except PyMongoError as e:
            raise Exception("Database query failed") from e
