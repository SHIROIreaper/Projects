"""---author: VYSHNAV PC---
version: 1.0.0
An automation script for using Nmap
*Note: Nmap should be installed on your system for this script to run.
       You can install Nmap from the official site: https://nmap.org/download
"""

import subprocess

print("\nChoose a scan mode:")
print("1. Ping Scan (-sn)")
print("2. Quick Scan (-F)")
print("3. Full Scan (-p-)")
print("4. Service Version Scan (-sV)")
print("5. Aggressive Scan (-A)")

choice = input("Enter the scan type (1-5): ")

if choice == "1":
    flags = ["-sn"]
elif choice == "2":
    flags = ["-F"]
elif choice == "3":
    flags = ["-p-"]
elif choice == "4":
    flags = ["-sV"]
elif choice == "5":
    flags = ["-A"]
else:
    print("Invalid choice. Defaulting to Quick Scan.")
    flags = ["-F"]

target = input("Enter domain name or IP to scan: ")
command = ["nmap"] + flags + [target]

try:
    result = subprocess.run(command, capture_output=True, text=True)
    #print(result.stdout)
except Exception as e:
    print(f"An error occurred: {e}")

save = input("Do you want to save the result to a file? (y/n): ")

if save.lower() == "y":
    filename = input("Name of the output file: ")
    try:
        with open(filename, "w") as file:
            file.write(result.stdout)
        print(f"\n Output saved to {filename}")
    except Exception as e:
        print(f"\n Failed to save file: {e}")
