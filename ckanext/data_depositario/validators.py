from ckan.common import json
from ckan.lib.navl.dictization_functions import Invalid
from ckan.logic.validators import int_validator
from ckan.common import _
import re
from datetime import datetime


def positive_integer_validator(value, context):
   if value is None:
      return None
   if hasattr(value, 'strip') and not value.strip():
      return None
   value = int_validator(value, context)
   if value < 1:
      raise Invalid(_('Must be a positive integer'))
   return value

def long_validator(value, context):
   if value is None:
      return None
   if hasattr(value, 'strip') and not value.strip():
      return None
   pattern = re.compile('^[-+]?(180(\.0+)?|((1[0-7]\d)|([1-9]?\d))(\.\d+)?)$')
   if re.match(pattern, value) is None:
      raise Invalid(_('Must be a valid longitude coordinate'))
   return value

def lat_validator(value, context):
   if value is None:
      return None
   if hasattr(value, 'strip') and not value.strip():
      return None
   pattern = re.compile('^[-+]?([1-8]?\d(\.\d+)?|90(\.0+)?)$')
   if re.match(pattern, value) is None:
      raise Invalid(_('Must be a valid latitude coordinate'))
   return value

def positive_float_validator(value, context):
   if value is None:
      return None
   if hasattr(value, 'strip') and not value.strip():
      return None
   value = float_validator(value, context)
   if value < 1:
      raise Invalid(_('Must be a positive float'))
   return value

def json_validator(value, context):
   if value == '':
      return value
   try:
      json.loads(value)
   except ValueError:
      raise Invalid('Invalid JSON')
   return value

def temp_res_validator(key, data, errors, context):
    if errors[key]:
        return

    value = data[key]

    if value == '':
        data[key] = None
        return

    if value[-1] == 'Z':
        return

    time_format = { u'date': ['%Y-%m-%d', 'YYYY-MM-DD'],
            u'month': ['%Y-%m', 'YYYY-MM'],
            u'year': ['%Y', 'YYYY'],
            u'decade': ['%Y', 'YYYY', 10],
            u'century': ['%Y', 'YYYY', 100] }
    temp_res = data.get(('temp_res',), '')
    if temp_res:
        try:
            if (temp_res == u'decade' or temp_res == u'century'):
                res = int(value)%time_format[temp_res][2]
                if (res != 0):
                    value = str(int(value) - res)
            value = datetime.strptime(value,
                    time_format[temp_res][0])
        except ValueError:
            raise Invalid(_('Date format incorrect') + _(', should be: ') + '%s' % time_format[temp_res][1])
        data[key] = value.isoformat() + 'Z'

def append_time_period(key, data, errors, context):
    if errors[key]:
        return

    value = data[key]
    if data.get(('time_period',), ''):
        out = json.loads(value)
        out.append(data[('time_period',)])
        data[key] = json.dumps(out)

def date_validator(key, data, errors, context):
    if errors[key]:
        return

    value = data[key]

    if value == '':
        data[key] = None
        return

    if value[-1] == 'Z':
        return

    time_format = ''
    is_error = [False, False, False]
    try:
        datetime.strptime(value, '%Y')
        time_format = '%Y'
    except ValueError: is_error[0] = True
    try:
        datetime.strptime(value, '%Y-%m')
        time_format = '%Y-%m'
    except ValueError: is_error[1] = True
    try:
        datetime.strptime(value, '%Y-%m-%d')
        time_format = '%Y-%m-%d'
    except ValueError: is_error[2] = True
    if len(set(is_error)) <= 1:
        raise Invalid(_('Date format incorrect'))
    data[key] = datetime.strptime(value, time_format).isoformat() + 'Z'

def duplicate_validator(key, data, errors, context):
    if errors[key]:
        return
    value = json.loads(data[key])
    
    unduplicated = list(set(value))
    data[key] = json.dumps(unduplicated)

def remove_blank_wrap(value, context):
   return "".join(value.split())
