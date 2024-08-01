import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class Vehicles(Base):
    __tablename__ = 'vehicles'
    # Here we define columns for the table vehicles
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    model = Column(String(250), nullable=False)
    vehicle_class = Column(String(250), nullable=False)
    manufacturer = Column(String(250), nullable=False)
    cost_in_credits = Column(Integer, nullable=True)


class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table user
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(50), nullable=False)
    diameter = Column(String(50), nullable=False)
    rotation_periodr = Column(Integer, nullable=True)
    orbital_period = Column(Integer, nullable=True)
    gravity = Column(String(50), nullable=True)
    population = Column(String(50), nullable=True)

class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table user
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    birth_year = Column(String(50), nullable=False)
    eye_color = Column(String(20), nullable=False)
    mass = Column(String(20), nullable=False)
    hair_color = Column(String(20), nullable=False)
    skin_color = Column(String(20), nullable=False)
    homeworld = Column(String(100), nullable=False)

    #characters Relations

    vehicles_id = Column(Integer, ForeignKey('vehicles.id'))
    vehicles = relationship(Vehicles)

    planets_id = Column(Integer, ForeignKey('planets.id'))
    planets = relationship(Planets)

class Users(Base):
    __tablename__ = 'users'
    # Here we define columns for the table user
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

    #Users Relations
  	
    favorites_characters = Column(Integer, ForeignKey('characters.id'))
    characters = relationship(Characters)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
