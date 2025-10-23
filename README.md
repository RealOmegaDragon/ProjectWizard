# ProjectWizard
*A modular Python-based penetration testing toolkit built for network reconnaissance and ethical security testing.*

---

## Overview
**ProjectWizard** is a command-line penetration testing framework designed to simplify **network reconnaissance**, **port scanning**, and **subnet mapping**.  
It’s written in **Python** and leverages **Nmap** for reliable host and service discovery, all while maintaining a modular architecture that’s easy to extend with new scanning features.

---

## Purpose
The goal of this project is to create a **lightweight, extensible, and transparent security toolkit** that:  
- Demonstrates core **network and security programming principles**.  
- Focuses on **ethical, user-controlled** vulnerability assessment.  
- Showcases a **clean Python architecture** emphasizing modularity and maintainability.  
- Provides a foundation for future expansion into automated vulnerability scanning and reporting.  

---

## Features
- Modular structure for scanners, reconnaissance, and utilities.  
- Integrated **Nmap** engine for port and service detection.  
- **DNS** and **WHOIS** enumeration modules for domain intelligence.  
- **Subnet mapping** and network discovery utilities.  
- Structured **JSON output** for result storage and future integration (`{"results": []}`).  
- Easy to modify and extend for new scanning modules.  

---

## Built With
- **Python 3.x**  
  - Core CLI logic, JSON handling, and module orchestration  
- **Nmap**  
  - Used for port and service detection (must be installed and in system PATH)  

---

## Project Structure
```
ProjectWizard/
│
├── main.py # Entry point for CLI execution
│
├── core/
│ ├── engine.py # Main scan engine and orchestration logic
│ ├── input.py # Handles user input and CLI parsing
│ └── output.py # JSON and console output handling
│
├── modules/
│ ├── recon/
│ │ ├── dns_enum.py # DNS enumeration module
│ │ └── whois_lookup.py # WHOIS lookup module
│ │
│ └── scan/
│ └── port_scanner.py # Port scanning logic (via Nmap)
│
├── utilities/
└── subnet_map.py # Subnet mapping and network utilities
```


---

## Requirements
- **Python 3.10+**  
- **Nmap** installed and available in your system PATH  

---

## Running the Project
1. Clone the repository:  
   ```bash
   git clone https://github.com/RealOmegaDragon/ProjectWizard.git
   cd ProjectWizard
2. Run the main script:
   `python main.py`
3. View results in the generated JSON files or console output.

---

## Ethical Use
**ProjectWizard** is intended strictly for authorized and ethical penetration testing.
Always ensure you have explicit permission before scanning or probing any system.
The author assumes no responsibility for misuse of this tool.

---

## What I Learned
Building **ProjectWizard** strengthened my understanding of:
- Structuring modular and scalable Python CLI applications.
- Integrating third-party tools (Nmap) safely and programmatically.
- Organizing multi-module security tool architectures.
- Managing structured JSON result handling for extensibility.

---

## Author
**Braxton Newhall**  
Social: [LinkedIn](https://linkedin.com/in/braxton-newhall-128597333) • [GitHub](https://github.com/RealOmegaDragon)  
Email: braxtonnewhall@gmail.com

---

## License
This project is open-source under the [MIT License](LICENSE).
