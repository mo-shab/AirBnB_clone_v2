#!/usr/bin/python3
""" Review module for the HBNB project """
from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
import models
from models.city import City


class Review(BaseModel):
    """ Review classto store review information """
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        __tablename__ = "reviews"
        text = Column(String(1024), nullable = False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""
