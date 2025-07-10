# Honeypot Setup Guide

## My Deployment Experience

I personally set up a honeypot server on **AWS EC2**, where I:

- Created a custom **Ubuntu Server instance**.
- Configured **port 22** to be accessible to attackers (the trap).
- Used an **alternate SSH port (e.g., 2552)** for my own secure admin access.
- Installed and configured the **Cowrie honeypot**, isolated within a virtual environment.
- Hardened access with proper **firewall rules (inbound security group policies)** and monitored logs via `journalctl`, `auth.log`, and Cowrie logs.

This document however outlines the general method of deploying a honeypot **locally or in a lab** using a **VM (Virtual Machine)**.

---

## Honeypot on Ubuntu VM

### Prerequisites

| Requirement         | Description                          |
|---------------------|--------------------------------------|
| VM Software         | VirtualBox / VMware / GNOME Boxes   |
| OS Image            | Ubuntu Server (e.g., 20.04 or 22.04) |
| Basic Networking    | NAT/Bridged with static IP setup     |
| Access              | Terminal or SSH                      |

---

### Step-by-Step Setup

#### 1. Install Ubuntu Server in VM

- Download ISO: https://ubuntu.com/download/server
- Create a VM in VirtualBox:
  - RAM: `>=1024 MB`
  - Disk: `>=10 GB (Dynamically Allocated)`
  - Enable: **Bridged Adapter** or **Host-only Adapter** for lab realism.

---

#### 2. Basic Configuration After Boot

Log in to your VM and run:

```
sudo apt update && sudo apt upgrade -y
adduser honeymaster #add a new user
usermod -aG sudo honeymaster
sudo apt install python3 python3-venv python3-pip -y
```
#### 3. Create Virtual Isolation

```
python3 -m venv honeypot-env
source honeypot-env/bin/activate
```
#### 4. Install and configure  Cowrie Honeypot

```
git clone https://github.com/cowrie/cowrie.git
cd cowrie
cp cowrie.cfg.dist cowrie.cfg
cp userdb.txt.dist userdb.txt
```
- Then Modify configuration in `nano etc/cowrie.cfg`
 - change the port for the honeytrap (eg: 80), Change hostname, enable authlog ,etc as needed.

#### 5. Start Cowrie

```
bin/cowrie start
tail -f log/cowrie.log
```

---
### Additional Resources
- [Cowrie Github](https://github.com/cowrie/cowrie)
- [VirtualBox Ntworking Docs](https://www.virtualbox.org/manual/ch06.html)
