
"""Maher Core: initial project status service.

This prototype reports project metadata only.
It does not control hardware or boot a phone.
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG_FILE = ROOT / "maher-os.json"


def get_system_status():
    """Read project configuration and report its current stage."""
    with CONFIG_FILE.open("r", encoding="utf-8") as file:
        config = json.load(file)

    return {
        "name": config["project"],
        "version": config["version"],
        "architecture": config["architecture"],
        "kernel_status": config["kernel"]["status"],
        "android_compatibility": config[
            "android_compatibility"
        ]["status"],
        "bootable": False,
    }


if __name__ == "__main__":
    print(json.dumps(
        get_system_status(),
        indent=2,
        ensure_ascii=False,
    ))
