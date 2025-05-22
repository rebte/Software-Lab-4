class ConfigSchema:
    def __init__(self, schema_dict):
        if not isinstance(schema_dict, dict):
            raise TypeError("Schema must be a dictionary")
        self.schema = schema_dict

    def validate(self, config):
        return self._validate_dict(config, self.schema)

    def _validate_dict(self, config, schema):
        for key, expected in schema.items():
            if key not in config:
                raise ValueError(f"Missing required field: {key}")

            value = config[key]

            if isinstance(expected, dict):
                if not isinstance(value, dict):
                    raise ValueError(f"Field '{key}' must be a dictionary")
                self._validate_dict(value, expected)
            elif isinstance(expected, tuple):
                if not isinstance(value, expected):
                    raise ValueError(f"Field '{key}' must be one of types: {expected}")
            else:
                if not isinstance(value, expected):
                    raise ValueError(f"Field '{key}' must be of type {expected.__name__}")
        return True
