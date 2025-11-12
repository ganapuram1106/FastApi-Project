from sqlalchemy.orm import Session
from app import models, schemas
from datetime import datetime

def get_robot_by_robot_id(db: Session, robot_id: str):
    return db.query(models.Robot).filter(models.Robot.robot_id == robot_id).first()

def create_robot(db: Session, robot: schemas.RobotCreate):
    db_robot = models.Robot(robot_id=robot.robot_id, location=robot.location)
    db.add(db_robot)
    db.commit()
    db.refresh(db_robot)
    return db_robot

def create_telemetry(db: Session, robot: models.Robot, telemetry: schemas.TelemetryCreate):
    db_tm = models.Telemetry(
        robot_db_id=robot.id,
        battery_level=telemetry.battery_level,
        temperature=telemetry.temperature,
        timestamp=datetime.utcnow()
    )
    db.add(db_tm)
    db.commit()
    db.refresh(db_tm)
    return db_tm

def get_all_robots(db: Session):
    return db.query(models.Robot).all()

def get_telemetry_for_robot(db: Session, robot: models.Robot):
    return db.query(models.Telemetry).filter(models.Telemetry.robot_db_id == robot.id).order_by(models.Telemetry.timestamp.desc()).all()
