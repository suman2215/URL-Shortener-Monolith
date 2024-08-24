from flask import request, redirect
from flask_restful import Resource
from models import URLModel
from cache import set_cache, cache_response
from config import Config

class URLShortener(Resource):
    def post(self):
        original_url = request.json['url']
        short_id = URLModel.generate_short_id()
        URLModel.save_url_mapping(original_url, short_id)
        set_cache(short_id, original_url)
        return {"shortened_url": Config.BASE_URL + short_id}, 201

class URLRedirect(Resource):
    @cache_response
    def get(self, short_id):
        original_url = URLModel.get_original_url(short_id)
        if original_url:
            return redirect(original_url)
        return {"message": "URL not found"}, 404
