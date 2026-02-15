class ConflictResolver:
    """
    The Logic Engine for Multi-Morbidity.
    Solves the 'Sepsis vs Heart Failure' paradox.
    """
    def evaluate_intervention(self, patient_state: dict, ai_proposal: str):
        audit_log = []
        
        has_hf = patient_state.get("has_heart_failure", False)
        has_sepsis = patient_state.get("has_sepsis_signs", False)
        proposal = ai_proposal.lower()
        
        # LOGIC GATE 1: FLUID OVERLOAD
        if "fluid" in proposal or "saline" in proposal:
            if has_hf:
                return "BLOCKED", [f"HAZARD MITIGATED: Fluid restriction active for Heart Failure."]

        # LOGIC GATE 2: HYPOGLYCEMIA
        if "insulin" in proposal:
            glucose = patient_state.get("glucose_mmol", 5.0)
            if glucose < 4.0:
                return "KILLED", [f"NEVER EVENT PREVENTED: Cannot give Insulin when BSL is {glucose}."]

        return "APPROVED", ["Action valid under current protocols."]
