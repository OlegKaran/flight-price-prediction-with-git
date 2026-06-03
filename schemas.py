from pydantic import BaseModel
from datetime import date

class FlightInfo(BaseModel):
    depart_date: date
    origin: str
    destination: str
    number_of_changes: int

class PriceResponse(BaseModel):
    found_at: str
    depart_date: str
    route: str
    number_of_changes: int
    predicted_price: int
    prediction_time_ms: str
    currency: str = 'RUB'