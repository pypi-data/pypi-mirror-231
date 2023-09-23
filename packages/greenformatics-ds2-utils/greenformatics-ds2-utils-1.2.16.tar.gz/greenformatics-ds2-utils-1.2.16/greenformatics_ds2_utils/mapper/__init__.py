# coding=utf-8

from greenformatics_ds2_utils.converter import *
import json


def map_dict_to_object(data, class_name, attribute_name_converter, attribute_name_map=None):
    """ Map the values form ``data`` dictionary to the attributes of one instance of ``class_name`` applying
    the attribute name converter (``attribute_name_converter``) and attribute name map (``attribute_name_map``)

    :param data: dictionary to be mapped to an instance of the ``class_name``
    :param class_name: the class of the object to convert the ``data`` dictionary to
    :param attribute_name_converter: the converter function to be applied on each keys in ``data``
    :param attribute_name_map: Optional param of an attribute mapping in which the keys are the keys in ``data`` and
    the associated values are the attribute names of the class (``class_name``)
    :return: an instance of the ``class_name`` with attribute values mapped from ``data``
    """

    mapped_object = class_name()
    for k, v in data.items():
        mapped_attribute_name = map_attribute_name(attribute_name_map, k)
        converted_attribute_name = attribute_name_converter(mapped_attribute_name)
        if isinstance(v, list) or isinstance(v, dict):
            setattr(mapped_object, converted_attribute_name,
                    json.dumps(v))
        else:
            nullable_field_value = year_zero_to_none(empty_str_to_none(v))
            setattr(mapped_object, converted_attribute_name, nullable_field_value)

    return mapped_object


def dict_to_object_in_snake_case(data, class_name, attribute_name_map=None):
    """ Map dict with camel case keys to an object with snake case attributes
    
    :param data: dictionary to be mapped to an instance of the ``class_name``
    :param class_name: the class of the object to convert the ``data`` dictionary to
    :param attribute_name_map: Optional param of an attribute mapping in which the keys are the keys in ``data`` and the associated
    values are the attribute names of the class (``class_name``)
    :return: an instance of the ``class_name`` with attribute values mapped from ``data``
    """

    return map_dict_to_object(data, class_name, camel_case_to_snake_case, attribute_name_map)


def dict_to_object_in_lower_case_no_spec(data, class_name, attribute_name_map=None):
    """ Map dict with camel case keys to an object with snake case attributes """

    return map_dict_to_object(data, class_name, nfkd_normalized_lower_no_spec, attribute_name_map)


def dict_to_object_in_lower_case_db_safe(data, class_name, attribute_name_map=None):
    """ Map dict with camel case keys to an object with snake case attributes """

    return map_dict_to_object(data, class_name, nfkd_normalized_lower_db_safe, attribute_name_map)


def dict_list_to_object_list(dict_list: [{}], class_name, attribute_name_converter=camel_case_to_snake_case,
                             attribute_name_map=None) -> []:
    """ Loop through the list of dictionaries and map them to objects. It results a list of object. """

    object_list = []
    for elem in dict_list:
        object_list.append(map_dict_to_object(elem, class_name, attribute_name_converter, attribute_name_map))
    return object_list


def wrap_dictionary_keys(data_dict, keys_to_keep, wrapper_key_name='nested'):
    """ Put fields of the ``data_dict`` dictionary not in ``keys_to_keep`` to a dictionary referred
    by ``wrapper_key_name``

    :param data_dict: the dictionary with all the key that should or should not keep as are
    :param keys_to_keep: the keys to be kept in the first level of the dictionary
    :param wrapper_key_name: the name of the key under which the non-first-level key-value pairs put
    :return: the dictionary where the key-value pairs are not in the ``keys_to_keep`` put under the key name given
    """
    keys_to_nest = set(data_dict.keys()) - set(keys_to_keep)
    result_dict = {key: value for key, value in data_dict.items() if key in keys_to_keep}
    nested_dict = {key: value for key, value in data_dict.items() if key in keys_to_nest}
    if len(nested_dict.keys()):
        result_dict[wrapper_key_name] = nested_dict
    return result_dict
