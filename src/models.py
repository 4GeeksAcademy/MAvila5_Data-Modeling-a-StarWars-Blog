import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}

####


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False, unique=True)
    email = Column(String(250), nullable=False, unique=True)
    hashed_password = Column(String(250), nullable=False)


class Peoples(Base):
    __tablename__ = 'peoples'
    id = Column(Integer, primary_key=True)
    people_name = Column(String(250), nullable=False)
    gender = Column(String(50))
    homeworld = Column(Integer, ForeignKey('planets.id'))
    vehicles = relationship('Vehicles', secondary='peoples_vehicles')
    films = relationship('Film', secondary='peoples_films')


class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(250), nullable=False)
    gravity = Column(String(100))
    residents = relationship('Peoples', secondary='planet_residents')
    films = relationship('Film', secondary='planet_films')


class UserFavorites(Base):
    __tablename__ = 'user_favorites'
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    fav_people = Column(Integer, ForeignKey('peoples.id'))
    fav_planet = Column(Integer, ForeignKey('planets.id'))
    fav_vehicle = Column(Integer, ForeignKey('vehicles.id'))
    fav_film = Column(Integer, ForeignKey('film.id'))


class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250))
    vehicle_class = Column(String(100))
    films = relationship('Film', secondary='vehicles_films')


class Film(Base):
    __tablename__ = 'film'
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    characters = relationship('Peoples', secondary='films_peoples')
    planets = relationship('Planets', secondary='films_planets')
    vehicles = relationship('Vehicles', secondary='films_vehicles')


# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
