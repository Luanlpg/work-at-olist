import sys
from os import environ

from dotenv import load_dotenv
from flask import Flask

from models import initialize_database
from resources import initialize_resources
from services.import_authors import ImportAuthors as import_authors
from schema.schema import Schema

sys.path.append("${PWD}")

application = Flask(__name__)

print('Loading environment variables from .env file')
load_dotenv('./environments/local.env')

for item in environ.items():
    application.config[item[0]] = item[1]

initialize_database(application)

initialize_resources(application)

@application.before_first_request
def startup():
    print("Initializing migration DB")
    Schema.migration()
    print("Initializing authors persistence")
    import_authors.start()

if __name__ == '__main__':
    print('Initilizing application')
    application.run()
