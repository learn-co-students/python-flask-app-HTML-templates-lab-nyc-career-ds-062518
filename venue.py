from base import Base
from sqlalchemy import *
from sqlalchemy.orm import relationship

class Venue(Base):
    __tablename__ = 'venues'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    capacity = Column(Integer)
    city_id = Column(Integer, ForeignKey('cities.id'))
    city = relationship("City", back_populates = 'venues')
    shows = relationship("Show", back_populates = 'venue')
