#! /usr/bin/python3.6
import logging
import sys
from config import config
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
sys.path.insert(0, config["sci-service_dir"])
from app import app as application
application.config.update(config)