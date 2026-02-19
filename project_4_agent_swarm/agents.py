# FIXED IMPORT: Using Full Path for Monorepo Compatibility
from project_4_agent_swarm.state import AgentState


class ClinicSwarm:
    """
    Project 4: The Agentic Swarm.
    Role: Automate Triage and Documentation.
    Moat: Human-in-the-Loop (HITL) Architecture.
    """

    def triage_agent(self, state: AgentState):
        v = state["vitals"]
        sys_bp = v.get("blood_pressure", {}).get("sys", 120)
        glucose = v.get("glucose", {}).get("value", 5.5)
        gcs = v.get("gcs", {}).get("score", 15)

        # Geriatric Alert Logic
        alerts = []
        is_emergency = False

        if sys_bp > 150:
            alerts.append("Hypertension Detected")
        if glucose > 10.0:
            alerts.append("Hyperglycemia (Diabetes)")
        if gcs < 14:
            alerts.append("Neurological/Dementia Decline (Low GCS)")

        if sys_bp < 90 or gcs < 9 or glucose > 20:
            is_emergency = True

        level = "Category 2 (Emergency)" if is_emergency else "Category 4 (Semi-Urgent)"
        msg = f"Triage Assessment: {', '.join(alerts) if alerts else 'Stable'}. Recommendation: Follow Geriatric Protocol."

        return {"triage_level": level, "messages": [msg]}

    def discharge_agent(self, state: AgentState):
        """Role: The Scribe. Writes the FHIR Summary based on Triage Level."""

        # Safety Check: Only run after Human (Nurse) Approval
        if not state.get("nurse_approved"):
            return {"messages": ["ERROR: Human sign-off required."]}

        v = state["vitals"]
        gcs = v.get("gcs", {}).get("score", 15)
        glucose = v.get("glucose", {}).get("value", 5.5)
        triage = state.get("triage_level", "Unknown")

        # CLINICAL BRANCHING LOGIC
        # If Category 2 (Emergency), we switch from 'Discharge' to 'Urgent Transfer'
        if "Category 2" in triage or gcs < 10 or glucose > 20:
            doc_type = "⚠️ URGENT TRANSFER SUMMARY (FHIR R5)"
            disposition = "EMERGENCY TRANSFER TO ACUTE CARE"
            plan = "Immediate stabilization of Glucose and Neurological monitoring required."
            outcome = "Critical - Not safe for home discharge."
        else:
            doc_type = "📄 DISCHARGE SUMMARY (FHIR R5)"
            disposition = "Discharged to Community Care"
            plan = "Follow-up with GP in 48 hours for co-morbidity review."
            outcome = "Stable - Safe for home discharge."

        summary = f"""
        {doc_type}
        -----------------------------------
        Patient ID: {state.get("patient_id", "Unknown")}
        Triage Level: {triage}
        
        VITAL SIGNS SUMMARY:
        - BP: {v.get("blood_pressure", {}).get("sys")}/{v.get("blood_pressure", {}).get("dia")}
        - Glucose: {glucose} mmol/L
        - GCS: {gcs}/15
        
        CLINICAL OUTCOME: {outcome}
        DISPOSITION: {disposition}
        PLAN: {plan}
        
        [STAMP]: SOVEREIGN CLINICAL_OS - 2026 AUDIT READY
        """
        return {"draft_summary": summary, "messages": ["Documentation Finalized."]}
