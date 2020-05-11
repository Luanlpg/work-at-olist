from models import db

class AuthorBookModel(db.Model):

    __tablename__ = 'author_book'
    id: int = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"))
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"))


    @staticmethod
    def get_by_id(id: int):
        return AuthorBookModel.query.filter_by(id=id).first()

    @staticmethod
    def filter_by_author_id(author_id: int):
        return AuthorBookModel.query.filter_by(author_id=author_id).all()

    @staticmethod
    def filter_by_book_id(book_id: int):
        return AuthorBookModel.query.filter_by(book_id=book_id).all()

    @staticmethod
    def list_all():
        return AuthorBookModel.query.order_by(AuthorBookModel.name).all()

    def save(self):
        db.session.merge(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
