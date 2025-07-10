# OVERVIEW
- This project implements an SSH/Telnet Medium Interaction Honeypot to capture and analyze unauthorized login attempts and malicious behavior patterns. It emulates a fake Linux shell and file system to deceive attackers, providing valuable insights into modern attack vectors and brute-force techniques.

##  What is Honeypot

A Honeypot is a network-attached system used as a trap for cyber-attackers to detect and study the tricks and types of attacks used by hackers. It acts as a potential target on the internet and informs the defenders about any unauthorized attempt at the information system. Honeypots are mostly used by large companies and organizations involved in cybersecurity. It helps cybersecurity researchers learn about the different types of attacks used by attackers. It is suspected that even cybercriminals use these honeypots to decoy researchers and spread wrong information. The cost of a honeypot is generally high because it requires specialized skills and resources to implement a system such that it appears to provide an organization’s resources while still preventing attacks at the backend and access to any production system.

## Tools And Technologies

| Tools             | Purpose                       | Setup Link            |
| :---------------- | :---------------------------- | :-------------------: |
| Cowrie            | SSH/Telnet Honeypot emulation | [Download Cowrie](https://github.com/cowrie/cowrie)   |
| A Server(Ubuntu)  | Host environment              | [Ubuntu Setup](https://ubuntu.com/tutorials/how-to-run-ubuntu-desktop-on-a-virtual-machine-using-virtualbox#1-overview)      |
| Fail2Ban          | Protecting real ssh access    | [Fail2Ban Setup](https://github.com/fail2ban/fail2ban)    |

---

## Deployment Summary

To simulate and analyze attacker behavior, I deployed a **medium-interaction honeypot** using [**Cowrie**](https://github.com/cowrie/cowrie) on a secure AWS EC2 instance.

- Port `22` was exposed as a trap for attackers.
- A separate port (e.g., `2222`) was configured for my own SSH access.
- The honeypot environment was isolated using virtualenv.
- Logs were monitored and managed to observe brute force attempts and command interactions.

---

## General Setup Process

For reproducibility and broader learning, I documented a [**generic honeypot setup**](./setup.md) using a VM-based Ubuntu Server:

### Environment Setup
- Launched an **Ubuntu Server EC2 instance** on AWS.
- Set **Security Group inbound rules**:
  - Port `22` → Open to attract attackers (honeypot port).
  - Port `2222` → For my personal SSH access.
- Enabled firewall (`ufw`) and assigned necessary ports.

### Cowrie Installation
- Installed Python 3 and required dependencies.
- Configured Cowrie for creating a honeypot at port 22.
- Deployed Cowrie in a virtual environment for isolation.

### Configuration Highlights
- Configured Cowrie to listen on port `22`.
- Admin access retained via a non-default port.
- Log collection enabled for analysis (`cowrie.log`, `auth.log`).

---

## Key Files & Folders

| File/Folder        | Purpose                          |
|--------------------|----------------------------------|
| `cowrie.cfg`       | Main configuration file          |
| `userdb.txt`       | Credential emulation setup       |
| `log/cowrie.log`   | Session and interaction logs     |
| `bin/cowrie`       | Start/stop the honeypot          |

---

## Outcome

The honeypot is now live and logging attacker behavior in real time. Observations include:

- Brute force SSH login attempts.
- Command injection patterns.
- Script download and execution behavior from attacker-controlled URLs.

---

# Disclaimer & Warning
This honeypot is intentionally exposed to the public internet. Never run a honeypot on your personal or office network without proper network segmentation and firewalls.