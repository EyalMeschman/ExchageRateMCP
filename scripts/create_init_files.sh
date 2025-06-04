#!/bin/bash

EXCLUDED_FOLDERS_JSON="mcp_server/excluded_folders.json"

# Extracting folder names from the JSON file, excluding the key
EXCLUDED_FOLDERS=$(grep -o '"[^"]*"' "$EXCLUDED_FOLDERS_JSON" | grep -v "excluded_folders" | tr -d '"' | tr '\n' ' ')

find mcp_server/ -type d | while read dir; do
    skip=0
    for folder in $EXCLUDED_FOLDERS; do
        if [ "$(basename "$dir")" = "$folder" ]; then
            skip=1
            break
        fi
    done

    if [ "$skip" -eq 0 ] && [ ! -f "$dir/__init__.py" ]; then
        touch "$dir/__init__.py"
        echo "Created __init__.py in $dir"
    fi
done
