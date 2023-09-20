import os

_project_name = 'sd-balance-strategy'


def get_current_dir():
    return os.getcwd()


def get_project_dir():
    return get_current_dir().split(_project_name)[0] + _project_name + "/"

