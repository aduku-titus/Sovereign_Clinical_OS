import sys
import os

# Ensure the system can find our core and data_lake modules
sys.path.append(os.getcwd())

from core.security.hasher import SovereignScrubber
from data_lake.embeddings.sovereign_engine import SovereignBrain
from data_lake.vector_db.sovereign_vault import SovereignVault


def execute_sovereign_deposit():
    # 1. Initialize our Sovereign Tools
    scrubber = SovereignScrubber()
    brain = SovereignBrain()
    vault = SovereignVault()

    # 2. THE DATA (Simulating output from Project 1: The Tatale Bridge)
    patient_name = "Titus Aduku"
    patient_dob = "1990-01-01"

    clinical_vitals = {
        "blood_pressure": "150/95",
        "temp": 38.2,
        "spo2": 92,
        "note": "Patient shows early signs of Sepsis. High fever and tachypnea.",
    }

    # 3. THE SCRUB (Identity Protection - UAE Law 45)
    # FIX: We use 'dob' to match the function definition in hasher.py
    ghost_id = scrubber.anonymize_id(patient_name, dob=patient_dob)
    print(f"\n[VAULT] Identity Anonymized: {ghost_id[:8]}...")

    # 4. THE VECTORIZATION (Semantic Meaning - Multilingual)
    clinical_vector = brain.vectorize_clinical_note(clinical_vitals["note"])
    print("[VAULT] Clinical Meaning Vectorized (1024-Dimensions).")

    # 5. THE DEPOSIT (The Vault)
    # We save the Ghost ID (UUID-compatible), the Math, and the Vitals
    vault.deposit_vitals(
        ghost_id=ghost_id,
        vector=clinical_vector,
        metadata={
            "dept": "Geriatrics",
            "vitals": clinical_vitals,
            "nurse_id": "RN-ADUKU-2026",
        },
    )
    print("--- DEPOSIT SUCCESSFUL: DATA IS SOVEREIGN AND SECURED ---")


if __name__ == "__main__":
    try:
        execute_sovereign_deposit()
    except Exception as e:
        print(f"❌ Deposit Failed: {e}")
