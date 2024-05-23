import yaml
import logging.config
from module_1 import main
with open('logging_settings.yaml', 'rt') as f:
    config = yaml.safe_load(f.read())
logging.config.dictConfig(config)

main()
