# Compliance: USA HIPAA & FDA SaMD
**Focus:** Privacy Safeguards & Software as a Medical Device (SaMD)

## Alignment Overview
Aligned with **HIPAA (1996) Technical Safeguards** and the **FDA Framework for AI/ML-Based Software as a Medical Device**.

## Key Statutory Alignments
1. **Technical Safeguards (45 CFR § 164.312):** 
   - *Implementation:* Access control is enforced via the **Sovereign Vault**, and transmission security is ensured by local-only loopback networking.
2. **Deterministic Safety (SaMD):** To satisfy FDA "Locked Model" concerns, the **Litigation Shield** uses hard-coded Pydantic schemas to prevent stochastic (random) AI errors.
3. **Audit Controls:** The system logs every interaction between the **Agent Swarm** and the Clinician for forensic auditing.