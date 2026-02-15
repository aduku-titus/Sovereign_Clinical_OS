# Compliance: Australia My Health Record & AHPRA
**Focus:** Clinical Governance and Interoperability (HI Service)

## Alignment Overview
Aligned with the **My Health Records Act 2012** and the **AHPRA** (Australian Health Practitioner Regulation Agency) guidelines for AI in clinical decision-making.

## Key Statutory Alignments
1. **HI Service Interoperability:** Uses **HL7 FHIR R5** mapping to ensure data captured by the **Edge Vision Bridge** can be integrated into the My Health Record ecosystem.
2. **Clinical Authority:** Per AHPRA guidelines, the AI cannot prescribe or diagnose autonomously. 
   - *Implementation:* **Project 4 (Agent Swarm)** includes a mandatory **Nurse-Override Dashboard**. No record is finalized without a practitioner’s digital sign-off.
3. **Rural Health Moat:** Specifically designed for "Offline-First" use in Western Australia and Northern Territory safety-net clinics.