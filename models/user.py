#!/usr/bin/python3
""" Module to execute the program """

from models.base_model import BaseModel


class User(BaseModel):
    """User class"""

    email = ""  # string - empty string
    password = ""  # string - empty string
    first_name = ""  # string - empty string
    last_name = ""  # string - empty string
