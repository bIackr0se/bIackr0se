# Jaafer Rahmani

**AI red teaming | Security engineering**

PhD researcher in adversarial machine learning, focused on the AI that defends industrial and vehicle networks.

[Website](https://biackr0se.github.io/) · [LinkedIn](https://www.linkedin.com/in/jaafer-rahmani/) · [ORCID](https://orcid.org/0009-0008-0975-2301) · [Email](mailto:jaafer.rahmani@owasp.org)

- Found and reported **CVE-2026-91141** (COVESA vsomeip) and **CVE-2026-58196** (Stacklok ToolHive)
- **12 peer-reviewed papers**: 8 published, 4 to appear
- **28 merged upstream PRs**, 12 of them in Microsoft PyRIT

## Disclosed and fixed

I found both vulnerabilities and reported them through coordinated disclosure. Both are fixed upstream.

- **CVE-2026-91141, COVESA vsomeip.** A 16-byte SOME/IP header made an endpoint allocate 512 MiB before the payload arrived. SOME/IP carries service communication inside vehicles. [CERT/CC VU#128947](https://kb.cert.org/vuls/id/128947) · [Writeup](https://biackr0se.github.io/posts/cve-2026-91141-vsomeip/)
- **CVE-2026-58196, Stacklok ToolHive.** A remote MCP server could make the host runtime send requests to internal addresses, outside the container sandbox. [Advisory](https://github.com/stacklok/toolhive/security/advisories/GHSA-pr64-jmmf-jp54) · [Writeup](https://biackr0se.github.io/posts/ssrf-out-of-the-sandbox/)

## Merged upstream

- [**Microsoft PyRIT: 12.**](https://github.com/microsoft/PyRIT/pulls?q=is%3Apr+is%3Amerged+author%3AbIackr0se) Stop encoded-prompt echoes from counting as successful decodes; fix Unicode payload decoding and package hallucination checks.
- [**cantools: 10.**](https://github.com/cantools/cantools/pulls?q=is%3Apr+is%3Amerged+author%3AbIackr0se) Fix candump log parsing, SYM and KCD writers, and decoded-log plotting.
- [**Scapy: 2.**](https://github.com/secdev/scapy/pulls?q=is%3Apr+is%3Amerged+author%3AbIackr0se) Dissect the PROFINET `PRAL_AlarmItem`; correct the Modbus Report Slave ID byte count.
- [**opcua-asyncio: 1.**](https://github.com/FreeOpcUa/opcua-asyncio/pulls?q=is%3Apr+is%3Amerged+author%3AbIackr0se) Stop swapping send and receive buffer sizes in the Hello/Acknowledge exchange.

[All 28 merged PRs](https://github.com/search?q=author%3AbIackr0se+is%3Apr+is%3Amerged+-user%3AbIackr0se&type=pullrequests)

## Research

To appear in 2026:
- When the Analyst Scans for the Attacker: Subverting Agentic LLM Security Operations in OT Networks. *SHIELD-AI @ ECML PKDD 2026, Springer CCIS*
- KEYSER: Stateful Adversarial Campaign Evaluation of ML-Based Intrusion Detection in Industrial Automation. *IEEE ETFA 2026*
- Adversarial Robustness Evaluation of a Multi-Layer OT Intrusion Detection System via Automated C2 Red Teaming. *IEEE ETFA 2026*
- Agentic Incident Response in IT/OT Critical Infrastructure: Reinforcement Learning and Cross-Domain Generalization. *CCSS 2026*

Published:
- [Characterizing Domain Shift in PROFINET Intrusion Detection: A Multi-Site Ground-Truth Evaluation](https://doi.org/10.1109/WFCS67029.2026.11511604). *IEEE WFCS 2026*
- [CoAnalyst: An Agentic LLM-Based Cybersecurity Analyst for Industrial Control Systems](https://doi.org/10.1109/WFCS67029.2026.11511585). *IEEE WFCS 2026*
- [An Integrated Testbed for MITRE-Mapped Attack Emulation in Industrial Control Networks](https://doi.org/10.3390/s26113514). *MDPI Sensors 2026*
- [An Operational Hybrid SIEM Framework for OT Anomaly Detection](https://doi.org/10.3390/s26103155). *MDPI Sensors 2026*
- [A SIEM-Based Framework for Multi-Layer Data Collection and Anomaly Detection in OT Networks](https://doi.org/10.1109/IDAACS68557.2025.11322203). *IEEE IDAACS 2025*
- [A Testbed for Cyber Attack Emulation and AI-Driven Anomaly Detection in Industrial IoT and OT Networks](https://doi.org/10.1109/IDAACS68557.2025.11322367). *IEEE IDAACS 2025*
- [A Comprehensive Review of Public Datasets for Machine Learning-Based Intrusion Detection in IoT and OT Networks](https://doi.org/10.1109/IDAACS68557.2025.11321996). *IEEE IDAACS 2025*
- [Mapping the MITRE ATT&CK Framework to Modbus Cyber Attacks in Industrial OT Networks](https://doi.org/10.1109/ICEST66328.2025.11098426). *IEEE ICEST 2025*

## What I build

- **[tank-lab](https://github.com/bIackr0se/tank-lab).** A Modbus attack overflows a simulated water tank while the ML intrusion detector reports normal; a physics check on the flow meters catches it. [Live demo](https://biackr0se.github.io/tank-lab/)
- **[AutoMCP](https://github.com/bIackr0se/AutoMCP).** Code for CoAnalyst, the LangGraph analyst for OT/IT alert triage with human review from the IEEE WFCS 2026 paper.
- **[codex-repair-shop](https://github.com/bIackr0se/codex-repair-shop).** Each episode takes one broken AI agent, scans it, fixes it and proves the fix with tests.
- **[agentarium](https://github.com/bIackr0se/agentarium).** A local, read-only view of what AI agents did across projects, with the evidence behind each result.
