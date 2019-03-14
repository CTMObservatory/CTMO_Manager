import yaml as _yaml

CONFIG_PATH = '/etc/ctmo/ctmo.conf.yaml'
_CONFIG_IS_LOADED = False
_config = {}


def load_config():
    global _config
    with open(CONFIG_PATH) as f:
        _config = _yaml.full_load(f.read())

def get_config():
    global _CONFIG_IS_LOADED
    global _config
    if not _CONFIG_IS_LOADED:
        load_config()
        _CONFIG_IS_LOADED = True
    return _config

def get_config_for_key(key):
    config = get_config()
    return config.get(key)
