# Compliance: Saudi Arabia NDMO & PDPL
**Focus:** National Data Management Office (NDMO) Standards

## Alignment Overview
This system aligns with the **Saudi Personal Data Protection Law (PDPL)** and the **NDMO Data Governance** framework for "Critical National Entities."

## Key Statutory Alignments
1. **Local Embeddings:** All vectorization (FastEmbed) occurs locally. This ensures that clinical knowledge bases used by the Vision Bridge do not leak to external hyperscalers.
2. **Health Data Sensitivity:** The PDPL treats health data as "Sensitive." 
   - *Implementation:* The **SovereignScrubber** hashes names into UUIDs before they enter the data lake, fulfilling "Privacy-by-Design" mandates.
3. **Offline Infrastructure:** Supports the KSA Vision 2030 goal of resilient digital healthcare by operating 100% without global cloud dependencies.