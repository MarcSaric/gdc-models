[![Build Status](https://travis-ci.org/NCI-GDC/gdc-models.svg)](https://travis-ci.org/NCI-GDC/gdc-models)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/f71223e269e64eaaa9f6069ceab526c2)](https://www.codacy.com/manual/NCI-GDC/gdc-models?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=NCI-GDC/gdc-models&amp;utm_campaign=Badge_Grade)

# GDC Models

Git repository centrally stores and serves GDC data models defined in static YAML files.

## Setup 'pre-commit' git hook

After 'git clone' this repository, you will need to run 'setup.sh' to install necessary
git 'pre-commit' hook to ensure YAML files are valid and well formatted.

```
> ./setup.sh
```

## Update the data models

Edit the YAML files as usual, then commit changes to git. Git 'pre-commit' hook will
validate YAML and ensure it's well formatted. It is important to keep YAML file formated
consistently(such as using 2 whitespaces for indentation) across all revisions, this
will make change tracking much easier.

If YAML validation issue is reported, you will need to resovle them before retrying commit again.

When prompted to format the YAML, you can just run:
```
> ./scripts/format_yaml.sh
```

This will automatically format all new or changed YAML files. A copy of unchanged original YAML file
is kept with `.bak` suffix. Before proceed with retrying `git commit`, please `diff` your original YAML
and automatically formated one to ensure YAML formatting did not create any error.

Note that comment is allowed in YAML files, so please use them as needed to add clarity to the data
model definitions.

## Use the data models

### Import ES models into Python code

```
from gdcmodels import get_es_models

es_models = get_es_models()
```

### Initialize Elasticsearch index settings and mappings using command line script

```
# get usage information by: python init_index.py -h
# initialize Elasticsearch indexes: case_set and file_set, add prefix 'gdc_r52' to index name
python init_index.py --index case_set file_set --host localhost --prefix gdc_r52
```
