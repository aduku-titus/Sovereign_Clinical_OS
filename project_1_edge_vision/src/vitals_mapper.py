from datetime import datetime


class GeriatricMapper:
    def process(self, raw):
        nums = raw["numbers"]
        keys = [k.upper() for k in raw["keywords"]]
        packet = {"timestamp": datetime.now().isoformat()}

        # 1. Cardiovascular (Hypertension)
        # Assuming the first two large numbers are BP
        bp_candidates = [n for n in nums if n > 40]
        if len(bp_candidates) >= 2:
            packet["blood_pressure"] = {
                "sys": bp_candidates[0],
                "dia": bp_candidates[1],
            }

        # 2. Pulse & SpO2
        packet["pulse"] = {"value": next((n for n in nums if 40 <= n <= 140), 72)}
        packet["spo2"] = {"value": next((n for n in nums if 85 <= n <= 100), 95)}

        # 3. Respiration (Critical for Sepsis/Pneumonia in Elderly)
        packet["respiration_rate"] = {
            "value": next((n for n in nums if 10 <= n <= 35), 18)
        }

        # 4. Metabolic (Diabetes)
        # Looking for numbers in mmol/L (typical 4.0 - 20.0)
        packet["glucose"] = {
            "value": next((n for n in nums if 3.0 <= n <= 25.0), 5.5),
            "unit": "mmol/L",
        }

        # 5. Neurological (Glasgow Coma Scale - Dementia/Delirium)
        # GCS is 3-15. We look for a keyword GCS.
        if "GCS" in keys:
            packet["gcs"] = {"score": next((n for n in nums if 3 <= n <= 15), 15)}

        # 6. Elimination (Renal & Gastro - Critical Geriatric Indicators)
        packet["urine_output"] = {
            "value": next((n for n in nums if n > 100), 450),
            "unit": "mL",
        }
        packet["bowel_movement"] = {
            "days_since": next((n for n in nums if 0 <= n <= 10), 1)
        }

        return packet
