import os
import pkg_resources
import re
from os.path import isfile, join as pj

import yaml


def load_yaml(filename):
    """Return contents of yaml file as dict"""
    with open(filename, 'r') as f:
        return yaml.safe_load(f)


def load_descriptions(filename):
    descriptions = load_yaml(filename)
    result = {}
    # we can select what properties to add in the future
    if '_meta' in descriptions:
        result['_meta'] = descriptions.get('_meta')
    return result


def get_es_models(es_model_dir=None):
    """
    Return ES settings and mappings as dict with contents from yaml file,
    dict is structured similarly as Elasticsearch's '_settings', '_mapping'
    return

    :param es_model_dir: root directory for gdc ES mappings
    :type es_model_dir: str
    :return: loaded mappings
    """

    if es_model_dir is None:
        es_model_dir = pkg_resources.resource_filename('gdcmodels', 'es-models')

    es_models = {}

    for es_index in os.listdir(es_model_dir):
        if os.path.isfile(os.path.join(es_model_dir, es_index)):
            continue

        for f in os.listdir(os.path.join(es_model_dir, es_index)):
            if es_index not in es_models:
                es_models[es_index] = {
                    '_settings': {}
                }

            if f.endswith('.mapping.yaml'):
                es_type = re.sub(r'\.mapping\.yaml$', '', f)
                es_models[es_index][es_type] = {
                        '_mapping': load_yaml(pj(es_model_dir, es_index, f))
                    }
                desc_path = pj(es_model_dir, es_index, 'descriptions.yaml')
                if isfile(desc_path):
                    descriptions = load_descriptions(desc_path)
                    es_models[es_index][es_type]['_mapping'].update(descriptions)
            elif f == 'settings.yaml':
                es_models[es_index]['_settings'] = load_yaml(
                    os.path.join(es_model_dir, es_index, f)
                )

    return es_models
