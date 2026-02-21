# 🏥 SOVEREIGN CLINICAL_OS
![Status](https://img.shields.io/badge/Status-Production%20Ready-green)
![Architecture](https://img.shields.io/badge/Architecture-Air--Gapped-blue)
![Compliance](https://img.shields.io/badge/Compliance-UAE%20Law%2045%20%7C%20NHS%20DCB0129-gold)

**Principal Architect:** Titus Afeo Azure Aduku  
**Strategic Window:** 2026 Migration Cycle (UAE, Australia, Switzerland, UK)  
**Status:** Air-Gapped / Offline-First / Production-Ready

---

## 📺 Live Demo: 100% Offline Inference
![Sovereign OS Offline Demo](docs/assets/offline_demo.gif)
*Demonstrating Llama-3 clinical reasoning running on local CPU with zero internet connectivity.*

---

## 🌐 The Governance-as-Code Dossier
This is a unified clinical operating system built to bypass the "Public Cloud Dependency" of modern healthcare. By integrating Computer Vision, Local LLMs, and Deterministic Logic, this OS provides National Health Security in an era of cyber-instability.

### 🏗️ 4 Pillars of Sovereignty
| Pillar | Technology | Function |
| :--- | :--- | :--- |
| **1. Edge Vision Bridge** | EasyOCR + OpenCV | Offline digitization of legacy analog vitals. |
| **2. Sovereign Vault** | Qdrant + FastEmbed | Local RAG and SHA-256 PII scrubbing. |
| **3. Litigation Shield** | Pydantic V2 | Deterministic clinical safety gates. |
| **4. Agentic Swarm** | LangGraph + Ollama | Local LLM triage and FHIR R5 automation. |

---

## 🏛️ 12-Nation Regulatory Readiness
This OS is architected to satisfy the specific legal frameworks of the 2026 migration targets:

| Cluster | Focus | Target Nations | Dossier Link |
| :--- | :--- | :--- | :--- |
| **A: Sovereignty** | Data Residency | UAE, Saudi Arabia, S. Korea | [View Dossier](docs/01_NATION_DOSSIERS/CLUSTER_A_SOVEREIGNTY/) |
| **B: Litigation** | Clinical Safety | UK, USA, Ireland | [View Dossier](docs/01_NATION_DOSSIERS/CLUSTER_B_LITIGATION/) |
| **C: Interoperability** | FHIR R5 / HI Service | Australia, Canada, NZ | [View Dossier](docs/01_NATION_DOSSIERS/CLUSTER_C_INTEROPERABILITY/) |
| **D: Ethics** | AI Act / Privacy | EU, Switzerland, Singapore | [View Dossier](docs/01_NATION_DOSSIERS/CLUSTER_D_ETHICS_AI/) |

---

## ⚡ System Architecture
The system operates as a containerized mesh, isolated from the public internet.

```mermaid
graph TD
    Clinician -->|UI| Streamlit[Clinician UI]
    Streamlit -->|Logic| API[Clinical Logic API]
    API -->|RAG| Qdrant[Sovereign Vault]
    API -->|Inference| Ollama[Local LLM Brain]
    
    subgraph "Air-Gapped Environment"
    Streamlit
    API
    Qdrant
    Ollama
    end

🚀 Quick Start (Airplane Mode)
Prerequisites:

Docker Desktop installed.
Hardware: Minimum 12GB RAM (16GB recommended).

1. Build the Factory
docker-compose up --build -d
2. Pull the Brain (Requires internet once)
docker exec -it clinical_brain_offline ollama pull llama3
3. Go Offline
Disconnect WiFi and navigate to http://localhost:8501

🛠️ Technical Specs
Logic: Pydantic V2 Deterministic Schemas
Standards: HL7 FHIR R5, SNOMED CT
Inference: Local Ollama (Llama 3 / DeepSeek)
Dependency Management: uv (Rust-based Python package manager)
Security: SHA-256 Pseudonymization & Hash-Chain Audit Logging

Architectural Inquiries: [Your LinkedIn Link] | [Your Email]