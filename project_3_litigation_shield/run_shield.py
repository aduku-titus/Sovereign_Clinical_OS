import sys
import os

sys.path.append(os.getcwd())

from src.governance import ClinicalContract
from src.conflict_resolver import ConflictResolver
from pydantic import ValidationError


def execute_litigation_defense():
    # SIMULATION: A complex Geriatric Patient
    # Sepsis (needs fluids) + Heart Failure (no fluids) + Hypoglycemia (no insulin)
    raw_patient_data = {
        "systolic_bp": 90,  # Low (Sepsis?)
        "diastolic_bp": 50,
        "glucose_mmol": 3.2,  # Hypo!
        "temp_c": 38.5,  # Fever
        "spo2": 92,
        "pulse": 110,
        "resp_rate": 24,
        "mmse_score": 20,
        "has_heart_failure": True,
        "has_sepsis_signs": True,
    }

    resolver = ConflictResolver()

    print("\n--- PROJECT 3: THE LITIGATION SHIELD ---")

    # PHASE 1: DATA INTEGRITY (The Contract)
    try:
        # We try to force the raw data into our Strict Contract
        # This will Fail because Glucose is 3.2 (Hypo trigger in validator)
        print("[SHIELD] Validating Patient Vitals against Safety Contract...")
        validated_patient = ClinicalContract(**raw_patient_data)
        print("✅ Data Accepted.")
    except ValidationError as e:
        print(f"🛑 CONTRACT VIOLATION: {e}")
        # In a real app, we might stop here, but for the demo, let's proceed to the conflict resolver

    print("\n[SHIELD] Analyzing AI Proposals against Multi-Morbidity Logic...")

    # SCENARIO A: AI suggests Fluids
    ai_action_1 = "Administer 1000ml Normal Saline IV bolus"
    print(f"\n🤖 AI Suggests: '{ai_action_1}'")
    decision, log = resolver.evaluate_intervention(raw_patient_data, ai_action_1)
    print(f"🛡️ SHIELD DECISION: {decision}")
    print(f"📝 AUDIT LOG: {log[0]}")

    # SCENARIO B: AI suggests Insulin
    ai_action_2 = "Give 5 units Insulin"
    print(f"\n🤖 AI Suggests: '{ai_action_2}'")
    decision, log = resolver.evaluate_intervention(raw_patient_data, ai_action_2)
    print(f"🛡️ SHIELD DECISION: {decision}")
    print(f"📝 AUDIT LOG: {log[0]}")


if __name__ == "__main__":
    execute_litigation_defense()
