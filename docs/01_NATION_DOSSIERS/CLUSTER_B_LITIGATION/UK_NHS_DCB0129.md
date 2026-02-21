 United Kingdom: NHS DCB0129
Clinical Safety Case: Mandatory for any health IT system in the NHS.
Architectural Response: Project 3 (Litigation Shield) acts as an automated Hazard Log. Every AI-generated triage suggestion is passed through a Deterministic Circuit Breaker (Pydantic V2) that cross-references NICE guidelines before the clinician sees the output.
DSPT Compliance: Satisfies the Data Security and Protection Toolkit via a local-only loopback architecture.