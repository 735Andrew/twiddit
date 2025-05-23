from flask import Blueprint
import os
import click

bp = Blueprint("cli", __name__, cli_group=None)


@bp.cli.group()
def translate():
    """Команды перевода и локализации"""
    pass


@translate.command()
def update():
    """Обновление всех языков"""
    if os.system("pybabel extract -F babel.cfg -k _l -o messages.pot ."):
        raise RuntimeError("extract command failed")
    if os.system("pybabel update -i messages.pot -d app/translations"):
        raise RuntimeError("update command failed")
    os.remove("messages.pot")


@translate.command()
def compile():
    """Компиляция всех языков"""
    if os.system("pybabel compile -d app/translations"):
        raise RuntimeError("compile command failed")


@translate.command()
@click.argument("lang")
def init(lang):
    """Инициализация нового языка"""
    if os.system("pybabel extract -F babel.cfg -k _l -o messages.pot ."):
        raise RuntimeError("extract command failed")
    if os.system("pybabel init -i messages.pot -d app/translations -l " + lang):
        raise RuntimeError("init command failed")
    os.remove("messages.pot")
