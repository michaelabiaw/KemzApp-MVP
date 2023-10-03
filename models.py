""" models for the application """

from flask_sqlalchemy import SQLAlchemy
from ecomz import app
from ecomz import db
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import json

#Base = declarative_base()


class Venue(db.Model):
    __tablename__ = 'venues'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(), nullable=False)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    #genres = db.Column(db.ARRAY(db.String))
    genres = db.Column(db.String())
    website_link = db.Column(db.String(),nullable=False)
    seeking_talent = db.Column(db.Boolean, default=False)
    image_link = db.Column(db.String(500), nullable=False)
    facebook_link = db.Column(db.String(120), nullable=False)
    seeking_description = db.Column(db.String())
    show = db.relationship('Show', backref='Venue', lazy=True)

    def __repr__(self):
        return f'<Venue {self.id} - {self.name}>'



class Artist(db.Model):
    __tablename__ = 'artists'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    #genres = db.Column(db.ARRAY(db.String))
    genres = db.Column(db.String())
    image_link = db.Column(db.String(500),nullable=False)
    facebook_link = db.Column(db.String(120),nullable=False)
    seeking_venue = db.Column(db.Boolean, default=False)
    website_link = db.Column(db.String(),nullable=False)
    seeking_description = db.Column(db.String())
    show = db.relationship('Show', backref='Artist', lazy=True)

    def __repr__(self) :
        return f'(Artist id:{self.id} {self.name})'



class Show(db.Model):
    __tablename__ = 'shows'
    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id'), nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey('Venue.id'), nullable=False)
    start_time = db.Column(db.DateTime,nullable=False)
    artist = db.relationship('Artist', backref='Show', lazy=True)
    #venue = db.relationship('Venue', backref='Show', lazy=True)
    venue_id = db.Column(db.Integer, db.ForeignKey('venues.id'), nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'), nullable=False)

