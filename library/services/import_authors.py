import csv

from models.author import AuthorModel
from models import db

import sqlalchemy

class ImportAuthors:

    def start():
        print(' ----------- persistindo autores! -----------  ')
        try:
            with open('authors.csv', 'r') as file:
                authors = csv.DictReader(file)

                item = lambda item: AuthorModel(name=(item['name'])) \
                        if not AuthorModel.get_by_name(item['name']) else None

                objects = []
                for i in authors:
                    author = item(i)
                    objects.append(author) if author else None

                db.session.add_all(objects)
                db.session.commit()
        except Exception as e:
            print(e)
        print(' ----------- persistencia concluida! -----------  ')
