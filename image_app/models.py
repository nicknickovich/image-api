# -*- coding: utf-8 -*-
"""
    image_app.models
    ~~~~~~~~~~~~~~~~

    Model for image data.
    These models are used by SQLAlchemy to create database, add, update
    and query database.
"""

from image_app import db


class Image(db.Model):
    """Model for an image."""
    id = db.Column(db.Integer, primary_key=True)
    image_file = db.Column(db.LargeBinary, nullable=False)
    date_uploaded = db.Column(db.DateTime, nullable=False)
    filename = db.Column(db.String(10), nullable=False)
