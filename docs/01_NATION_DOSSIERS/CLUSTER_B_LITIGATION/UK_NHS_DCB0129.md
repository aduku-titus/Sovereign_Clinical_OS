# Compliance: UK NHS DCB0129
**Focus:** Clinical Risk Management for Health IT

## Alignment Overview
This OS implements the mandatory **DCB0129** standard required by the NHS for any manufacturer of health software.

## Key Statutory Alignments
1. **Clinical Safety Case (Project 3):** The **Litigation Shield** serves as the automated safety case. It cross-checks all outputs against **NICE Guidelines** and the **Merck Manual**.
2. **Hazard Log Mitigation:** Every "Never Event" (e.g., lethal dose suggestion) is mitigated by the **ConflictResolver** class, which acts as a deterministic circuit breaker.
3. **Data Protection:** Satisfies the **NHS Data Security and Protection Toolkit (DSPT)** requirements via the air-gapped Docker-compose deployment.