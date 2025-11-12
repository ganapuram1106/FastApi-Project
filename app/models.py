from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Robot(Base):
    __tablename__ = "robots"

    id = Column(Integer, primary_key=True, index=True)
    robot_id = Column(String, unique=True, index=True, nullable=False)
    location = Column(String, nullable=True)

    # One-to-many relationship: one Robot has many Telemetry rows
    telemetry = relationship("Telemetry", back_populates="robot", cascade="all, delete-orphan")


class Telemetry(Base):
    __tablename__ = "telemetry"

    id = Column(Integer, primary_key=True, index=True)
    robot_db_id = Column(Integer, ForeignKey("robots.id", ondelete="CASCADE"), nullable=False)
    battery_level = Column(Float, nullable=False)
    temperature = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Back reference to parent Robot
    robot = relationship("Robot", back_populates="telemetry")
