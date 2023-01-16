from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField


class AddForm(FlaskForm):

    name = StringField('Name of Puppy: ')
    submit = SubmitField('Add Puppy')

class DelForm(FlaskForm):

    id = IntegerField('Id Number of Puppy to remove: ')
    submit = SubmitField('Remove puppy')

class AddOwner(FlaskForm):

    name = StringField('Name of Owner: ')
    id_pup = IntegerField('Id of Puppy: ')
    submit = SubmitField('Add Owner')