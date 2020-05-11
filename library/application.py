from dotenv import load_dotenv
from flask import Flask
from models import initialize_database
from os import environ
from resources import initialize_resources
from services.import_authors import ImportAuthors as import_authors
from schema.schema import Schema
import sys

sys.path.append("${PWD}")

application = Flask(__name__)

# load de variáveis de ambiente
print('Loading environment variables from .env file')
load_dotenv('./environments/local.env')

# load das variaveis de ambiente dentro do flask
for item in environ.items():
    application.config[item[0]] = item[1]

# start no database
initialize_database(application)

# Starting RESTful endpoints
initialize_resources(application)

@application.before_first_request
def startup():
    print("Initializing migration DB")
    Schema.migration()
    print("Initializing persist authors")
    import_authors.start()

# Run application
if __name__ == '__main__':
    print('Initilizing application')
    application.run()
