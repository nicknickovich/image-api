# -*- coding: utf-8 -*-
"""
    Create a sqlite database with test data.

    Created database can be used for manual testing.
"""

import base64
import os
import datetime
from image_app import db, create_app
from image_app.models import Image
from image_app.utils import generate_json


app = create_app("config.py")

with app.app_context():
    # Initialize database.
    db.create_all()

    # Create example data.
    image_files = [filename for filename in os.listdir(os.path.join("tests", "test_images"))
                if filename.endswith((".jpg", ".jpeg", ".png"))]

    for image_file in image_files:
        # Get base64 bytes object from image.
        with open(os.path.join("tests", "test_images", image_file), "rb") as f:
            encoded = base64.b64encode(f.read())
        
        date_uploaded = datetime.datetime.now()

        new_image = Image(
            image_file=encoded,
            date_uploaded=date_uploaded,
            filename=image_file
        )

        db.session.add(new_image)
        db.session.commit()
