# Compliance: UAE Federal Law No. 45 (PDPL)
**Focus:** Data Residency & National Sovereignty

## Alignment Overview
The Sovereign Clinical_OS is architected to exceed the requirements of **UAE Federal Law No. 45 (2021)** regarding the protection of personal data.

## Key Statutory Alignments
1. **Article 13 (Data Residency):** The law restricts the transfer of personal data outside the UAE. 
   - *Implementation:* Our system uses **Project 2 (Sovereign Cloud)**, performing all LLM inference via Ollama on local hardware. No patient data crosses national borders.
2. **Article 27 (Security of Processing):** Requires appropriate technical and organizational measures.
   - *Implementation:* Data is encrypted at rest using AES-256 within the **Sovereign Vault** (Qdrant).
3. **Sovereignty Check:** Aligns with the UAE's "Digital First" and "Data Sovereignty" strategies by ensuring national health data remains on UAE soil.