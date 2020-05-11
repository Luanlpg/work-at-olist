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

    api.add_resource(AuthorResource, '/api/author')
    api.add_resource(AuthorDetailResource, '/api/author/<param>')

class HttpCode(IntEnum):
    Ok = 200
    BadRequest = 400
    Unauthorized = 401
    Forbidden = 403
    NotFound = 404
