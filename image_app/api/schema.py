# -*- coding: utf-8 -*-
"""
    image_app.api.schema
    ~~~~~~~~~~~~~~~~~~~~

    Utility classes and objects for serializing image information.
"""

from department_app import ma


class ImageSchema(ma.Schema):
    """Utility class for serializing image data."""
    class Meta:
        """Fields for serializing."""
        fields = ("id", "image", "date_uploaded", "image_type")

image_schema = ImageSchema()
images_schema = ImageSchema(many=True)
