# -*- coding: utf-8 -*-
"""
    image_app.api.views
    ~~~~~~~~~~~~~~~~~~~

    REST API for images.
"""

from flask import Blueprint, request
from flask_restful import Resource
from image_app.models import Image
from image_app import db, api_restful
from image_app.api.schema import image_schema, images_schema


api_v2 = Blueprint("api", __name__)


class ImageApi(Resource):
    """CRUD functionality for images."""
    def get(self, image_id=None):
        """Retrieve an image with a given id if id is provided.
        Otherwise retrieve all images.
        """
        if image_id is None:
            all_images = Image.query.all()
            return images_schema.dump(all_images)

        image = Image.query.get_or_404(image_id)
        return image_schema.dump(image)

    def post(self):
        """Create a new image."""
        # Get image's attributes from json.
        image = request.json["image"]
        date_uploaded = request.json["date_uploaded"]
        image_type = request.json["image_type"]
        # Create a new image with provided attributes.
        new_image = Image(
            image=image,
            date_uploaded=date_uploaded,
            image_type=image_type,
        )
        db.session.add(new_image)
        db.session.commit()

        return image_schema.dump(new_image), 201

    def put(self, image_id):
        """Update an image with a given id."""
        image = Image.query.get_or_404(image_id)
        # Get attributes for an image from json.
        image = request.json["image"]
        date_uploaded = request.json["date_uploaded"]
        image_type = request.json["image_type"]
        # Set new values for attributes.
        image.image = image
        image.date_uploaded = date_uploaded
        image.image_type = image_type

        db.session.commit()

        return image_schema.dump(image)

    def delete(self, image_id):
        """Delete an image with a given id."""
        image = Image.query.get_or_404(image_id)
        db.session.delete(image)
        db.session.commit()

        return image_schema.dump(image)


# Setup resource routing for employees.
api_restful.add_resource(ImageApi,
                         "/api/images",
                         "/api/images/<image_id>")
