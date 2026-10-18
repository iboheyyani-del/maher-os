
"""Maher OS project status service.

This module reports project metadata.
It does not boot a device or build AOSP.
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG_FILE = ROOT / "maher-os.json"


def get_system_status():
    """Return the current, declared project status."""
    with CONFIG_FILE.open("r", encoding="utf-8") as file:
        config = json.load(file)

    platform = config["platform"]
    kernel = config["kernel"]
    android = config["android_compatibility"]
    build = config["build"]

    return {
        "name": config["project"],
        "version": config["version"],
        "architecture": config["architecture"],
        "platform": platform["identifier"],
        "source_integrated": platform["source_integrated"],
        "kernel_status": kernel["status"],
        "android_compatibility": android["status"],
        "bootable": build["bootable"],
        "target_device": config["hardware"]["target_device"],
    }


if __name__ == "__main__":
    print(
        json.dumps(
            get_system_status(),
            indent=2,
            ensure_ascii=False,
        )
    )
