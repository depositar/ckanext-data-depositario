def remove_blank_wrap(value, context):
    """
    Remove blank and text wrap in the value.
    """
    return "".join(value.split())

def value_string_convert(key, data, errors, context):
    """
    Takes a list of values that is a comma-separated string (in data[key])
    and parses values. These are added to the data dict, enumerated. Borrowed
    from tag_string_convert in CKAN core.
    """
    if isinstance(data[key], basestring):
        values = [value.strip() \
                for value in data[key].split(',') \
                if value.strip()]
    else:
        values = data[key]

    data[key] = values
