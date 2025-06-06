import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
# импортирование переменных конфигурации приложения
load_dotenv(os.path.join(basedir, ".env"))


class Config:
    """Параметры конфигурации для создания приложения."""

    SECRET_KEY = os.environ.get("SECRET_KEY") or "very_secret_key"
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL"
    ) or "sqlite:///" + os.path.join(basedir, "app.db")

    # Сведения о сервере электронной почты
    MAIL_SERVER = os.environ.get("MAIL_SERVER")
    MAIL_PORT = int(os.environ.get("MAIL_PORT") or 25)
    MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS") is not None
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    MS_TRANSLATOR_KEY = os.environ.get("MS_TRANSLATOR_KEY")
    ADMINS = os.environ.get("ADMINS")

    POSTS_PER_PAGE = 25  # Количество постов на страницу
    LANGUAGES = ["en", "ru"]  # Поддерживаемые приложением языки
    LOG_TO_STDOUT = os.environ.get("LOG_TO_STDOUT")
    ELASTICSEARCH_URL = os.environ.get("ELASTICSEARCH_URL")
    REDIS_URL = os.environ.get("REDIS_URL") or "redis://"
