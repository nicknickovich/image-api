"""
    Tests for CRUD functionality of API.
"""
import base64
import json
import os
from image_app.utils import generate_json

test_img_path = os.path.join(os.getcwd(), "tests", "test_images")

# Names of all images in test_images folder.
IMAGE_FILES = [filename for filename in os.listdir(test_img_path)
               if filename.endswith((".jpg", ".jpeg", ".png"))]
IMAGE_FILES.sort()

def test_api_return_all_images(test_client, init_database):
    image_files = IMAGE_FILES[:3]
    json_data = []
    for index, image_file in enumerate(image_files):
    # Get base64 bytes object from image.
        with open(os.path.join(test_img_path, image_file), "rb") as f:
            encoded = base64.b64encode(f.read())
        new_image = generate_json(
            id=index+1, encoded_image=encoded, filename=image_file
        )
        json_data.append(new_image)
    
    response = test_client.get("/api/images")
    assert response.json == json_data


def test_api_return_one_image(test_client, init_database):
    image_file = IMAGE_FILES[0]
    # Get base64 bytes object from image.
    with open(os.path.join(test_img_path, image_file), "rb") as f:
        encoded = base64.b64encode(f.read())
    new_image = generate_json(
        id=1, encoded_image=encoded, filename=image_file
    )
    
    response = test_client.get("/api/images/1")
    assert response.json["date_uploaded"] == new_image["date_uploaded"]


# def test_api_add_new_image(test_client, init_database):
#    # TODO
# def test_api_update_image(test_client, init_database):
#    # TODO
# def test_api_delete_image(test_client, init_database):
#    # TODO
