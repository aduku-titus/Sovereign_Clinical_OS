import hashlib
import uuid
import os
from dotenv import load_dotenv  # New Import

# Load the secret from the .env file
load_dotenv()


class SovereignScrubber:
    def __init__(self):
        # SECURITY UPGRADE: Fetch from environment, never hard-code
        self.salt = os.getenv("SOVEREIGN_SALT")

        if not self.salt:
            raise ValueError(
                "CRITICAL SECURITY ERROR: Missing SOVEREIGN_SALT in .env file."
            )

    def anonymize_id(self, patient_name: str, dob: str) -> str:
        # ... (Rest of the logic remains the same) ...
        raw_string = f"{patient_name.strip().lower()}{dob}{self.salt}"
        hash_obj = hashlib.sha256(raw_string.encode())
        hash_bytes = hash_obj.digest()[:16]
        return str(uuid.UUID(bytes=hash_bytes))
