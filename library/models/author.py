from models import db


class AuthorModel(db.Model):
    __tablename__ = 'author'

    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(100), nullable=False, unique=True)

    @staticmethod
    def get_by_name(name: str):
        return db.session.query(AuthorModel).filter_by(name=name).first()

    @staticmethod
    def get_by_id(id: int):
        return AuthorModel.query.filter_by(id=id).first()

    @staticmethod
    def list_all():
        return AuthorModel.query.order_by(AuthorModel.name).all()

    def save(self):
        db.session.merge(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
