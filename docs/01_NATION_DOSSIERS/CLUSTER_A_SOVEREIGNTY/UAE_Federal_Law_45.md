UAE: Federal Decree-Law No. 45 (PDPL)
Article 13 (Data Residency): Prohibits transfer of personal data outside the state without high-level adequacy.
Architectural Response: Uses Project 2 (Sovereign Vault). All LLM weights are stored in an air-gapped Docker volume on UAE-based hardware. Zero API calls to external cloud providers (OpenAI/Anthropic).
Article 27 (Security of Processing):
Implementation: AES-256 encryption-at-rest within the Qdrant vector database, orchestrated via a local-only Docker network mesh.