from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct


class SovereignVault:
    """
    Project 2: The Sovereign Vault (Qdrant Integration).
    Version-Stable Edition (Compatible with qdrant-client 1.7.3).
    """

    def __init__(self, collection_name="geriatric_ward"):
        # Logic: Connect to the 'Hospital Building' (Docker Container)
        self.client = QdrantClient(host="localhost", port=6333)
        self.collection_name = collection_name

        # --- ROBUST VERSION-STABLE CHECK ---
        # Instead of the new 'collection_exists' method, we use the stable 'get_collections'
        collections_response = self.client.get_collections()
        existing_names = [c.name for c in collections_response.collections]

        if self.collection_name not in existing_names:
            print(f"[SOVEREIGN_OS] Initializing New Ward Vault: {self.collection_name}")
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(size=1024, distance=Distance.COSINE),
            )
        else:
            print(
                f"[SOVEREIGN_OS] Vault Ward '{self.collection_name}' is already online."
            )

    def deposit_vitals(self, ghost_id: str, vector: list, metadata: dict):
        """Secures clinical math and identity into the Docker-encapsulated Vault."""
        self.client.upsert(
            collection_name=self.collection_name,
            points=[PointStruct(id=ghost_id, vector=vector, payload=metadata)],
        )
        print(f"[SOVEREIGN_OS] Data Secured for Ghost ID: {ghost_id[:8]}...")


if __name__ == "__main__":
    # Test the connection
    try:
        vault = SovereignVault()
        print("Sovereign Vault is Online and Validated.")
    except Exception as e:
        print(f"❌ Connection Error: Ensure Docker is running. Error: {e}")
