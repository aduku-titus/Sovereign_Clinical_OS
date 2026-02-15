from langgraph.graph import StateGraph, END
from state import AgentState
from agents import ClinicSwarm
import sqlite3
from langgraph.checkpoint.sqlite import SqliteSaver

# 1. Setup Memory (Antifragility)
conn = sqlite3.connect("swarm_memory.db", check_same_thread=False)
memory = SqliteSaver(conn)

# 2. Initialize Swarm
swarm = ClinicSwarm()
workflow = StateGraph(AgentState)

# 3. Add Nodes (The Staff)
workflow.add_node("triage_nurse", swarm.triage_agent)
workflow.add_node("scribe", swarm.discharge_agent)

# 4. Define the Flow
workflow.set_entry_point("triage_nurse")

# --- THE HITL LOGIC ---
# We go from Triage -> Human Check -> Scribe
# We do NOT connect Triage directly to Scribe. We stop.
workflow.add_edge("triage_nurse", END)
# Note: In a real app, the UI triggers the next step.
# Here we simulate the 'Pause' by ending the first run.

# 5. Compile the Graph
app = workflow.compile(checkpointer=memory)

if __name__ == "__main__":
    print("Graph Compiled with SQLite Memory. Ready for HITL Workflow.")
