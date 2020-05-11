from models import db

class BookModel(db.Model):
    """
    Book model.
    """
    
    __tablename__ = 'book'
    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(70), nullable=False)
    edition: str = db.Column(db.String(50), nullable=False)
    publication_year: str = db.Column(db.String(10), nullable=False)

    @staticmethod
    def get_by_name(name: str):
        return db.session.query(BookModel).filter_by(name=name).first()

    @staticmethod
    def filter_by_name(name: str):
        return db.session.query(BookModel).filter(BookModel.name.like(f'%{name}%')).all()

    @staticmethod
    def get_by_id(id: int):
        return BookModel.query.filter_by(id=id).first()

    @staticmethod
    def filter_by_edition(edition: str):
        return BookModel.query.filter_by(edition=edittion)

    @staticmethod
    def filter_by_publication_year(publication_year: str):
        return BookModel.query.filter_by(publication_year=publication_year)

    @staticmethod
    def list_all():
        return BookModel.query.order_by(BookModel.name).all()

    def save(self):
        db.session.merge(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
