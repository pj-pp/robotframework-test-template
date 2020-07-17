# from bson.json_util import dumps
import json
import jsonpointer


def load_json(json_string):
    try:
        return json.loads(json_string)
    except ValueError as e:
        raise ValueError(
            "Could not parse '%s' as JSON: %s" % (json_string, e))


def get_json_value(json_string, json_pointer):
    conv_json = load_json(json_string)
    return jsonpointer.resolve_pointer(conv_json, json_pointer)
