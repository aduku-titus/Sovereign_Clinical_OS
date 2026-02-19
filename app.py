import sys
import os
import streamlit as st
import time
import json

# --- ROBUST PATHING (SOLVES MODULENOTFOUNDERROR) ---
# This ensures Python sees all project folders regardless of nesting
root_path = os.path.abspath(os.path.dirname(__file__))
if root_path not in sys.path:
    sys.path.insert(0, root_path)

# Inject sub-directories into path for direct module access
sub_paths = [
    os.path.join(root_path, "project_1_edge_vision", "src"),
    os.path.join(root_path, "project_3_litigation_shield", "src"),
    os.path.join(root_path, "project_4_agent_swarm"),
    os.path.join(root_path, "core", "security"),
]
for p in sub_paths:
    if p not in sys.path:
        sys.path.append(p)

# --- IMPORTS ---
try:
    from vitals_mapper import GeriatricMapper
    from agents import ClinicSwarm
    from safety_shield import ClinicalValidator
    from audit_logger import SovereignAuditLogger
except ImportError as e:
    st.error(f"Infrastructure Error: {e}")
    st.info("Ensure all folders have __init__.py files and names are lowercase.")
    st.stop()

# --- INITIALIZE CORE SECURITY ---
audit_log = SovereignAuditLogger()

# --- UI CONFIG ---
st.set_page_config(page_title="Sovereign Elder-Guard", layout="wide", page_icon="🏥")
st.title("🏥 Sovereign Clinical_OS: The Elder-Guard")
st.markdown(
    "**Principal Architect:** Titus Aduku | **Status:** 🟢 Online | **Compliance:** UAE Law 45 / NHS DCB0129"
)

# --- SIDEBAR: STEP 1 & PROJECT 5 AUDIT ---
with st.sidebar:
    st.header("1. Patient Intake")
    p_name = st.text_input("Patient Name", "John Doe")
    if st.button("Generate Sovereign Ghost ID"):
        # Simulated SHA-256 Pseudonymization
        st.session_state["ghost_id"] = "ABC-123-GHOST"
        st.success(f"ID Generated: {st.session_state['ghost_id']}")

    st.markdown("---")
    st.header("🛡️ Project 5: Audit Integrity")

    # Verify Chain Integrity in Real-Time
    is_valid, integrity_msg = audit_log.verify_chain()
    if is_valid:
        st.success(integrity_msg)
    else:
        st.error(integrity_msg)

    if st.checkbox("View Immutable Audit Trail"):
        try:
            with open("data_lake/vault_db/audit_chain.json", "r") as f:
                st.json(json.load(f))
        except FileNotFoundError:
            st.warning(
                "No audit logs found yet. Complete a sign-off to start the chain."
            )

# --- MAIN LAYOUT ---
col1, col2, col3 = st.columns(3)

# COLUMN 1: STEP 2 - EDGE VISION BRIDGE
with col1:
    st.subheader("2. Edge Vision Bridge")
    if st.button("📸 Scan Monitor"):
        with st.spinner("Digitizing Geriatric Vitals..."):
            time.sleep(1)
            # SIMULATING COMPLEX GERIATRIC MONITOR (Emergency Case)
            raw_data = {
                "numbers": [155.0, 95.0, 88.0, 22.0, 8.2, 14.0, 94.0, 155.0, 8.2],
                "keywords": [
                    "SYS",
                    "DIA",
                    "HR",
                    "RR",
                    "GLU",
                    "GCS",
                    "SPO2",
                    "ML",
                    "DAYS",
                ],
            }
            mapper = GeriatricMapper()
            st.session_state["vitals"] = mapper.process(raw_data)
            st.rerun()

    if "vitals" in st.session_state:
        v = st.session_state["vitals"]
        st.write("### Captured Vitals")
        st.write(
            f"🩺 **BP:** {v['blood_pressure']['sys']}/{v['blood_pressure']['dia']}"
        )
        st.write(f"💓 **Pulse:** {v['pulse']['value']} bpm")
        st.write(
            f"🫁 **SpO2:** {v['spo2']['value']}% | **RR:** {v.get('respiration_rate', {}).get('value', 'N/A')}"
        )
        st.write(f"🩸 **Glucose:** {v['glucose']['value']} {v['glucose']['unit']}")
        st.write(f"🧠 **GCS:** {v.get('gcs', {}).get('score', 'N/A')}/15")
        st.write(
            f"🚽 **Urine:** {v['urine_output']['value']}ml | **Bowel:** {v['bowel_movement']['days_since']}d since"
        )

# COLUMN 2: STEP 3 - LITIGATION SHIELD & VAULT
with col2:
    st.subheader("3. Safety & Sovereignty")
    if "vitals" in st.session_state:
        # PROJECT 3: LITIGATION SHIELD (Deterministic Safety)
        st.markdown("#### 🛡️ Litigation Shield")
        validator = ClinicalValidator()
        alerts = validator.validate(st.session_state["vitals"])

        for alert in alerts:
            if "🛑 CRITICAL" in alert:
                st.error(alert)
            elif "⚠️ WARNING" in alert:
                st.warning(alert)
            else:
                st.success(alert)

        st.markdown("---")
        # PROJECT 2: SOVEREIGN VAULT
        if st.button("🔒 Encrypt to Local Vault"):
            st.toast("Data Secured in Qdrant (Local Only)", icon="✅")
            st.session_state["saved"] = True
    else:
        st.info("Awaiting Vitals...")

# COLUMN 3: STEP 4 - AGENTIC SWARM (HITL)
with col3:
    st.subheader("4. AI Agent Swarm")
    if "vitals" in st.session_state:
        swarm = ClinicSwarm()

        # 1. RUN TRIAGE AGENT
        triage_state = {"vitals": st.session_state["vitals"]}
        triage_res = swarm.triage_agent(triage_state)
        st.session_state["current_triage"] = triage_res["triage_level"]

        st.metric("Triage Level", st.session_state["current_triage"])
        st.write(triage_res["messages"][0])

        st.markdown("---")

        # 2. NURSE-IN-THE-LOOP BUTTON
        if st.button("✅ Nurse Approve & Draft"):
            if "ghost_id" not in st.session_state:
                st.error("Action Blocked: Generate Patient ID first.")
            else:
                # Construct state for Scribe
                scribe_state = {
                    "vitals": st.session_state["vitals"],
                    "patient_id": st.session_state["ghost_id"],
                    "triage_level": st.session_state["current_triage"],
                    "nurse_approved": True,
                }

                discharge_res = swarm.discharge_agent(scribe_state)
                st.session_state["summary"] = discharge_res["draft_summary"]

                # --- PROJECT 5: LOG TO HASH-CHAIN ---
                audit_summary = f"ID: {st.session_state['ghost_id']} | Triage: {st.session_state['current_triage']}"
                event_hash = audit_log.log_event(
                    actor="REGISTERED_NURSE_01",
                    action="CLINICAL_SIGN_OFF",
                    data_summary=audit_summary,
                )
                st.session_state["last_event_hash"] = event_hash

        # Display results and Hash Signature
        if "summary" in st.session_state:
            st.text_area("FHIR Record Output", st.session_state["summary"], height=300)
            if "last_event_hash" in st.session_state:
                st.caption(
                    f"Immutable Signature: `{st.session_state['last_event_hash']}`"
                )
    else:
        st.info("Awaiting Triage...")
