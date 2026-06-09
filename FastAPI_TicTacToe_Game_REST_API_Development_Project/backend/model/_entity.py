from sqlalchemy import Column, Integer, String, DateTime
from ..engine.database import Base
from datetime import datetime


class Entity(Base):

    __tablename__ = "games"

    id = Column(Integer, primary_key=True)
    board = Column(String, default="---------")
    current_player = Column(String, default="X")
    status = Column(String, default="ongoing")
    created_at = Column(DateTime, default=datetime.now)