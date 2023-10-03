from datetime import datetime
from flask_wtf import Form
from wtforms import StringField, SelectField, SelectMultipleField, DateTimeField, BooleanField
from wtforms.validators import DataRequired, AnyOf, URL
from ecomz import app

class ShowForm(Form):
    artist_id = StringField(
        'artist_id'
    )
    venue_id = StringField(
        'venue_id'
    )
    start_time = DateTimeField(
        'start_time',
        validators=[DataRequired()],
        default= datetime.today()
    )

class VenueForm(Form):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    city = StringField(
        'city', validators=[DataRequired()]
    )
    state = SelectField(
        'state', validators=[DataRequired()],
        choices=[
            ('AR', 'AR'),
            ('GR', 'GR'),
            ('BR', 'BR'),
            ('BE', 'BE'),
            ('CR', 'CR'),
            ('AHR', 'AHR'),
            ('ER', 'ER'),
            ('NR', 'NR'),
            ('SR', 'SR'),
            ('UE', 'UE'),
            ('NE', 'NE'),
            ('UW', 'UW'),
            ('VR', 'VR'),
            ('OR', 'OR'),
            ('WR', 'WR'),
            ('WN', 'WN')
        ]
    )
    address = StringField(
        'address', validators=[DataRequired()]
    )
    phone = StringField(
        'phone'
    )
    image_link = StringField(
        'image_link'
    )
    genres = SelectMultipleField(
        
        'genres', validators=[DataRequired()],
        choices= [
            ('Alternative', 'Alternative'),
            ('Hi-life', 'Hi-life'),
            ('Classical', 'Classical'),
            ('Country', 'Country'),
            ('Gospel', 'Gospel'),
            ('Instrumental', 'Instrumental'),
            ('Pop', 'Pop'),
            ('R&B', 'R&B'),
            ('Reggae-Dancehall', 'Reggae-Dancehall'),
            ('Afrobeats', 'Afrobeats'),
            ('Other', 'Other'),
        ]
     )

    facebook_link = StringField(
        'facebook_link', validators=[URL()]
    )
    website_link = StringField(
        'website_link'
    )

    seeking_talent = BooleanField( 'seeking_talent' )

    seeking_description = StringField(
        'seeking_description'
    )



class ArtistForm(Form):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    city = StringField(
        'city', validators=[DataRequired()]
    )
    state = SelectField(
        'state', validators=[DataRequired()],
        choices=[
            ('AR', 'AR'),
            ('GR', 'GR'),
            ('BR', 'BR'),
            ('BE', 'BE'),
            ('CR', 'CR'),
            ('AHR', 'AHR'),
            ('ER', 'ER'),
            ('NR', 'NR'),
            ('SR', 'SR'),
            ('NE', 'NE'),
            ('UE', 'UE'),
            ('UW', 'UW'),
            ('VR', 'VR'),
            ('OR', 'OR'),
            ('WR', 'WR'),
            ('WN', 'WN'),
        ]
    )
    phone = StringField(
        # TODO implement validation logic for state
        'phone'
    )
    image_link = StringField(
        'image_link'
    )
    genres = SelectMultipleField(
        'genres', validators=[DataRequired()],
        choices=[
            ('Alternative', 'Alternative'),
            ('Hi-life', 'Hi-life'),
            ('Classical', 'Classical'),
            ('Country', 'Country'),
            ('Gospel', 'Gospel'),
            ('Instrumental', 'Instrumental'),
            ('Pop', 'Pop'),
            ('R&B', 'R&B'),
            ('Reggae-Dancehall', 'Reggae-Dancehall'),
            ('Afrobeats', 'Afrobeats'),
            ('Other', 'Other'),
        ]
     )
    facebook_link = StringField(
        # TODO implement enum restriction
        'facebook_link', validators=[URL()]
     )

    website_link = StringField(
        'website_link'
     )

    seeking_venue = BooleanField( 'seeking_venue' )

    seeking_description = StringField(
            'seeking_description'
     )




