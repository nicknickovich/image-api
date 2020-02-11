# -*- coding: utf-8 -*-
"""
    image_app.api.schema
    ~~~~~~~~~~~~~~~~~~~~

    Utility classes and objects for serializing image information.
"""

from image_app import ma


class ImageSchema(ma.Schema):
    """Utility class for serializing image data."""
    class Meta:
        """Fields for serializing."""
        fields = ("id", "image_file", "date_uploaded", "filename")

image_schema = ImageSchema()
images_schema = ImageSchema(many=True)
