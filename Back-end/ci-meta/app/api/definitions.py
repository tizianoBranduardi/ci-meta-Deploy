from app.models import *
from app import appbuilder
from flask import Flask
from flask_appbuilder.api import ModelRestApi
from flask_appbuilder.models.sqla.interface import SQLAInterface

app = Flask(__name__)
app.config["DEBUG"] = True

class Document(ModelRestApi):
    resource_name = 'document'
    datamodel = SQLAInterface(Document)
    base_order = ('id', 'asc')
    page_size=1000

appbuilder.add_api(Document)

class Actor(ModelRestApi):
    resource_name = 'actor'
    datamodel = SQLAInterface(Actor)
    page_size=1000

appbuilder.add_api(Actor)

class Appuser(ModelRestApi):
    resource_name = 'appuser'
    datamodel = SQLAInterface(Appuser)
    page_size=1000

appbuilder.add_api(Appuser)

class Image(ModelRestApi):
    resource_name = 'image'
    datamodel = SQLAInterface(Image)
    page_size=1000

appbuilder.add_api(Image)

class Person(ModelRestApi):
    resource_name = 'person'
    datamodel = SQLAInterface(Person)
    base_order = ('name', 'asc')
    page_size=1000

appbuilder.add_api(Person)

class Place(ModelRestApi):
    resource_name = 'place'
    datamodel = SQLAInterface(Place)
    base_order = ('city', 'asc')
    page_size=1000

appbuilder.add_api(Place)

class Position(ModelRestApi):
    resource_name = 'position'
    datamodel = SQLAInterface(Position)
    page_size=1000

appbuilder.add_api(Position)

class Institution(ModelRestApi):
    resource_name = 'institution'
    datamodel = SQLAInterface(Institution)
    base_order = ('name', 'asc')
    page_size=1000

appbuilder.add_api(Institution)

class Affiliation(ModelRestApi):
    resource_name = 'affiliation'
    datamodel = SQLAInterface(Affiliation)
    page_size=1000

appbuilder.add_api(Affiliation)

class Configuration(ModelRestApi):
    resource_name = 'configuration'
    datamodel = SQLAInterface(Configuration)
    page_size=1000

appbuilder.add_api(Configuration)
