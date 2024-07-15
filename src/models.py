import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()
    
class Usuario(Base):
    __tablename__ = 'Usuario'
    ID = Column(Integer, primary_key=True)
    contrasena = Column(String(20))
    username = Column(String(12))
    nombre = Column(String(10))
    apellidos = Column(String(15))
    email = Column(String(25))
    favoritos = Column(Integer, ForeignKey('Favoritos.id_favorito'))

class Favoritos(Base):
    __tablename__ = 'Favoritos'
    id_favorito = Column(Integer, primary_key=True)
    id_planeta = Column(Integer, ForeignKey('Planeta.id_planeta'), nullable=True)
    id_personaje = Column(Integer, ForeignKey('Personaje.id_personaje'), nullable=True)

class Planeta(Base):
    __tablename__ = 'Planeta'
    id_planeta = Column(Integer, primary_key=True)
    nombre = Column(String(25))
    descripcion = Column(String(2000))
    foto = Column(String)

class Personaje(Base):
    __tablename__ = 'Personaje'
    id_personaje = Column(Integer, primary_key=True)
    nombre = Column(String(25))
    descripcion = Column(String(2000))
    foto = Column(String)



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
