from models import db
from models.author_book import AuthorBookModel
from models.author import AuthorModel
from models.book import BookModel

from os import environ

from sqlalchemy import create_engine


class Schema:
    @staticmethod
    def migration():
        engine = create_engine(environ.get('SQLALCHEMY_DATABASE_URI'))
        db.create_all()
