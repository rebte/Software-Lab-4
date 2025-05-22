from .parser import parse_config

def validate_config(path, schema):
    config = parse_config(path)
    return schema.validate(config)

def validate_dict(config_dict, schema):
    return schema.validate(config_dict)
