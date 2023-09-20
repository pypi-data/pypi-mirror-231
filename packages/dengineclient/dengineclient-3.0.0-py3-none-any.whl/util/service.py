import os

DEPLOY_PATH = '/home/xiaoju/sd-balance-strategy/.deploy/'
CLUSTER_FILE = DEPLOY_PATH + 'service.cluster.txt'
SERVICE_NAME_FILE = DEPLOY_PATH + 'service.service_name.txt'


def get_cluster():
    return _get_first_line(CLUSTER_FILE)


def get_service_name():
    return _get_first_line(SERVICE_NAME_FILE)


def _get_first_line(path):
    if not os.path.exists(path):
        return ""

    with open(path) as content:
        for line in content:
            return line.strip()
