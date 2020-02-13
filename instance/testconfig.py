"""
    Test config for app.

    SQLite database is used in this case for testing purposes.
"""

import os

SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(
    os.getcwd(), "tests", "test.db")
SQLALCHEMY_TRACK_MODIFICATIONS = False
TESTING = True
WTF_CSRF_ENABLED = False