def parse_filters(filter_str):
    filters = {}
    for item in filter_str.split(','):
        filter_name, filter_value = item.split('=')
        filters[filter_name.strip()] = float(filter_value.strip())
    return filters
