from enum import IntEnum
from flask_restful import Api
from functools import wraps
from werkzeug.exceptions import HTTPException
from os import environ


def initialize_resources(application):
    api = Api(application)

    # Endpoints
    from resources.author import AuthorResource
    from resources.author import AuthorDetailResource
    from resources.book import BookResource
    from resources.book import BookDetailResource

    api.add_resource(AuthorResource, '/api/author')
    api.add_resource(AuthorDetailResource, '/api/author/<param>')
    api.add_resource(BookResource, '/api/book')
    api.add_resource(BookDetailResource, '/api/book/<param>')

class HttpCode(IntEnum):
    Ok = 200
    BadRequest = 400
    Unauthorized = 401
    Forbidden = 403
    NotFound = 404
