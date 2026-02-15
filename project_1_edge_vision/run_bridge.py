import json
from src.vitals_mapper import GeriatricMapper
from src.safety_shield import ClinicalValidator


def execute_full_audit():
    # Simulate a Nurse's daily round at Tatale
    # BP 150/95, SpO2 92, RR 22, Pulse 105, Temp 38.1 (Sepsis Signs!)
    # MMSE 20 (Dementia), Urine 300ml, 4 Days since BM
    raw_ocr = {
        "numbers": [150.0, 95.0, 92.0, 22.0, 105.0, 38.1, 20.0, 300.0, 4.0],
        "keywords": ["SYS", "DIA", "SPO2", "RR", "HR", "TEMP", "MMSE", "ML", "DAYS"],
    }

    mapper = GeriatricMapper()
    validator = ClinicalValidator()

    vitals = mapper.process(raw_ocr)
    safety_audit = validator.validate(vitals)

    print("\n[SOVEREIGN_OS] PROJECT 1: FULL GERIATRIC 9 AUDIT")
    print(json.dumps(vitals, indent=2))
    print("\n[SOVEREIGN_OS] LITIGATION SHIELD ALERTS:")
    for alert in safety_audit:
        print(f"!! {alert}")


if __name__ == "__main__":
    execute_full_audit()
