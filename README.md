# image-api

Basic api for images. For the sake of the exercise it is assumed that images will be provided in a form of json data where image itself is stored as base64 string.


## API routes:
- GET /api/images - retrieve all images;
- GET /api/images/<image_id> - retrieve an image with a given id;
- POST /api/images - add new image;
- PUT /api/images/<image_id> - update an image with a given id;
- DELETE /api/images/<image_id> - delete an image with a given id;


## Fields:
- id: unique integer identifier;
- image_file: base64 bytes object;
- date_uploaded: date when record was created (datetime object);
- filename: name of the file as string;

For testing purposes setup.py file is provided. It creates a test database and populates it with data for images from test_images folder.
