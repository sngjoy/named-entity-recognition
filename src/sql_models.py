from sqlalchemy import Integer, String
from sqlalchemy.sql.schema import Column

from src.database import Base


class EntitiesCount(Base):
    __tablename__ = "entities_count"

    id = Column(Integer, primary_key=True)
    article_id = Column(String, nullable=False)
    entities = Column(String, nullable=False)
    counts = Column(Integer, nullable=False)
