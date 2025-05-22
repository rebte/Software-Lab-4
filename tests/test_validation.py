import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from configlib.schema import ConfigSchema
from configlib.validator import validate_dict


def test_valid_config():
    schema = ConfigSchema({
        "name": str,
        "active": bool
    })
    config = {"name": "Test", "active": True}
    assert validate_dict(config, schema) is True

def test_missing_key():
    schema = ConfigSchema({
        "name": str,
        "active": bool
    })
    config = {"name": "Test"}
    with pytest.raises(ValueError):
        validate_dict(config, schema)

def test_wrong_type():
    schema = ConfigSchema({
        "name": str,
        "active": bool
    })
    config = {"name": "Test", "active": "yes"}
    with pytest.raises(ValueError):
        validate_dict(config, schema)
