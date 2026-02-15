from pydantic import BaseModel, Field, field_validator
from typing import Optional

class ClinicalContract(BaseModel):
    """
    Project 3: The Litigation Shield.
    Enforce NHS DCB0129 'Clinical Safety Case' via Code.
    """
    systolic_bp: int = Field(..., ge=40, le=300)
    diastolic_bp: int = Field(..., ge=20, le=160)
    glucose_mmol: float = Field(..., ge=1.0, le=40.0)
    temp_c: float = Field(..., ge=30.0, le=45.0)
    spo2: int = Field(..., ge=50, le=100)
    pulse: int = Field(..., ge=20, le=250)
    resp_rate: int = Field(..., ge=4, le=60)
    mmse_score: int = Field(..., ge=0, le=30)
    
    has_heart_failure: bool = False
    has_sepsis_signs: bool = False

    @field_validator('glucose_mmol')
    @classmethod
    def check_hypoglycemia(cls, v):
        if v < 4.0:
            raise ValueError("CRITICAL: Hypoglycemia detected. AI Intervention Blocked.")
        return v
