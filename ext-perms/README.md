# ext-perms

**"What's your browser extension really asking for?"**  
`ext-perms` — a terminal-friendly tool that instantly reveals the permissions an unpacked browser extension is requesting.  

Whether you're auditing extensions for security, privacy, or just curiosity, `ext-perms` gets straight to the point with zero dependencies.


## Objective

Browser extensions can request powerful permissions that pose security or privacy risks. This tool helps identify those permissions quickly by parsing the `manifest.json`.

## Requirements

- Bash shell (Linux, macOS, or WSL on Windows)

## Usage

```
git clone https://github.com/SHIROIreaper/Projects.git
cd Projects/ext-perms
chmod +x ext-perms.sh
./ext-perms.sh /path/to/unpacked/extension
```
## Output
- The script prints the following:

  1. Confirmation of manifest file presence

  2. Clean list of permissions extracted from manifest.json

> Note that this works with chromium-based browsers (like google chrome, microsoft edge, etc). Firefox may cause malfunction.
 > I'm currently working on a CLI-tool that would fetch the permissions and hidden leaks from any extensions. This project would be shifted to that in the distant future.
