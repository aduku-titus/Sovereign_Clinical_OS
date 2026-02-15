import streamlit as st
import sys
import os
import time

# --- BRIDGE SETUP ---
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from project_1_edge_vision.src.vitals_mapper import GeriatricMapper
from project_1_edge_vision.src.safety_shield import ClinicalValidator
from core.security.hasher import SovereignScrubber
from data_lake.embeddings.sovereign_engine import SovereignBrain
from data_lake.vector_db.sovereign_vault import SovereignVault

# Import Project 4 (The Swarm)
from project_4_agent_swarm.agents import ClinicSwarm

# --- UI CONFIG ---
st.set_page_config(page_title="Sovereign Elder-Guard", layout="wide", page_icon="🏥")
st.title("🏥 Sovereign Clinical_OS: The Elder-Guard")
st.markdown(
    "**Principal Architect:** Titus Aduku | **Status:** 🟢 Online (Local-Only) | **Compliance:** UAE Law 45"
)

# --- SIDEBAR: IDENTITY ---
with st.sidebar:
    st.header("1. Patient Intake")
    p_name = st.text_input("Patient Name", "John Doe")
    p_dob = st.text_input("DOB", "1950-01-01")

    if st.button("Generate Sovereign Ghost ID"):
        scrubber = SovereignScrubber()
        ghost_id = scrubber.anonymize_id(p_name, p_dob)
        st.session_state["ghost_id"] = ghost_id
        st.success(f"UUID: {ghost_id}")
        st.caption("SHA-256 Deterministic Anonymization Active")

# --- MAIN LAYOUT ---
col1, col2, col3 = st.columns(3)

# COLUMN 1: SENSORY INPUT (Project 1)
with col1:
    st.subheader("2. Edge Vision Bridge")
    st.info("Digitizing Analog Signals...")

    if st.button("📸 Scan Monitor"):
        with st.spinner("Processing via OpenCV..."):
            time.sleep(1)
            # Simulated 'Sepsis' Scan
            raw_ocr = {
                "numbers": [150.0, 95.0, 92.0, 26.0, 110.0, 38.5, 20.0, 300.0, 4.0],
                "keywords": [
                    "SYS",
                    "DIA",
                    "SPO2",
                    "RR",
                    "HR",
                    "TEMP",
                    "MMSE",
                    "ML",
                    "DAYS",
                ],
            }
            mapper = GeriatricMapper()
            vitals = mapper.process(raw_ocr)
            st.session_state["vitals"] = vitals
            st.json(vitals)

# COLUMN 2: SAFETY & STORAGE (Project 2 & 3)
with col2:
    st.subheader("3. Safety & Sovereignty")

    if "vitals" in st.session_state:
        # Run Shield
        validator = ClinicalValidator()
        alerts = validator.validate(st.session_state["vitals"])

        st.markdown("#### 🛡️ Litigation Shield")
        for alert in alerts:
            if "CRITICAL" in alert:
                st.error(alert)
            elif "WARNING" in alert:
                st.warning(alert)
            else:
                st.success(alert)

        st.markdown("---")
        # Run Vault
        if st.button("🔒 Encrypt to Local Vault"):
            if "ghost_id" in st.session_state:
                vault = SovereignVault()
                brain = SovereignBrain()

                # Semantic Embedding
                note = f"Patient vitals: {st.session_state['vitals']}. Alerts: {alerts}"
                vector = brain.vectorize_clinical_note(note)

                # Deposit
                vault.deposit_vitals(
                    st.session_state["ghost_id"], vector, st.session_state["vitals"]
                )
                st.toast("Data Secured in Docker Vault", icon="✅")
            else:
                st.error("Missing Ghost ID")

# COLUMN 3: AGENTIC SWARM (Project 4)
with col3:
    st.subheader("4. AI Agent Swarm")
    st.info("Automating Documentation...")

    if "vitals" in st.session_state:
        # Initialize Swarm
        swarm = ClinicSwarm()

        # 1. Triage Agent
        triage_state = {
            "vitals": st.session_state["vitals"],
            "patient_id": st.session_state.get("ghost_id", "Unknown"),
        }
        triage_result = swarm.triage_agent(triage_state)

        st.markdown(f"**Triage Level:** `{triage_result['triage_level']}`")
        st.write(triage_result["messages"][0])

        st.markdown("---")

        # 2. HITL (Human-in-the-Loop) PAUSE
        st.write("🤖 **Scribe Agent is ready to draft.**")

        # This is the "AHPRA/UAE Law" Compliance Button
        if st.button("✅ Nurse Approve & Draft"):
            # 3. Discharge Agent (Only runs after click)
            scribe_state = {**triage_state, **triage_result, "nurse_approved": True}
            discharge_result = swarm.discharge_agent(scribe_state)

            st.text_area(
                "FHIR Discharge Summary", discharge_result["draft_summary"], height=200
            )
            st.success("Documentation Complete. 40% Shift Time Reclaimed.")
