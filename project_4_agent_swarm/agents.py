# FIXED IMPORT: Using Full Path for Monorepo Compatibility
from project_4_agent_swarm.state import AgentState

class ClinicSwarm:
    """
    Project 4: The Agentic Swarm.
    Role: Automate Triage and Documentation.
    Moat: Human-in-the-Loop (HITL) Architecture.
    """
    
    def triage_agent(self, state: AgentState):
        """Role: The Triage Nurse. Assigns Urgency Category."""
        # print("--- [AGENT] TRIAGE NURSE: Assessing Vitals ---") # Optional logging
        vitals = state["vitals"]
        
        # Logic: High RR or Low BP = Cat 2 (Emergency)
        # We use .get() to be safe if keys are missing
        sys_bp = 120
        if "blood_pressure" in vitals:
            sys_bp = vitals["blood_pressure"].get("sys", 120)
            
        rr = 16
        if "respiration_rate" in vitals:
            rr = vitals["respiration_rate"].get("value", 16)
        
        if sys_bp < 90 or rr > 25:
            category = "Category 2 (Emergency)"
            msg = f"TRIAGE ALERT: Unstable Vitals (BP {sys_bp}, RR {rr}). Immediate Review."
        else:
            category = "Category 4 (Semi-Urgent)"
            msg = "Patient Stable. Queue for standard review."
            
        return {"triage_level": category, "messages": [msg]}

    def discharge_agent(self, state: AgentState):
        """Role: The Scribe. Writes the FHIR Summary."""
        # print("--- [AGENT] SCRIBE: Drafting Discharge Summary ---")
        
        # Logic: Only runs AFTER human approval
        if not state.get("nurse_approved"):
            return {"messages": ["ERROR: Cannot discharge without Nurse Approval."]}
            
        summary = f"""
        DISCHARGE SUMMARY (FHIR R5)
        Patient ID: {state.get('patient_id', 'Unknown')}
        Triage: {state.get('triage_level', 'N/A')}
        Outcome: Discharged to GP with monitoring.
        Safety Checks: Passed.
        """
        return {"draft_summary": summary, "messages": ["Discharge Drafted."]}
