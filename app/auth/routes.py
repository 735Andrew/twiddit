from app.auth.forms import LoginForm, RegistrationForm, ResetPasswordForm, ResetPasswordRequestForm
from app import db
from flask import render_template, redirect, url_for, request, flash
from urllib.parse import urlsplit
from flask_login import current_user, login_user, logout_user
from app.models import User
from app.auth.email import send_password_reset_email
from app.auth import bp
import sqlalchemy as sa
from flask_babel import _


@bp.route('/login', methods=["GET", "POST"])
def login():
    """Маршрут регистрации пользователя."""
    if current_user.is_authenticated:
        # В случае, если пользователь уже зарегистрирован в системе -
        # он минует систему верификации.
        return redirect(url_for("main.index"))
    form = LoginForm() # Форма регистрации
    if form.validate_on_submit():
        query = sa.select(User).where(User.username == form.username.data)
        user = db.session.scalar(query) # Запрос к БД для проверки наличия пользователя
        if user is None or not user.check_password(form.password.data):
            flash(_("Invalid username or password"))
            return redirect(url_for("auth.login"))
        login_user(user, remember=form.remember_me.data)

        # Возвращение пользователя к изначальному его запросу в случае если:
        # 1. Пользователь не был зарегистрирован в системе
        # 2. Пользователь переходил не на адрес /login
        next_page = request.args.get("next")
        if not next_page or urlsplit(next_page).netloc != " ":
            next_page = url_for("main.index")
        return redirect(next_page)
    return render_template("auth/login.html", title=_("Sign In"), form=form)


@bp.route("/logout")
def logout():
    """Маршрут выхода пользователя из системы"""
    logout_user()
    return redirect(url_for("main.index"))


@bp.route('/register', methods=["GET", "POST"])
def register():
    """Маршрут регистрации пользователя в приложении"""
    if current_user.is_authenticated:
        return redirect(url_for('auth.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(_("Congratulations! You are now a registered user!"))
        return redirect(url_for("auth.login"))
    return render_template("auth/register.html", title=_("Register"), form=form)


@bp.route("/reset_password_request", methods=["GET", "POST"])
def reset_password_request():
    """Маршрут сброса пароля пользователем"""
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        query = sa.select(User).where(User.email == form.email.data)
        user = db.session.scalar(query)
        if user:
            send_password_reset_email(user)
        flash(_('Check your email for the instructions to reset your password'))
        return redirect(url_for('auth.login'))
    return render_template("auth/reset_password_request.html", title=_("Reset Password"), form=form)


@bp.route("/reset_password/<token>", methods=["GET", "POST"])
def reset_password(token):
    """Маршрут обновления пароля пользователем"""
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for("main.index"))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash(_("Your password has been reset"))
        return redirect(url_for("auth.login"))
    return render_template("auth/reset_password.html", form=form)
