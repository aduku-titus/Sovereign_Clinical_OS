import hashlib
import json
import os
from datetime import datetime


class SovereignAuditLogger:
    def __init__(self, log_file="data_lake/vault_db/audit_chain.json"):
        self.log_file = log_file
        # Ensure directory exists
        os.makedirs(os.path.dirname(self.log_file), exist_ok=True)

        # Initialize the chain if file doesn't exist
        if not os.path.exists(self.log_file):
            self._initialize_genesis_block()

    def _initialize_genesis_block(self):
        genesis_entry = {
            "index": 0,
            "timestamp": str(datetime.now()),
            "action": "GENESIS_BLOCK",
            "actor": "SYSTEM_ROOT",
            "data_summary": "Initial Sovereign Audit Chain Created",
            "previous_hash": "0" * 64,
        }
        genesis_entry["hash"] = self._calculate_hash(genesis_entry)
        with open(self.log_file, "w") as f:
            json.dump([genesis_entry], f, indent=4)

    def _calculate_hash(self, entry):
        # Create a stable string representation for hashing
        entry_string = json.dumps(
            {
                "index": entry["index"],
                "timestamp": entry["timestamp"],
                "action": entry["action"],
                "actor": entry["actor"],
                "data_summary": entry["data_summary"],
                "previous_hash": entry["previous_hash"],
            },
            sort_keys=True,
        )
        return hashlib.sha256(entry_string.encode()).hexdigest()

    def log_event(self, actor, action, data_summary):
        """Logs a new clinical action to the chain."""
        with open(self.log_file, "r") as f:
            chain = json.load(f)

        last_entry = chain[-1]
        new_entry = {
            "index": last_entry["index"] + 1,
            "timestamp": str(datetime.now()),
            "action": action,
            "actor": actor,
            "data_summary": data_summary,
            "previous_hash": last_entry["hash"],
        }
        new_entry["hash"] = self._calculate_hash(new_entry)

        chain.append(new_entry)
        with open(self.log_file, "w") as f:
            json.dump(chain, f, indent=4)
        return new_entry["hash"]

    def verify_chain(self):
        """Validates the entire audit log for tampering."""
        with open(self.log_file, "r") as f:
            chain = json.load(f)

        for i in range(1, len(chain)):
            current = chain[i]
            previous = chain[i - 1]

            # 1. Check if stored hash matches calculated hash
            if current["hash"] != self._calculate_hash(current):
                return False, f"Tamper detected at Index {current['index']}"

            # 2. Check if the link to previous hash is broken
            if current["previous_hash"] != previous["hash"]:
                return (
                    False,
                    f"Link broken between {previous['index']} and {current['index']}",
                )

        return True, "Chain Integrity Verified: 100%"
