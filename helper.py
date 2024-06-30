def parse_filters(filter_str):
    filters = {}
    for item in filter_str.split(','):
        filter_name, filter_value = item.split('=')
        if filter_name.strip() not in filters:
            filters[filter_name.strip()] = []
        filters[filter_name.strip()].append(float(filter_value.strip()))
    return filters
