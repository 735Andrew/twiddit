from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
import sqlalchemy as sa
from flask_babel import _, lazy_gettext as _l
from app import db
from app.models import User

class LoginForm(FlaskForm):
    """Форма входа пользователя в приложение"""
    username = StringField(_l("Username"), validators=[DataRequired()])
    password = PasswordField(_l("Password"), validators=[DataRequired()])
    remember_me = BooleanField(_l("Remember me"))
    submit = SubmitField(_l("Sign in!"))

class RegistrationForm(FlaskForm):
    """Форма регистрации пользователя в приложении"""
    username = StringField(_l("Username"), validators=[DataRequired()])
    email = StringField(_l("Email"), validators=[DataRequired(), Email()])
    password = PasswordField(_l("Password"), validators=[DataRequired()])
    password2 = PasswordField(_l("Repeat Password"), validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField(_l("Register"))

    def validate_username(self, username):
        # Проверка уникальности имени пользователя
        query = sa.select(User).where(User.username == username.data)
        user = db.session.scalar(query)
        if user is not None:
            raise ValidationError(_('Use a different username!'))

    def validate_email(self, email):
        # Проверка уникальности почты пользователя
        query = sa.select(User).where(User.email == email.data)
        user = db.session.scalar(query)
        if user is not None:
            raise ValidationError(_('Use a different email!'))


class ResetPasswordRequestForm(FlaskForm):
    """Форма запроса на сброс пароля пользователем"""
    email = StringField(_l('Email'), validators=[DataRequired(), Email()])
    submit = SubmitField(_l('Request Password Reset'))

class ResetPasswordForm(FlaskForm):
    """Форма обновления пароля пользователем"""
    password = PasswordField(_l("Password"), validators=[DataRequired()])
    password2 = PasswordField(_l("Repeat password"), validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(_l("Request Password Reset"))