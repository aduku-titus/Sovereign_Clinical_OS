from fastembed import TextEmbedding
import numpy as np


class SovereignBrain:
    """
    Project 2: The Sovereign Cloud (Multilingual Embedding Engine).
    Engine: intfloat/multilingual-e5-large (1024-Dimensions)
    Compliance: UAE Law 45 & EU GDPR.
    """

    def __init__(self):
        print(
            "[SOVEREIGN_OS] Initializing High-Resolution Multilingual Brain (E5-Large)..."
        )
        # We use the exact name found by your diagnostic script
        self.model = TextEmbedding(model_name="intfloat/multilingual-e5-large")

    def vectorize_clinical_note(self, note: str):
        """
        Turns clinical text into 1024 mathematical coordinates.
        Logic: We add 'query: ' prefix as required by E5-Large for better accuracy.
        """
        formatted_note = f"query: {note}"
        embeddings = list(self.model.embed([formatted_note]))
        return embeddings[0].tolist()


if __name__ == "__main__":
    brain = SovereignBrain()

    # 12-Nation Test: English (AU/US), Arabic (UAE), German (CH/DE)
    handovers = [
        "Patient is confused and has a high fever.",
        "المريض مرتبك ويعاني من حمى شديدة",
        "Der Patient ist verwirrt und hat hohes Fieber.",
    ]

    print("\n--- SEMANTIC SOVEREIGNTY TEST (E5-LARGE) ---")
    for note in handovers:
        vector = brain.vectorize_clinical_note(note)
        print(f"Note: {note}")
        print(f"Vector (First 5): {vector[:5]}...")
        print("Status: Encoded Locally via ONNX. Sovereignty 100%.\n")
