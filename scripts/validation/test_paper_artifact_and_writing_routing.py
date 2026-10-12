"""Unit-test entry point for the synthetic cross-client routing contract."""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("validate_paper_artifact_and_writing_routing.py")
SPEC = importlib.util.spec_from_file_location("paper_artifact_routing_validator", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class PaperArtifactAndWritingRoutingTests(unittest.TestCase):
    def test_synthetic_contract_and_cross_client_routes(self) -> None:
        failures = MODULE.validate_contract(MODULE.ROOT)
        self.assertEqual([], failures, "\n".join(failures))


if __name__ == "__main__":
    unittest.main()
