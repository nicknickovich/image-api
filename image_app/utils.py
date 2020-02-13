# -*- coding: utf-8 -*-
"""
    Utility functions.
"""
from datetime import datetime


def generate_json(id, encoded_image, filename):
    """Generate a dictionary for image with given id, filename
    and encoded image as base64 bytes object.
    Return dictionary that is easily converted to json.
    """
    date_uploaded = datetime.strftime(
        datetime(2020, 1, 1), "%Y-%m-%dT%H:%M:%S"
    )

    new_image = {
        "id": id,
        "image_file": encoded_image.decode("ascii"),
        "date_uploaded": date_uploaded,
        "filename": filename
    }
    
    return new_image