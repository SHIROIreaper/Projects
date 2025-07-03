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
git clone 
cd ext-perms
./ext-perms.sh /path/to/unpacked/extension
```
