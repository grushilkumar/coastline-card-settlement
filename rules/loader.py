"""Loads rules/limits.yaml once at start."""
from pathlib import Path

import yaml

LIMITS_FILE = Path(__file__).with_name("limits.yaml")


def load_limits():
    return yaml.safe_load(LIMITS_FILE.read_text())


def approval_limit():
    return load_limits()["APPROVAL_LIMIT"]
