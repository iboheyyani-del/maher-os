
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from core.maher_core import get_system_status


class MaherCoreTests(unittest.TestCase):

    def test_project_identity(self):
        status = get_system_status()
        self.assertEqual(status["name"], "Maher OS")
        self.assertEqual(status["platform"], "AOSP")
        self.assertEqual(status["architecture"], "aarch64")

    def test_aosp_is_not_claimed_integrated(self):
        status = get_system_status()
        self.assertFalse(status["source_integrated"])
        self.assertFalse(status["bootable"])

    def test_future_components(self):
        status = get_system_status()
        self.assertEqual(
            status["kernel_status"],
            "not_integrated",
        )
        self.assertEqual(
            status["android_compatibility"],
            "planned",
        )

    def test_target_device_is_not_selected(self):
        status = get_system_status()
        self.assertIsNone(status["target_device"])


if __name__ == "__main__":
    unittest.main()
