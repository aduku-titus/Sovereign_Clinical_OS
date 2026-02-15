class ClinicalValidator:
    """
    Project 3 Integration: The Litigation Shield (V1.1)
    Physiological Boundaries for the COMPLETE Geriatric 9.
    """

    @staticmethod
    def validate(vitals):
        alerts = []

        # 1. BP (Hypertension)
        if "blood_pressure" in vitals:
            sys, dia = vitals["blood_pressure"]["sys"], vitals["blood_pressure"]["dia"]
            if not (40 <= sys <= 280) or not (20 <= dia <= 160) or sys <= dia:
                alerts.append("BP_INVALID: Check Analog Dial/Cuff placement")

        # 2. BSL (Diabetes)
        if "glucose" in vitals:
            val, unit = vitals["glucose"]["value"], vitals["glucose"]["unit"]
            if (unit == "mmol/L" and val < 4.0) or (unit == "mg/dL" and val < 70):
                alerts.append("GLUCOSE_CRITICAL: Hypoglycemia Risk")

        # 3. SpO2 (Respiratory)
        if "spo2" in vitals and vitals["spo2"]["value"] < 90:
            alerts.append("SPO2_WARNING: Hypoxia Detected")

        # 4. Pulse (Cardiac)
        if "pulse" in vitals:
            p = vitals["pulse"]["value"]
            if p < 50 or p > 110:  # Geriatric specific heart rate norms
                alerts.append(
                    "PULSE_WARNING: Bradycardia/Tachycardia - Check for Arrhythmia"
                )

        # 5. Temp (Infection/Sepsis)
        if "temp" in vitals:
            t = vitals["temp"]["value"]
            if t > 37.5:  # Lower fever threshold for elders
                alerts.append("TEMP_WARNING: Hyperthermia - Potential Sepsis")
            elif t < 35.5:
                alerts.append("TEMP_WARNING: Hypothermia - Systemic Risk")

        # 6. RR (The Silent Killer)
        if "respiration_rate" in vitals:
            rr = vitals["respiration_rate"]["value"]
            if rr < 12 or rr > 24:
                alerts.append(
                    "RR_CRITICAL: Abnormal breathing - Immediate Assessment Required"
                )

        # 7. MMSE (Dementia/Cognition)
        if "mmse" in vitals and vitals["mmse"]["score"] < 24:
            alerts.append(
                "COGNITIVE_ALERT: MMSE Score < 24 - Cognitive Impairment Suspected"
            )

        # 8. Urine Output (Kidney/Hydration)
        if "urine_output" in vitals and vitals["urine_output"]["value"] < 400:
            alerts.append("URINE_CRITICAL: Oliguria - Possible Renal Failure")

        # 9. Bowel Movement (Delirium/GI)
        if "bowel_movement" in vitals and vitals["bowel_movement"]["days_since"] >= 3:
            alerts.append(
                "BOWEL_WARNING: Constipation Risk - Primary Cause of Geriatric Delirium"
            )

        return alerts if alerts else ["All 9 Parameters Validated: Patient Stable"]
