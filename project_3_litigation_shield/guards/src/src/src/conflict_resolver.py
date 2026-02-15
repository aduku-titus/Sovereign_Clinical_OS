class ConflictResolver:
    """
    The Logic Engine for Multi-Morbidity.
    Solves the 'Sepsis vs Heart Failure' paradox.
    """

    def evaluate_intervention(self, patient_state: dict, ai_proposal: str):
        audit_log = []
        decision = "APPROVED"

        # 1. Parse the Patient State
        has_hf = patient_state.get("has_heart_failure", False)
        has_sepsis = patient_state.get("has_sepsis_signs", False)

        # 2. Parse the AI Proposal (Simple keyword matching for MVP)
        proposal = ai_proposal.lower()

        # --- LOGIC GATE 1: FLUID OVERLOAD RISK ---
        if "fluid" in proposal or "saline" in proposal:
            if has_sepsis and has_hf:
                decision = "BLOCKED"
                reason = "CONFLICT: Sepsis requires fluids, but Heart Failure prohibits rapid infusion."
                mitigation = "SUGGESTION: Use Vasopressors instead of heavy fluids. Consult Senior MD."
                audit_log.append(f"HAZARD MITIGATED: {reason} -> {mitigation}")
                return decision, audit_log

            if has_hf:
                decision = "BLOCKED"
                reason = "SAFETY: Fluid restriction active for Heart Failure."
                audit_log.append(f"HAZARD MITIGATED: {reason}")
                return decision, audit_log

        # --- LOGIC GATE 2: HYPOGLYCEMIA RISK ---
        if "insulin" in proposal:
            glucose = patient_state.get("glucose_mmol", 5.0)
            if glucose < 4.0:
                decision = "KILLED"
                reason = f"CRITICAL: Cannot give Insulin when BSL is {glucose}."
                audit_log.append(f"NEVER EVENT PREVENTED: {reason}")
                return decision, audit_log

        return "APPROVED", ["Action valid under current protocols."]
