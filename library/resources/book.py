from flask import request
from flask_restful import Resource

from models.book import BookModel
from models.author_book import AuthorBookModel


class BookResource(Resource):
    """
    Books endpoint.
    """

    def _list_book(self):
        """
        Method that lists all books.
        Returns a list.
        """
        books = BookModel.list_all()
        return list(map(lambda book: {
            'id': book.id,
            'name': book.name,
            'edition': book.edition,
            'publication_year': book.publication_year
            }, books))

    def get(self):
        """
        Method that lists all books.
        Returns a list.
        """
        try:
            return self._list_book()
        except Exception as e:
            return f"{e}", 500

    def post(self):
        """
        Method that register the book.
        Returns a string.
        """
        item = request.get_json() if request.get_json() else request.form
        try:
            if item:
                model = BookModel()
                model.name = item['name']
                model.edition = item['edition']
                model.publication_year = item['publication_year']
                model.save()
                association = AuthorBookModel()
                for author_id in item['authors']:
                    association.author_id = author_id
                    association.book_id = BookModel.get_by_name(item['name']).id
                    association.save()
                return 'Created', 201
            else:
                return 'Not created, invalid payload', 400
        except Exception as e:
            return f"{e}", 500


class BookDetailResource(Resource):
    """
    Individual endpoint of books.
    """

    def _get_book(self, param):
        """
        Method that selects book, by name or by id.
        Returns a list or a dict depending on the input parameter.
        """
        # case if integer is id
        if param.isnumeric():
            book = BookModel.get_by_id(param)
            if book is None:
                return {'message': 'Book not found'}, 404
            authors = AuthorBookModel.filter_by_book_id(book.id)
            authors = [author.author_id for author in authors]
            return {
            'id': book.id,
            'name': book.name,
            'edition': book.edition,
            'publication_year': book.publication_year,
            'authors': authors
            }
        else:
            books = BookModel.filter_by_name(param)
            if books is None:
                return {'message': 'Book not found'}, 404
            if len(books) == 1:
                book = books[0]
                authors = AuthorBookModel.filter_by_book_id(book.id)
                authors = [author.author_id for author in authors]
                return {
                'id': book.id,
                'name': book.name,
                'edition': book.edition,
                'publication_year': book.publication_year,
                'authors': authors
                }
            return list(map(lambda book: {
                'id': book.id,
                'name': book.name,
                'edition': book.edition,
                'publication_year': book.publication_year
                }, books))

    def get(self, param):
        """
        Method that selects book, by name or by id.
        Returns a list or a dict depending on the input parameter.
        """
        try:
            return self._get_book(param)

        except Exception as e:
            return f"{e}", 500

    def put(self, param):
        """
        Method editing book.
        Returns a string.
        """
        item = request.get_json() if request.get_json() else request.args
        try:
            if item:
                model = BookModel()
                # case if numeric is id
                if param.isnumeric():
                    model = BookModel.get_by_id(param)
                else:
                    model = BookModel.get_by_name(param)
                if 'name' in item:
                    model.name = item['name']
                if 'edition' in item:
                    model.edition = item['edition']
                if 'publication_year' in item:
                    model.publication_year = item['publication_year']
                model.save()
                return 'Edited', 204
            else:
                return 'Unedited, invalid payload', 400
        except Exception as e:

            return f"{e}", 500

    def delete(self, param):
        """
        Method that removes book.
        Returns a string.
        """
        try:
            # case if numeric is id
            if param.isnumeric():
                book = BookModel.get_by_id(param)
                authors = AuthorBookModel.filter_by_book_id(param)
            else:
                book = BookModel.get_by_name(param)
                authors = AuthorBookModel.filter_by_book_id(book.id)
            book.delete()
            for author_association in authors:
                author_association.delete()
            return 'No Content', 204
        except Exception as e:
            return f"{e}", 500
