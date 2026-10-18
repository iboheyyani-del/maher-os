
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from core.maher_core import get_system_status


class MaherCoreTests(unittest.TestCase):

    def test_project_status(self):
        status = get_system_status()

        self.assertEqual(status["name"], "Maher OS")
        self.assertEqual(status["architecture"], "aarch64")
        self.assertFalse(status["bootable"])

    def test_future_features_are_not_claimed_ready(self):
        status = get_system_status()

        self.assertEqual(
            status["kernel_status"],
            "not_integrated"
        )
        self.assertEqual(
            status["android_compatibility"],
            "planned"
        )


if __name__ == "__main__":
    unittest.main()
