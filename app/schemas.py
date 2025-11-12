from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

# Base schema for telemetry data
class TelemetryBase(BaseModel):
    battery_level: float
    temperature: float

# Schema used when creating telemetry (input)
class TelemetryCreate(TelemetryBase):
    pass

# Schema used for output (response)
class TelemetryOut(TelemetryBase):
    id: int
    timestamp: datetime

    # Pydantic v2: enable reading from ORM models
    model_config = {"from_attributes": True}


# Base schema for robot
class RobotBase(BaseModel):
    robot_id: str
    location: Optional[str] = None

# Schema used when creating a robot (input)
class RobotCreate(RobotBase):
    pass

# Schema used for output (response)
class RobotOut(RobotBase):
    id: int
    telemetry: List[TelemetryOut] = []

    # Pydantic v2: enable reading from ORM models
    model_config = {"from_attributes": True}
