from jsonschema.validators import validates
from mindtickle.services.utils.commonUtils import fileUtils


def verify_response_schema(actual_response_json, json_schema_file):
    response_json_schema = fileUtils.readJsonFile(json_schema_file)
    validates(instance=actual_response_json, schema=response_json_schema)


