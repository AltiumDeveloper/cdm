"""
conftest.py — pytest configuration for the design validation test suite.

Adds the tests/ directory to sys.path so that test utilities
(udm_to_cdm_transformer, etc.) are importable as top-level modules
from within the test files.
"""

import os
import sys

# Ensure the tests/ directory itself is on sys.path so test utility modules
# like udm_to_cdm_transformer can be imported directly.
_tests_dir = os.path.dirname(__file__)
if _tests_dir not in sys.path:
    sys.path.insert(0, _tests_dir)
