# -*- coding: utf-8 -*-
"""
    image_app.api.views
    ~~~~~~~~~~~~~~~~~~~

    REST API for images.
"""
from datetime import datetime
from flask import Blueprint, request
from flask_restful import Resource
from image_app.models import Image
from image_app import db, api_restful
from image_app.api.schema import image_schema, images_schema


api = Blueprint("api", __name__)


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
        image_file = bytes(request.json["image_file"], "ascii")
        date_uploaded = datetime.strptime(
            request.json["date_uploaded"], "%Y-%m-%dT%H:%M:%S.%f"
        )
        filename = request.json["filename"]
        # Create a new image with provided attributes.
        new_image = Image(
            image_file=image_file,
            date_uploaded=date_uploaded,
            filename=filename,
        )
        db.session.add(new_image)
        db.session.commit()

        return image_schema.dump(new_image), 201

    def put(self, image_id):
        """Update an image with a given id."""
        image = Image.query.get_or_404(image_id)
        # Get attributes for an image from json.
        image_file = bytes(request.json["image_file"], "ascii")
        filename = request.json["filename"]
        # Set new values for attributes.
        image.image_file = image_file
        image.filename = filename

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
