import csv

from models.author import AuthorModel
from models import db

class ImportAuthors:
    """
    Class that automates the persistence of authors.
    """

    def start():
        """
        Method that performs the persistence of authors contained in a csv file.
        """
        try:
            with open('authors.csv', 'r') as file:
                authors = csv.DictReader(file)
                # lambda that returns Author Model object if it doesn't
                # already exist in the bank
                item = lambda item: AuthorModel(name=(item['name'])) \
                        if not AuthorModel.get_by_name(item['name']) else None
                objects = []
                for i in authors:
                    author = item(i)
                    objects.append(author) if author else None
                db.session.add_all(objects)
                db.session.commit()
        except Exception as e:
            return e
        print('Persistence of authors completed')
