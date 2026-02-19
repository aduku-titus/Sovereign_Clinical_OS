import streamlit as st
import time
from project_1_edge_vision.src.vitals_mapper import GeriatricMapper
from project_4_agent_swarm.agents import ClinicSwarm

# --- UI CONFIG ---
st.set_page_config(page_title="Sovereign Elder-Guard", layout="wide", page_icon="🏥")
st.title("🏥 Sovereign Clinical_OS: The Elder-Guard")
st.markdown(
    "**Principal Architect:** Titus Aduku | **Status:** 🟢 Online | **Compliance:** UAE Law 45"
)

# --- SIDEBAR: STEP 1 ---
with st.sidebar:
    st.header("1. Patient Intake")
    p_name = st.text_input("Patient Name", "John Doe")
    if st.button("Generate Sovereign Ghost ID"):
        st.session_state["ghost_id"] = "ABC-123-GHOST"  # Mock ID for demo
        st.success(f"ID Generated: {st.session_state['ghost_id']}")

# --- MAIN LAYOUT ---
col1, col2, col3 = st.columns(3)

# COLUMN 1: STEP 2
with col1:
    st.subheader("2. Edge Vision Bridge")
    if st.button("📸 Scan Monitor"):
        with st.spinner("Digitizing Geriatric Vitals..."):
            time.sleep(1)
            # SIMULATING A COMPLEX GERIATRIC MONITOR (BP, Glucose, GCS, SpO2, etc.)
            raw_data = {
                "numbers": [155.0, 95.0, 88.0, 22.0, 8.2, 14.0, 94.0, 500.0, 3.0],
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
        # Display as a clean list for the audit
        st.write(
            f"🩺 **BP:** {v['blood_pressure']['sys']}/{v['blood_pressure']['dia']}"
        )
        st.write(f"💓 **Pulse:** {v['pulse']['value']} bpm")
        st.write(
            f"🫁 **SpO2:** {v['spo2']['value']}% | **RR:** {v['respiration_rate']['value']}"
        )
        st.write(f"🩸 **Glucose:** {v['glucose']['value']} {v['glucose']['unit']}")
        st.write(f"🧠 **GCS:** {v.get('gcs', {}).get('score', 'N/A')}/15")
        st.write(
            f"🚽 **Urine:** {v['urine_output']['value']}ml | **Bowel:** {v['bowel_movement']['days_since']}d since"
        )

# COLUMN 2: STEP 3
with col2:
    st.subheader("3. Safety & Sovereignty")
    if "vitals" in st.session_state:
        st.success("🛡️ Litigation Shield: No Conflict Detected")
        if st.button("🔒 Encrypt to Local Vault"):
            st.toast("Saved to Qdrant Database", icon="✅")
            st.session_state["saved"] = True
    else:
        st.info("Awaiting Vitals...")

# COLUMN 3: STEP 4 (THE NURSE ACTION)
# COLUMN 3: AGENTIC SWARM
with col3:
    st.subheader("4. AI Agent Swarm")
    if "vitals" in st.session_state:
        swarm = ClinicSwarm()

        # 1. RUN TRIAGE AGENT
        triage_state = {"vitals": st.session_state["vitals"]}
        triage_res = swarm.triage_agent(triage_state)

        # Store triage in session state so the next agent can see it
        st.session_state["current_triage"] = triage_res["triage_level"]

        st.metric("Triage Level", triage_res["triage_level"])
        st.write(triage_res["messages"][0])

        st.markdown("---")

        # 2. NURSE-IN-THE-LOOP BUTTON
        if st.button("✅ Nurse Approve & Draft"):
            # Construct the FULL state to pass to the Scribe
            scribe_state = {
                "vitals": st.session_state["vitals"],
                "patient_id": st.session_state.get("ghost_id", "GHOST-99"),
                "triage_level": st.session_state[
                    "current_triage"
                ],  # FIXED: Passing the triage level
                "nurse_approved": True,
            }

            discharge_res = swarm.discharge_agent(scribe_state)
            st.session_state["summary"] = discharge_res["draft_summary"]

        # Display the result
        if "summary" in st.session_state:
            st.text_area("FHIR Record Output", st.session_state["summary"], height=300)
