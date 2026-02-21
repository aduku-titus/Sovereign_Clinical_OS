import sys
import os
import streamlit as st
import time
import json
import requests  # Moved to top for stability

# --- ROBUST PATHING ---
root_path = os.path.abspath(os.path.dirname(__file__))
if root_path not in sys.path:
    sys.path.insert(0, root_path)

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

# --- SIDEBAR ---
with st.sidebar:
    st.header("1. Patient Intake")
    p_name = st.text_input("Patient Name", "John Doe")
    if st.button("Generate Sovereign Ghost ID"):
        st.session_state["ghost_id"] = "ABC-123-GHOST"
        st.success(f"ID Generated: {st.session_state['ghost_id']}")

    st.markdown("---")
    st.header("🛡️ Project 5: Audit Integrity")

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
            st.warning("No audit logs found yet.")

# --- MAIN LAYOUT ---
col1, col2, col3 = st.columns(3)

# COLUMN 1: EDGE VISION
with col1:
    st.subheader("2. Edge Vision Bridge")
    if st.button("📸 Scan Monitor"):
        with st.spinner("Digitizing Geriatric Vitals..."):
            time.sleep(1)
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

# COLUMN 2: LITIGATION SHIELD
with col2:
    st.subheader("3. Safety & Sovereignty")
    if "vitals" in st.session_state:
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
        if st.button("🔒 Encrypt to Local Vault"):
            st.toast("Data Secured in Qdrant (Local Only)", icon="✅")
            st.session_state["saved"] = True
    else:
        st.info("Awaiting Vitals...")

# COLUMN 3: AGENTIC SWARM
with col3:
    st.subheader("4. AI Agent Swarm")
    if "vitals" in st.session_state:
        swarm = ClinicSwarm()
        triage_state = {"vitals": st.session_state["vitals"]}
        triage_res = swarm.triage_agent(triage_state)
        st.session_state["current_triage"] = triage_res["triage_level"]

        st.metric("Triage Level", st.session_state["current_triage"])
        st.write(triage_res["messages"][0])

        st.markdown("---")
        if st.button("✅ Nurse Approve & Draft"):
            if "ghost_id" not in st.session_state:
                st.error("Action Blocked: Generate Patient ID first.")
            else:
                scribe_state = {
                    "vitals": st.session_state["vitals"],
                    "patient_id": st.session_state["ghost_id"],
                    "triage_level": st.session_state["current_triage"],
                    "nurse_approved": True,
                }
                discharge_res = swarm.discharge_agent(scribe_state)
                st.session_state["summary"] = discharge_res["draft_summary"]

                audit_summary = f"ID: {st.session_state['ghost_id']} | Triage: {st.session_state['current_triage']}"
                event_hash = audit_log.log_event(
                    actor="REGISTERED_NURSE_01",
                    action="CLINICAL_SIGN_OFF",
                    data_summary=audit_summary,
                )
                st.session_state["last_event_hash"] = event_hash

        if "summary" in st.session_state:
            st.text_area("FHIR Record Output", st.session_state["summary"], height=300)
            if "last_event_hash" in st.session_state:
                st.caption(
                    f"Immutable Signature: `{st.session_state['last_event_hash']}`"
                )
    else:
        st.info("Awaiting Triage...")

# --- 5. CLINICAL CONSULTANT (CHAT INTERFACE) ---
# This is now fully un-indented (flush left) so it always renders at the bottom.

st.divider()
st.subheader("5. Clinical Consultant (Offline AI)")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat Input Widget
prompt = st.chat_input("Consult the Sovereign Brain...")
if prompt:
    # Display user message
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Call Ollama
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        try:
            # Check if Requests library is available
            import requests

            url = "http://ollama-brain:11434/api/generate"
            # NOTE: Changed model to 'llama3' - ensure you ran 'ollama pull llama3'
            payload = {
                "model": "llama3",
                "system": "You are Sovereign Clinical AI, an expert triage system for hospital staff. Provide highly accurate, immediate clinical triage steps, vital sign assessments, and pharmacological interventions. Be concise and professional.",
                "prompt": prompt,
                "stream": True,
            }

            with requests.post(url, json=payload, stream=True, timeout=300) as response:
                if response.status_code == 200:
                    for line in response.iter_lines():
                        if line:
                            body = json.loads(line)
                            if "response" in body:
                                token = body["response"]
                                full_response += token
                                message_placeholder.markdown(full_response + "▌")
                    message_placeholder.markdown(full_response)
                    st.session_state.messages.append(
                        {"role": "assistant", "content": full_response}
                    )
                else:
                    st.error(
                        f"Ollama Error: {response.status_code}. Ensure model is pulled."
                    )

        except ImportError:
            st.error("Missing 'requests' library. Add it to requirements.txt")
        except Exception as e:
            st.error(f"⚠️ Connection Error: Is Ollama running? {e}")
