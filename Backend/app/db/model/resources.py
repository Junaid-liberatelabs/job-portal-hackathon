from sqlalchemy import Column, String, DateTime, Enum, ARRAY, Float, Tuple

class Resources(Base):
    __tablename__ = "resources"
    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    url = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    def __repr__(self):
        return f"<Resources(id={self.id}, name={self.name}, description={self.description}, url={self.url})>"