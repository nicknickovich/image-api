import os

SECRET_KEY = "dev"
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(
    os.getcwd(), "test.db")
