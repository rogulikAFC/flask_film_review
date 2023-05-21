import os

from pathlib import Path


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    BASEDIR = Path(__file__).parent
    IMAGE_UPLOAD_FOLDER=f'{BASEDIR}/app/static/images'