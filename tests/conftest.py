"""
    Fixtures that create separate instance of an app and database.
"""

import base64
import datetime
import os
import pytest
from image_app import create_app, db
from image_app.models import Image


@pytest.fixture(scope="module")
def test_client():
    """Create an instance of an app.  Add it to context.
    Run tests and then delete app from context.
    """
    # Create app with test configuration.
    app = create_app("testconfig.py")

    # Test client provided by Flask
    testing_client = app.test_client()

    # Establish an app context.
    ctx = app.app_context()
    ctx.push()

    yield testing_client

    # Remove app context.
    ctx.pop()


@pytest.fixture(scope="module")
def init_database():
    """Create an instance of a database and populate it with test data.
    Run tests and then delete test data.
    """
    # Initialize database.
    db.create_all()

    test_img_path = os.path.join(os.getcwd(), "tests", "test_images")
    # Create example data.
    image_files = [filename for filename in os.listdir(test_img_path)
                   if filename.endswith((".jpg", ".jpeg", ".png"))]
    image_files.sort()
    image_files = image_files[:3]

    for index, image_file in enumerate(image_files):
        # Get base64 bytes object from image.
        with open(os.path.join(test_img_path, image_file), "rb") as f:
            encoded = base64.b64encode(f.read())
        
        date_uploaded = datetime.datetime(2020, 1, 1)

        new_image = Image(
            image_file=encoded,
            date_uploaded=date_uploaded,
            filename=image_file
        )

        db.session.add(new_image)
        db.session.commit()

    yield db

    # Delete everything from db.
    db.drop_all()