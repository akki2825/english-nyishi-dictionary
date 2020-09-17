import json
from typing import Dict


def json2xml(json_obj: Dict[str, str]) -> str:
    """
    Converts JSON to Lexonomy's XML.
    """
    result_list = []

    json_obj_type = type(json_obj)

    if json_obj_type is dict:
        count = 0
        for tag_name in json_obj:
            sub_obj = json_obj[tag_name]
            result_list.append("<entry lxnm:entryID='%s' xmlns:lxnm='http://www.lexonomy.eu/'>" % (count))
            result_list.append("<headword xml:space='preserve'>%s</headword>" % (tag_name))
            result_list.append('<sense>')
            result_list.append("<translation xml:space='preserve'>%s</translation>" % (str(sub_obj)))
            result_list.append('</sense>')
            result_list.append('</entry>')
            count +=1
        return "".join(result_list)

    return "%s%s" % (json_obj)
