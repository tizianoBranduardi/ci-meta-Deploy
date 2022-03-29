from .models import *
from . import appbuilder, db
from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface

from .api import definitions


class actorModelView(ModelView):
   datamodel = SQLAInterface(Actor)
   list_columns = ["document_id", "person.name", "document.id", "role"]
   show_columns = ["document_id", "person.name", "document.id", "appuser.username", "role", "person_id", "appuser_id"]
   edit_columns = ["document_id", "role", "person_id", "appuser_id"]
   add_columns = ["document_id", "role", "person_id", "appuser_id"]
   related_views = []

appbuilder.add_view(
      actorModelView, "actor List", icon="fa-folder-open-o", category="Menu")


class imageModelView(ModelView):
   datamodel = SQLAInterface(Image)
   list_columns = ["description", "document.id", "title", "data"]
   show_columns = ["description", "document.id", "title", "data", "id", "document_id"]
   edit_columns = ["description", "title", "data", "id", "document_id"]
   add_columns = ["description", "title", "data", "id", "document_id"]
   related_views = []

appbuilder.add_view(
      imageModelView, "image List", icon="fa-folder-open-o", category="Menu")


class positionModelView(ModelView):
   datamodel = SQLAInterface(Position)
   list_columns = ["document_id", "place.description", "document.id", "type"]
   show_columns = ["document_id", "place.description", "document.id", "appuser.username", "type", "place_id", "appuser_id"]
   edit_columns = ["document_id", "type", "place_id", "appuser_id"]
   add_columns = ["document_id", "type", "place_id", "appuser_id"]
   related_views = []

appbuilder.add_view(
      positionModelView, "position List", icon="fa-folder-open-o", category="Menu")


class documentModelView(ModelView):
   datamodel = SQLAInterface(Document)
   list_columns = ["id", "type", "incipit", "transcription", "language"]
   show_columns = ["id", "type", "incipit", "transcription", "language", "gregorian_date", "collection", "folder", "note", "shelfmark", "folder_number",  "is_date_deduced", "is_deleted"]
   edit_columns = ["id", "type", "incipit", "transcription", "language", "gregorian_date", "collection", "folder", "note", "shelfmark", "folder_number", "is_date_deduced", "is_deleted"]
   add_columns = ["id", "type", "incipit", "transcription", "language", "gregorian_date", "collection", "folder", "note", "shelfmark", "folder_number", "is_date_deduced", "is_deleted"]
   related_views = [actorModelView, imageModelView, positionModelView]

appbuilder.add_view(
      documentModelView, "document List", icon="fa-folder-open-o", category="Menu")


# table already generated per recursion: actor


class personModelView(ModelView):
   datamodel = SQLAInterface(Person)
   list_columns = ["name", "is_deleted"]
   show_columns = ["name", "is_deleted", "id", "is_validated"]
   edit_columns = ["name", "is_deleted", "id", "is_validated"]
   add_columns = ["name", "is_deleted", "id", "is_validated"]
   related_views = [actorModelView]

appbuilder.add_view(
      personModelView, "person List", icon="fa-folder-open-o", category="Menu")


# table already generated per recursion: position


class placeModelView(ModelView):
   datamodel = SQLAInterface(Place)
   list_columns = ["description", "city", "is_deleted"]
   show_columns = ["description", "city", "is_deleted", "id", "is_validated"]
   edit_columns = ["description", "city", "is_deleted", "id", "is_validated"]
   add_columns = ["description", "city", "is_deleted", "id", "is_validated"]
   related_views = [positionModelView]

appbuilder.add_view(
      placeModelView, "place List", icon="fa-folder-open-o", category="Menu")

class appuserModelView(ModelView):
   datamodel = SQLAInterface(Appuser)
   list_columns = ["username", "password", "auth_key", "password_reset_token", "is_disabled"]
   show_columns = ["username", "password", "auth_key", "password_reset_token", "is_disabled", "id"]
   edit_columns = ["username", "password", "auth_key", "password_reset_token", "is_disabled", "id"]
   add_columns = ["username", "password", "auth_key", "password_reset_token", "is_disabled", "id"]
   related_views = [actorModelView, positionModelView]

appbuilder.add_view(
      appuserModelView, "appuser List", icon="fa-folder-open-o", category="Menu")


db.create_all()

