from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
from flask_babel import lazy_gettext as _l, _
from app import db
import sqlalchemy as sa
from app.models import User


class EditProfileForm(FlaskForm):
    """
    Форма по изменению пользователем своих данных
    (имени пользователя и поля "о себе") в приложении
    """
    username = StringField(_l("Username"), validators=[DataRequired()])
    about_me = TextAreaField(_l("About me"), validators=[Length(min=0, max=140)])
    submit = SubmitField(_l("Submit"))

    def __init__(self, original_username, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        # Функция проверки корректности введённого пользователем нового имени
        if username.data != self.original_username:
            query = sa.select(User).where(User.username == self.username.data)
            user = db.session.scalar(query)
            if user is not None:
                raise ValidationError(_("Please use a different username."))


class EmptyForm(FlaskForm):
    """Форма-кнопка. Нужна для оформления подписки / отписки"""
    submit = SubmitField('Submit')


class PostForm(FlaskForm):
    """Форма для написания поста пользователем"""
    post = TextAreaField(_l("Say something"), validators=[DataRequired(), Length(min=1, max=140)])
    submit = SubmitField(_l("Submit"))


class MessageForm(FlaskForm):
    """Форма для написания личного сообщения пользователю"""
    message = TextAreaField(_l("Message"), validators = [DataRequired(), Length(min=0, max=140)])
    submit = SubmitField(_l("Submit"))
