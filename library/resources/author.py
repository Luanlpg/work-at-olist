from flask import request
from flask_restful import Resource

from models.author import AuthorModel


class AuthorResource(Resource):
    """
    Authors endpoint.
    """

    def _list_author(self):
        """
        Method that lists all authors.
        Returns a list.
        """
        authors = AuthorModel.list_all()
        return list(map(lambda author: {
            'id': author.id,
            'name': author.name
            }, authors))

    def get(self):
        """
        Method that lists all authors.
        Returns a list.
        """
        try:
            return self._list_author()
        except Exception as e:
            return f"{e}", 500

    def post(self):
        """
        Method that register the author.
        Returns a string.
        """
        item = request.get_json() if request.get_json() else request.form
        try:
            if item:
                model = AuthorModel()
                model.name = item['name']
                model.save()
                return 'Created', 201
            else:
                return 'Not created, invalid payload', 400
        except Exception as e:
            return f"{e}", 500


class AuthorDetailResource(Resource):
    """
    Individual endpoint of authors.
    """

    def _get_author(self, param):
        """
        Method that selects author, by name or by id.
        Returns a list or a dict depending on the input parameter.
        """
        # case if integer is id
        if param.isnumeric():
            author = AuthorModel.get_by_id(param)
            if author is None:
                return {'message': 'Author not found'}, 404
            return {
            'id': author.id,
            'name': author.name
            }
        else:
            authors = AuthorModel.filter_by_name(param)
            if authors is None:
                return {'message': 'Author not found'}, 404
            return list(map(lambda author: {
                'id': author.id,
                'name': author.name
                }, authors))




    def get(self, param):
        """
        Method that selects author, by name or by id.
        Returns a list or a dict depending on the input parameter.
        """
        try:
            return self._get_author(param)

        except Exception as e:
            return f"{e}", 500

    def put(self, param):
        """
        Method editing author.
        Returns a string.
        """
        item = request.get_json() if request.get_json() else request.args
        try:
            if item:
                model = AuthorModel()
                # case if numeric is id
                if param.isnumeric():
                    model = AuthorModel.get_by_id(param)
                else:
                    model = AuthorModel.get_by_name(param)
                model.name = item['name']
                model.save()
                return 'Edited', 204
            else:
                return 'Unedited, invalid payload', 400
        except Exception as e:

            return f"{e}", 500

    def delete(self, param):
        """
        Method that removes author.
        Returns a string.
        """
        try:
            # case if numeric is id
            if param.isnumeric():
                author = AuthorModel.get_by_id(param)
            else:
                author = AuthorModel.get_by_name(param)
            author.delete()
            return 'No Content', 204
        except Exception as e:
            return f"{e}", 500
