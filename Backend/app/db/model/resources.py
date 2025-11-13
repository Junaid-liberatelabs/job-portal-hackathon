from sqlalchemy import Column, String, DateTime, ARRAY, func
from pgvector.sqlalchemy import Vector
from app.db.base import Base
import uuid


class Resource(Base):
    __tablename__ = "resources"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    url = Column(String, nullable=False)
    tags = Column(ARRAY(String), nullable=True, default=list, server_default="{}")
    # pricing_tag = Column(
    #     ENUM("Free", "Paid"), nullable=False, default="Free", server_default="Free"
    # # )
    created_at = Column(
        DateTime, nullable=False, default=func.now(), server_default=func.now()
    )
    updated_at = Column(
        DateTime,
        nullable=False,
        default=func.now(),
        onupdate=func.now(),
        server_default=func.now(),
    )
    embedding = Column(Vector(384), nullable=True)


    def __repr__(self):
        return f"<Resource(id={self.id}, name={self.name}, url={self.url}, tags={self.tags})>"
