from models import db

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer

class AuthorBookModel(db.Model):
    __tablename__ = 'author_book'

    id: int = db.Column(db.Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey("author.id"))
    book_id = Column(Integer, ForeignKey("book_id.id"))


    @staticmethod
    def get_by_id(id: int):
        return AuthorModel.query.filter_by(id=id).first()

    @staticmethod
    def get_by_author_id(author_id: int):
        return AuthorModel.query.filter_by(author_id=author_id).first()

    @staticmethod
    def get_by_book_id(book_id: int):
        return AuthorModel.query.filter_by(book_id=book_id).first()

    @staticmethod
    def list_all():
        return AuthorModel.query.order_by(AuthorModel.name).all()

    def save(self):
        db.session.merge(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
