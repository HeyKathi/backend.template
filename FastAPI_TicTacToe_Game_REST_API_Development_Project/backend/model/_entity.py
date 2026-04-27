from sqlalchemy import Column, Integer, String
from ..engine.database import Base


class Entity(Base):

    __tablename__ = "games"

    id = Column(Integer, primary_key=True)
    board = Column(String, default="---------")
    current_player = Column(String, default="X")
    status = Column(String, default="ongoing")