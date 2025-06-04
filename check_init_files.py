import os
import sys
import json
from pathlib import Path


def _get_project_root() -> Path:
    """
    Get /mcp_server path
    """
    return Path(__file__).parent


def check_init_file(directory):
    missing_init = []

    with open(
        os.path.join(_get_project_root(), "mcp_server/excluded_folders.json"),
        encoding="utf-8",
    ) as file:
        config = json.load(file)
    excluded_folders = set(config["excluded_folders"])

    for root, _, files in os.walk(directory):
        if os.path.basename(root) in excluded_folders:
            continue
        if "__init__.py" not in files:
            missing_init.append(root)

    if missing_init:
        print("\nFolders missing __init__.py file:")
        list_of_folders = []
        for folder in missing_init:
            print(folder)
            list_of_folders.append(os.path.basename(folder))
        print(
            "\nTo fix it you may:\n"
            + "1. Run './scripts/create_init_files.sh' on your IDE's Terminal to add the __init__.py files.\n"
            + f"2. Or add the directories '{list_of_folders}' to 'excluded_folders.json' "
            + "to exclude them from being required to have an __init__.py file."
        )
        sys.exit(1)

    print("\nAll folders have an __init__.py file.")


if __name__ == "__main__":
    DIRECTORY = os.path.join(_get_project_root(), "mcp_server")
    check_init_file(DIRECTORY)
