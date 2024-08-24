from functools import wraps
from flask import redirect
import memcache
from config import Config

cache = memcache.Client(Config.MEMCACHED_SERVER, debug=0)

def set_cache(key, value, time=300):
    try:
        cache.set(key, value, time)
    except Exception as e:
        raise Exception("Failed to set cache") from e

def get_cache(key):
    try:
        return cache.get(key)
    except Exception as e:
        raise Exception("Failed to get cache") from e

def cache_response(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        short_id = kwargs.get('short_id')
        cached_url = get_cache(short_id)
        if cached_url:
            return redirect(cached_url)

        response = func(*args, **kwargs)

        if response.status_code == 302:  # HTTP status code for redirection
            set_cache(short_id, response.headers['Location'])

        return response

    return wrapper

def check_memcached_connection():
    try:
        # Set and get a test value to check if Memcached is accessible
        cache.set('test', 'connection')
        if cache.get('test') == 'connection':
            return True
        return False
    except Exception as e:
        print(f"Memcached Connection Error: {e}")
        return False
