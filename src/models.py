import os
import sys
from sqlalchemy import Table, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


favorite_planets = Table(
    'favorite_planets', Base.metadata,
     Column('user_id', Integer, ForeignKey('users.id'), primary_key=True),
     Column('planets_id', Integer, ForeignKey('planets.id'),primary_key=True)
)

favorite_characters = Table(
    'favorite_characters', Base.metadata,
     Column('user.id', Integer, ForeignKey('users.id'),primary_key=True),
     Column('characters_id', Integer, ForeignKey('characters.id'),primary_key=True)
)

favorite_vehicles = Table(
    'favorite_vehicles', Base.metadata,
     Column('user.id', Integer, ForeignKey('users.id'),primary_key=True),
     Column('vehicles_id', Integer, ForeignKey('vehicles.id'),primary_key=True)
)


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
    favorite_planets = relationship('Planets', secondary=favorite_planets, backref= 'favorited_by')
    favorite_characters = relationship('Characters', secondary=favorite_characters, backref= 'favorited_by')
    favorite_vehicles = relationship('Vehicles', secondary=favorite_vehicles, backref= 'favorited_by')
    # favorites_characters = Column(Integer, ForeignKey('characters.id'))
    # characters = relationship(Characters)


def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
