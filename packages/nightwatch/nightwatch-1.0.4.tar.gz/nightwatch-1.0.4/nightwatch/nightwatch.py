import logging
import json
import os
import datetime
from kafkawrapper import sendData

ENV_LOG_LEVEL = os.environ.get('LOGGING_LEVEL')

class Nightwatch:
  def __init__(self):
    self.kafka_topic = os.environ.get('KAFKA_LOG_TOPIC')
    self.log_level = ['INFO', 'DEBUG', 'WARNING', 'ERROR', 'CRITICAL']
    LOG_LEVEL = {
      'INFO': ['INFO', 'DEBUG', 'WARNING', 'ERROR', 'CRITICAL'],
      'DEBUG': ['DEBUG', 'WARNING', 'ERROR', 'CRITICAL'],
      'WARNING': ['WARNING', 'ERROR', 'CRITICAL'],
      'ERROR': ['ERROR', 'CRITICAL'],
      'CRITICAL': ['CRITICAL'],
    }
    self.allowed_level = LOG_LEVEL[ENV_LOG_LEVEL]

 
  def log(self, message, data, log_level=logging.INFO, logger = True, console = False):
    try:
      if log_level in self.allowed_level:
        message = self.message_format(message, data)
        if logger == True:
          current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
          formatted_message = f"{current_time} {log_level} {message}"
          sendData(self.kafka_topic, formatted_message, {})
        if console == True:
           print(f"{formatted_message}")
    except Exception as e:
      print(f'Error in log {str(e)}')
    
  def message_format(self, message_string, data = {}):
    try:
      message_string += ' '
      if isinstance(data, list) or isinstance(data, dict) or isinstance(data, tuple):
        message_string += json.dumps(data) if len(data) > 2 else ''
      elif isinstance(data, str):
        message_string += data
      elif isinstance(data, int) or isinstance(data, float) or isinstance(data, bool):
        message_string += str(data)
      elif data is None:
        message_string += 'None'
    except Exception as e:
      print(f'Error in message formatting {str(e)}')
    return message_string

  def info(self, message, data = {}, logger = True, console = False):
    self.log(message, data, 'INFO', logger, console)

  def debug(self, message, data = {}, logger = True, console = False):
    self.log(message, data, 'DEBUG', logger, console)

  def warning(self, message, data = {}, logger = True, console = False):
    self.log(message, data, 'WARNING', logger, console)

  def error(self, message, data = {}, logger = True, console = False):
    self.log(message, data, 'ERROR', logger, console)

  def critical(self, message, data = {}, logger = True, console = False):
    self.log(message, data, 'CRITICAL', logger, console)
