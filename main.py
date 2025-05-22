from configlib.parser import parse_config
from configlib.validator import validate_dict
from configlib.schema import ConfigSchema

schema = ConfigSchema({
    "app_name": str,
    "version": (int, float),
    "debug": bool,
    "database": {
        "host": str,
        "port": int,
        "user": str,
        "password": str,
    }
})

try:
    config = parse_config("examples/example_valid.yaml")
    if validate_dict(config, schema):
        print("✅ Конфигурація вірна")
except ValueError as e:
    print("❌ Конфигурація невірна:", e)

    
try:
    config = parse_config("examples/example_invalid.yaml")
    if validate_dict(config, schema):
        print("✅ Конфигурація вірна")
except ValueError as e:
    print("❌ Конфигурація невірна:", e)