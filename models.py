from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, Float, DateTime
from database import Base

# Formats tables. Can also be done in SQL.
class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)

    text = Column(String, nullable=False)
    label = Column(String, nullable=False)
    score = Column(Float, nullable=False)

    created_at = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc)
    )