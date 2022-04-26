# coding: utf-8
import json
from os import defpath
from typing import Text
from sqlalchemy import Boolean, Column, Date, DateTime, ForeignKey, Integer, LargeBinary, String, UniqueConstraint, text, Sequence
from sqlalchemy.orm import relationship
from sqlalchemy.types import TEXT
from flask_appbuilder import Model
from flask_appbuilder.security.sqla.models import User


class Document(Model):
    __tablename__ = 'document'

    id = Column(Integer, Sequence('document_id_seq'), primary_key=True, nullable=True)
    type = Column(String(255))
    incipit = Column(String(255))
    transcription = Column(TEXT)
    language = Column(String(255))
    gregorian_date = Column(Date)
    title = Column(String(255))
    archive = Column(String(255))
    publication = Column(String(255))
    collection = Column(String(255), unique=False)
    folder = Column(String(255), unique=False)
    note = Column(String(255))
    shelfmark = Column(String(255))
    folder_number = Column(String(255))
    is_date_deduced = Column(Boolean)
    is_deleted = Column(Boolean, server_default=text("false"))

    def json(self) :
	    return {"id": self.id, "type": self.type, "incipit": self.incipit, "transcription": self.transcription,\
            "language": self.language, "gregorian_date": str(self.gregorian_date), "collection": self.collection, "folder": self.folder,\
            "note": self.note, "shelfmark": self.shelfmark, "folder_number": self.folder_number, "is_date_deduced": self.is_date_deduced, "is_deleted": self.is_deleted}
    def __repr__(self):
        return json.dumps(self.json())

class Appuser(Model):
    __tablename__ = 'appuser'

    id = Column(Integer, Sequence('appuser_id_seq'), primary_key=True, nullable=True)
    username = Column(String(255), unique=True)
    password = Column(String(255))
    auth_key = Column(String(255))
    password_reset_token = Column(String(255))
    is_disabled = Column(Boolean, server_default=text("false"))

    def __repr__(self):
        return self.name
    
    def __init__(self, username, password, auth_key, password_reset_token, is_disabled):
        self.username = username
        self.password = password
        self.auth_key = auth_key
        self.password_reset_token = password_reset_token
        self.is_disabled = is_disabled


class Person(Model):
    __tablename__ = 'person'

    id = Column(Integer, Sequence('person_id_seq'), primary_key=True, nullable=True)
    name = Column(String(255), unique=True)
    name_latin = Column(String(255))
    alias = Column(String(255))
    birth = Column(String(255))
    death = Column(String(255))
    reference = Column(TEXT)
    wikidata = Column(String(255))
    links = Column(String(255))
    notes = Column(TEXT)
    is_deleted = Column(Boolean, server_default=text("false"))
    is_validated = Column(Boolean)

    def __repr__(self):
        return self.name


class Place(Model):
    __tablename__ = 'place'

    id = Column(Integer, Sequence('place_id_seq'), primary_key=True, nullable=True)
    city = Column(String(255))
    description = Column(String(255))
    is_deleted = Column(Boolean, server_default=text("false"))
    is_validated = Column(Boolean)
    
    def __repr__(self):
        return self.name

class Actor(Model):
    __tablename__ = 'actor'
    __table_args__ = (
        UniqueConstraint('document_id', 'person_id', 'role'),
    )

    id= Column(Integer, Sequence('actor_id_seq'), primary_key=True, nullable=True)
    document_id = Column(ForeignKey('document.id', ondelete='CASCADE'), nullable=False)
    person_id = Column(ForeignKey('person.id', ondelete='CASCADE'), nullable=False)
    appuser_id = Column(ForeignKey('ab_user.id', ondelete='CASCADE'), nullable=False)
    role = Column(String(255))

    appuser = relationship('User')
    document = relationship('Document')
    person = relationship('Person')

    def __repr__(self):
        return self.name


class Image(Model):
    __tablename__ = 'image'

    id = Column(Integer, Sequence('image_id_seq'), primary_key=True, nullable=True)
    title = Column(String(255),nullable=True)
    data = Column(TEXT)
    description = Column(String(255), nullable=True)
    document_id = Column(ForeignKey('document.id'), nullable=False)

    document = relationship('Document')

    def __repr__(self):
        return self.name


class Position(Model):
    __tablename__ = 'position'
    __table_args__ = (
        UniqueConstraint('document_id', 'place_id', 'type'),
    )
    id= Column(Integer, Sequence('position_id_seq'), primary_key=True, nullable=True)
    document_id = Column(ForeignKey('document.id', ondelete='CASCADE'), nullable=False)
    place_id = Column(ForeignKey('place.id', ondelete='CASCADE'), nullable=False)
    appuser_id = Column(ForeignKey('ab_user.id', ondelete='CASCADE'), nullable=False)
    type = Column(String(255))

    appuser = relationship('User')
    document = relationship('Document')
    place = relationship('Place')

    def __repr__(self):
        return self.name

class Institution(Model):
    __tablename__ = 'institution'

    id = Column(Integer, Sequence('institution_id_seq'), primary_key=True, nullable=True)
    name = Column(String(255),nullable=True)
    visibility = Column(String(255),nullable=True)
    type = Column(String(255),nullable=True)
    year = Column(String(255),nullable=True)
    place = Column(String(255),nullable=True)
    notes = Column(String(255),nullable=True)

    def __repr__(self):
        return self.name

class Affiliation(Model):
    __tablename__ = 'affiliation'
    __table_args__ = (
        UniqueConstraint('person_id', 'institution_id'),
    )

    person_id = Column(ForeignKey('person.id', ondelete='CASCADE'), primary_key=True, nullable=False)
    institution_id = Column(ForeignKey('institution.id', ondelete='CASCADE'), primary_key=True, nullable=False)
    from_date = Column(Date)
    to_date= Column(Date)

    person = relationship('Person')
    institution = relationship('Institution')

    def __repr__(self):
        return self.name