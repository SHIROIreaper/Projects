#!/bin/bash

# Check if path is provided
if [[ -z "$1" ]]; then
    echo "[x] Usage: $0 /path/to/unpacked/extension"
    exit 1
fi

EXT_DIR="${1%/}"  # Remove trailing slash

# Try to locate manifest.json recursively
MANIFEST_PATH=$(find "$EXT_DIR" -type f -name "manifest.json" | head -n 1)

if [[ ! -f "$MANIFEST_PATH" ]]; then
    echo "[x] manifest.json not found under $EXT_DIR"
    exit 1
fi

echo "[ok] Found manifest.json at: $MANIFEST_PATH"
echo "[info] Permissions used:"

# Extract and print permissions
grep '"permissions"' "$MANIFEST_PATH" \
  | sed -E 's/.*"permissions"\s*:\s*\[([^]]*)\].*/\1/' \
  | tr ',' '\n' \
  | tr -d '" ' \
  | sed '/^$/d' \
  | while read -r perm; do
      echo "- $perm"
  done
