# -*- coding: utf-8 -*-
"""
    Create a sqlite database with test data.
"""

import base64
import os
import datetime
from image_app import db, create_app
from image_app.models import Image


app = create_app("config.py")

with app.app_context():
    # Initialize database.
    db.create_all()

    # Create example data.
    image_files = [f for f in os.listdir("test_images") 
                if os.path.isfile(os.path.join("test_images", f))]

    for image in image_files:
        # Get base64 bytes object from image.
        with open(os.path.join("test_images", image), "rb") as f:
            encoded = base64.b64encode(f.read())
        date_uploaded = datetime.datetime.now()
        
        new_image = Image(
            image_file=encoded,
            date_uploaded=date_uploaded,
            filename=image
        )

        db.session.add(new_image)
        db.session.commit()
