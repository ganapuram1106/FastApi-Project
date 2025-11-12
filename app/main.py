from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Robot Telemetry Management API")  # <- Must exist here, top-level


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/robots", response_model=schemas.RobotOut, status_code=status.HTTP_201_CREATED)
def create_robot(robot: schemas.RobotCreate, db: Session = Depends(get_db)):
    existing = crud.get_robot_by_robot_id(db, robot.robot_id)
    if existing:
        raise HTTPException(status_code=400, detail="Robot with this robot_id already exists")
    return crud.create_robot(db, robot)


@app.post("/robots/{robot_id}/telemetry", response_model=schemas.TelemetryOut, status_code=status.HTTP_201_CREATED)
def add_telemetry(robot_id: str, telemetry: schemas.TelemetryCreate, db: Session = Depends(get_db)):
    robot = crud.get_robot_by_robot_id(db, robot_id)
    if not robot:
        raise HTTPException(status_code=404, detail="Robot not found")
    return crud.create_telemetry(db, robot, telemetry)


@app.get("/robots", response_model=list[schemas.RobotOut])
def read_robots(db: Session = Depends(get_db)):
    return crud.get_all_robots(db)


@app.get("/robots/{robot_id}/telemetry", response_model=list[schemas.TelemetryOut])
def read_telemetry(robot_id: str, db: Session = Depends(get_db)):
    robot = crud.get_robot_by_robot_id(db, robot_id)
    if not robot:
        raise HTTPException(status_code=404, detail="Robot not found")
    return crud.get_telemetry_for_robot(db, robot)
