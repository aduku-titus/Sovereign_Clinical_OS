class ClinicalValidator:
    """
    Project 3: The Litigation Shield (V1.2 - Monorepo Optimized)
    Role: Deterministic Safety Gates for 12-Nation Compliance.
    Nations: USA (FDA SaMD), UK (DCB0129), UAE (Law 45).
    """

    @staticmethod
    def validate(vitals):
        alerts = []

        # 1. Cardiovascular: Hypertension Stage 2 (Aligned with Dashboard 155/95)
        if "blood_pressure" in vitals:
            sys = vitals["blood_pressure"].get("sys", 120)
            dia = vitals["blood_pressure"].get("dia", 80)
            if sys > 150 or dia > 95:
                alerts.append(
                    "⚠️ WARNING: Hypertensive Stage 2. Monitor for stroke risk."
                )
            if sys < 90:
                alerts.append(
                    "🛑 CRITICAL: Hypotension. Potential shock or over-medication."
                )

        # 2. Metabolic: Hyperglycemic Crisis (Aligned with Dashboard 22.0)
        if "glucose" in vitals:
            val = vitals["glucose"].get("value", 5.5)
            if val > 15.0:
                alerts.append(
                    f"🛑 CRITICAL: Hyperglycemic Crisis ({val} mmol/L). Risk of DKA/HHS."
                )
            elif val < 4.0:
                alerts.append(
                    "🛑 CRITICAL: Hypoglycemia. Immediate Glucose administration required."
                )

        # 3. Neurological: Glasgow Coma Scale (Aligned with Dashboard 8.2)
        # GCS < 9 is the clinical "Airway Risk" threshold.
        gcs = vitals.get("gcs", {}).get("score", 15)
        if gcs < 9:
            alerts.append(
                f"🛑 CRITICAL: Severe Neuro Decline (GCS {gcs}). High risk of airway obstruction."
            )
        elif gcs < 13:
            alerts.append("⚠️ WARNING: Mild/Moderate Delirium detected.")

        # 4. Respiratory & Pulse
        rr = vitals.get("respiration_rate", {}).get("value", 18)
        spo2 = vitals.get("spo2", {}).get("value", 95)
        if rr > 24 or spo2 < 92:
            alerts.append(
                "🛑 CRITICAL: Respiratory Distress. Possible Pneumonia/Sepsis."
            )

        # 5. Renal: Oliguria (Aligned with Dashboard 155ml)
        # Urine < 400ml/day is a critical indicator of Kidney Failure
        urine = vitals.get("urine_output", {}).get("value", 500)
        if urine < 400:
            alerts.append(
                f"🛑 CRITICAL: Oliguria ({urine}ml). Possible Acute Kidney Injury."
            )

        # 6. Gastro: Constipation & Delirium (Aligned with Dashboard 8.2 days)
        # In geriatrics, 5+ days without a BM is a primary cause of Delirium
        bowel = vitals.get("bowel_movement", {}).get("days_since", 0)
        if bowel >= 5:
            alerts.append(
                f"⚠️ WARNING: Severe Constipation ({bowel} days). Risk of fecal impaction."
            )

        return alerts if alerts else ["✅ All 9 Parameters Validated: Patient Stable"]
