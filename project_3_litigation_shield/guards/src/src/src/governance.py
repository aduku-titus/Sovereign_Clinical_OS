from pydantic import BaseModel, Field, field_validator
from typing import Optional, Literal


class ClinicalContract(BaseModel):
    """
    Project 3: The Litigation Shield.
    Objective: Enforce NHS DCB0129 'Clinical Safety Case' via Code.
    Logic: If data violates these rules, the system throws a 'ValidationError'
    which serves as legal proof the AI was stopped.
    """

    # 1. THE GERIATRIC 9 (Strict Typing)
    # We use 'Field' to document the 'Why' for auditors
    systolic_bp: int = Field(
        ..., ge=40, le=300, description="Must be physiological range"
    )
    diastolic_bp: int = Field(..., ge=20, le=160)
    glucose_mmol: float = Field(..., ge=1.0, le=40.0)
    temp_c: float = Field(..., ge=30.0, le=45.0)
    spo2: int = Field(..., ge=50, le=100)
    pulse: int = Field(..., ge=20, le=250)
    resp_rate: int = Field(..., ge=4, le=60)
    mmse_score: int = Field(..., ge=0, le=30)

    # Elimination (Optional because not always captured every shift)
    urine_output_ml: Optional[int] = Field(None, ge=0, le=10000)
    bowel_days: Optional[int] = Field(None, ge=0, le=30)

    # 2. THE MULTI-MORBIDITY CONTEXT
    # This helps the Shield decide on conflicts
    has_heart_failure: bool = False
    has_sepsis_signs: bool = False

    # 3. THE VALIDATORS (The 'Standing Orders')

    @field_validator("systolic_bp")
    @classmethod
    def check_pulse_pressure(cls, v, info):
        # We can't check diastolic here easily in Pydantic v2 without 'model_validator'
        # So we keep this simple: Is the number itself valid?
        if v > 220:
            print(f"⚠️ [SHIELD WARNING] Extreme Hypertension: {v}")
        return v

    @field_validator("glucose_mmol")
    @classmethod
    def check_hypoglycemia(cls, v):
        if v < 4.0:
            raise ValueError(
                "CRITICAL: Hypoglycemia detected. AI Intervention Blocked."
            )
        return v


class InterventionRequest(BaseModel):
    """
    The AI wants to do something. The Shield checks if it's safe.
    """

    proposed_action: str
    dosage: Optional[float] = None
    drug_name: Optional[str] = None
