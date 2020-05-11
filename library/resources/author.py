from flask import request, jsonify
from flask_restful import Resource
from models.author import AuthorModel
from datetime import date, datetime


class AuthorResource(Resource):

    def _list_author(self):
        authors = AuthorModel.list_all()

        return list(map(lambda author: {
            'id': author.id,
            'name': author.name
            }, authors))

    def get(self):
        try:
            return self._list_author()
        except Exception as e:
            return f"{e}", 500
