# -*- coding: utf-8 -*-
"""
    image_app.models
    ~~~~~~~~~~~~~~~~

    Model for image data.
    These models are used by SQLAlchemy to create database, add, update
    and query database.
"""

from department_app import db


class Image(db.Model):
    """Model for an image."""
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.LargeBinary, nullable=False)
    date_uploaded = db.Column(db.DateTime, nullable=False)
    image_type = db.Column(db.String(20), nullable=False)
