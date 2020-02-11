# -*- coding: utf-8 -*-
"""
    run.py
    ~~~~~~

    Module to run the application.
"""

from image_app import create_app

app = create_app("config.py")


if __name__ == "__main__":
    app.run(debug=True)
