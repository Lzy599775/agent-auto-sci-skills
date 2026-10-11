"""Unit-test entry point for the writing-exemplar golden-set contract."""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = Path(__file__).with_name("validate_writing_exemplar_routing.py")
SPEC = importlib.util.spec_from_file_location("writing_exemplar_validator", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class WritingExemplarRoutingContractTests(unittest.TestCase):
    def test_golden_set_and_public_contract(self) -> None:
        failures = MODULE.validate_contract(ROOT)
        self.assertEqual([], failures, "\n".join(failures))


if __name__ == "__main__":
    unittest.main()
