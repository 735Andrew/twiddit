from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
from flask_babel import lazy_gettext as _l, _
from app import db
import sqlalchemy as sa
from app.models import User


class EditProfileForm(FlaskForm):
    username = StringField(_l("Username"), validators=[DataRequired()])
    about_me = TextAreaField(_l("About me"), validators=[Length(min=0, max=140)])
    submit = SubmitField(_l("Submit"))

    def __init__(self, original_username, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = db.session.scalar(sa.select(User).where(User.username == self.username.data))
            if user is not None:
                raise ValidationError(_("Please use a different username."))


class EmptyForm(FlaskForm):
    submit = SubmitField('Submit')


class PostForm(FlaskForm):
    post = TextAreaField(_l("Say something"), validators=[DataRequired(), Length(min=1, max=140)])
    submit = SubmitField(_l("Submit"))


class MessageForm(FlaskForm):
    message = TextAreaField(_l("Message"), validators = [DataRequired(), Length(min=0, max=140)])
    submit = SubmitField(_l("Submit"))
